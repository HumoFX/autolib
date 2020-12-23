from datetime import time

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _
from partial_date import PartialDateField

# Create your models here.
from requests import Response

from api.v1.University.models import Faculty, University


class AbstractHuman(models.Model):
    """Simple Abstract Human model
    Note that this model may be linked to django registered users
    """

    first_name = models.CharField(_("Имя"), max_length=100, null=True, blank=True)
    last_name = models.CharField(_("Фамилия"), max_length=100, null=True)
    first_initial = models.CharField(_("Инициалы"), max_length=10, blank=True, null=True)

    # This is a django user
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.get_formatted_name()

    def save(self, *args, **kwargs):
        """Set initials and try to set django user before saving"""

        self._set_first_initial()
        self._set_user()
        super(AbstractHuman, self).save(*args, **kwargs)

    def _set_first_initial(self, force=False):
        """Set author first name initial"""

        if self.first_initial and not force:
            return
        self.first_initial = " ".join([c[0] for c in self.first_name.split()])

    def get_formatted_name(self):
        """Return author formated full name, e.g. Maupetit J"""

        return "%s %s" % (self.last_name, self.first_initial)

    def _set_user(self):
        """Look for local django user based on human name"""

        if "" in (self.last_name, self.first_name):
            return

        self._set_first_initial()

        User = get_user_model()
        try:
            self.user = User.objects.get(
                models.Q(last_name__iexact=self.last_name),
                models.Q(first_name__iexact=self.first_name)
                | models.Q(first_name__istartswith=self.first_initial[0]),
            )
        except User.DoesNotExist:
            pass
        except User.MultipleObjectsReturned:
            pass


class Author(AbstractHuman):
    """Entry author"""

    class Meta:
        ordering = ("last_name", "first_name")
        verbose_name = _("Автор")
        verbose_name_plural = _("Авторы")


class Editor(AbstractHuman):
    """Journal or book editor"""

    class Meta:
        ordering = ("last_name", "first_name")
        verbose_name = _("Редактор")
        verbose_name_plural = _("Редакторы")


class AbstractEntity(models.Model):
    """Simple abstract entity"""

    name = models.CharField(_("Наименование"), max_length=150)
    abbreviation = models.CharField(
        _("Аббревиатура/код объекта"),
        max_length=100,
        blank=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Language(AbstractEntity):
    """Document content language"""

    class Meta:
        verbose_name = _("Язык")
        verbose_name_plural = _("Языки")


class Journal(AbstractEntity):
    """Peer reviewed journal"""

    class Meta:
        verbose_name = _("Журнал")
        verbose_name_plural = _("Журналы")


class DocumentType(AbstractEntity):
    """Type of entry"""

    class Meta:
        verbose_name = _("Характер документа")
        verbose_name_plural = _("Характер документов")


class Publisher(AbstractEntity):
    """Journal or book publisher"""

    class Meta:
        verbose_name = _("Издатель")
        verbose_name_plural = _("Издатели")


class UDC(MPTTModel):
    """Universal Decimal Classification"""
    udc = models.CharField(max_length=64, verbose_name='Код УДК')
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    parent = TreeForeignKey('self', null=True, default="", blank=True, related_name='children',
                            on_delete=models.CASCADE, verbose_name='Родительский удк')


    class Meta:
        verbose_name = _("УДК")
        verbose_name_plural = _("УДК")

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.udc, self.name)


class LibraryStorage(AbstractEntity):
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Место хранения документов")
        verbose_name_plural = _("Места хранения документов")


class Category(models.Model):
    udc_id = models.CharField(max_length=64, unique=True, )
    name = models.TextField(unique=True)
    parent = models.ForeignKey('self', null=True, default="", blank=True, related_name='childrens',
                               on_delete=models.CASCADE, verbose_name='Родительский удк')

    class Meta:
        verbose_name = 'Категорий'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return "{} - {}".format(self.name, self.udc_id)


class CopyrightMark(AbstractEntity):
    class Meta:
        verbose_name = _("Авторсикй знак")
        verbose_name_plural = _("Авторский знак")


class Book(models.Model):
    udc = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='УДК', null=True,
                            verbose_name="УДК", help_text="Временно")
    udc_new = models.ForeignKey(UDC, on_delete=models.SET_NULL, null=True, verbose_name="УДК*",
                                help_text="Универасальная "
                                          "десятичная "
                                          "классификация")
    copyright_mark = models.ForeignKey(CopyrightMark, on_delete=models.CASCADE, verbose_name="Авторский знак", null=True, blank=True)
    key_words = models.TextField(verbose_name="Ключевые слова", default='', blank=True)
    img = models.ImageField(upload_to='img/books', verbose_name='Обложка(Фото)', null=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, verbose_name='Университет',
                                   blank=False)
    date_get = models.DateField(auto_now_add=False, verbose_name='Дата получения', null=True)
    created = models.DateField(auto_now_add=True, )

    # Base fields
    type = models.ForeignKey(
        "DocumentType", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Характер документа"
    )

    title = models.CharField(
        _("Заглавие"), blank=True, max_length=512)

    authors = models.ManyToManyField(
        "Author", related_name="entries", through="AuthorEntryRank", blank=True, verbose_name="Авторы"
    )
    journal = models.ForeignKey(
        "Journal", related_name="entries", blank=True, null=True, on_delete=models.CASCADE, verbose_name="Журнал"
    )
    publication_date = PartialDateField(_("Дата издания"), null=True)
    is_partial_publication_date = models.BooleanField(
        _("Дата частичной публикации?"),
        default=True,
        help_text=_(
            "Отметьте это, если дата публикации не указана (например, если действителен только год)"
        ),
    )
    volume = models.CharField(
        _("Том"),
        max_length=50,
        blank=True,
        help_text=_("Том книги/журнала"),
    )
    pages = models.CharField(
        _("Страницы"),
        max_length=50,
        blank=True,
        help_text=_("Номера страниц, разделенные запятыми или двойным дефисом"),
    )

    # Identifiers
    doi = models.CharField(
        _("DOI"),
        max_length=100,
        blank=True,
        help_text=_("Идентификатор цифрового объекта этого ресурса"),
    )
    issn = models.CharField(
        _("ISSN"),
        max_length=20,
        blank=True,
        help_text=_("Международный стандартный серийный номер"),
    )
    isbn = models.CharField(
        _("ISBN"),
        max_length=20,
        blank=True,
        help_text=_("Международный стандартный номер книги"),
    )
    isbn2 = models.CharField(
        _("ISBN 2"),
        max_length=20,
        blank=True,
        help_text=_("Международный стандартный номер книги"),
    )
    pmid = models.CharField(
        _("PMID"), blank=True, max_length=20, help_text=_("Pubmed ID")
    )
    inventory_number = models.CharField(_("Инвентарный номер"), blank=True, max_length=100,
                                        help_text=_(
                                            "Инвертизационные номера, разделенные запятыми или двойным дефисом"))

    # Book
    booktitle = models.CharField(
        _("Название книги"),
        max_length=50,
        blank=True,
        help_text=_("Название книги, если цитируется только ее часть"),
    )
    edition = models.CharField(
        _("Издание"),
        max_length=100,
        blank=True,
        help_text=_(
            "Издание книги"
        ),
    )
    chapter = models.CharField(_("Количество глав"), max_length=50, blank=True)

    # PhD Thesis
    school = models.CharField(
        _("Школа"),
        max_length=50,
        blank=True,
        help_text=_("Школа, в которой была написана диссертация"),
    )

    # Proceedings
    organization = models.CharField(
        _("Организция"),
        max_length=50,
        blank=True,
        help_text=_("Спонсор конференции"),
    )

    # Misc
    editors = models.ManyToManyField("Editor", related_name="entries", blank=True, verbose_name="Редакторы")
    publisher = models.ForeignKey(
        "Publisher",
        related_name="entries",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Издатель"
    )
    address = models.CharField(
        _("Адрес"),
        max_length=250,
        blank=True,
        help_text=_(
            "Адрес издателя"
        ),
    )
    annote = models.CharField(
        _("Аннотация"),
        max_length=250,
        blank=True,
        help_text=_("Аннотация"),
    )
    note = models.TextField(
        _("Заметка"), blank=True, help_text=_("Разная дополнительная информация")
    )
    e_book = models.BooleanField(verbose_name='Электроная версия', default=False)
    file = models.FileField(upload_to='file/e_books', null=True, blank=True, verbose_name='Файл')
    printed_book = models.BooleanField(verbose_name='Печатная версия', default=False)
    special_books = models.BooleanField(verbose_name='Редкая книга', default=False)
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество', default=0)
    real_time_count = models.PositiveSmallIntegerField(verbose_name='Кол-во книги на данный момент', default=0)
    price = models.FloatField(verbose_name='Цена', default=0)
    rating = models.FloatField(verbose_name='Рейтинг', default=0)
    used = models.PositiveIntegerField(verbose_name='Использовано', default=0)
    language = models.ForeignKey("Language", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Язык")
    # Related publications
    crossref = models.ManyToManyField("self", blank=True, verbose_name="Связанные публикации ")

    class Meta:
        verbose_name = _("Книга")
        verbose_name_plural = _("Книги")
        ordering = ("-publication_date",)

    # def clean(self):
    #     if self.is_partial_publication_date:
    #         fmt = "%Y"
    #     else:
    #         fmt = "%F %Y"
    #     return self.publication_date.strftime(fmt)

    def __str__(self):
        """Format entry with a default bibliography style"""
        # Authors
        author_str = "%(last_name)s %(first_initial)s"
        s = ", ".join([author_str % a.__dict__ for a in self.get_authors()])
        s = ", и ".join(s.rsplit(", ", 1))  # last author case
        s += ", "

        # Title
        s += '"%(title)s", ' % self.__dict__

        # Journal
        if self.journal:
            if self.journal.abbreviation:
                s += "в %(abbreviation)s, " % self.journal.__dict__
            else:
                # fall back to the real name
                s += "в %(name)s, " % self.journal.__dict__

        # Misc
        if self.volume and self.pages:
            s += "том. %(volume)s, стр. %(pages)s, " % self.__dict__
        # if self.publication_date:
        #     s += "%s." % self.publication_date.strftime("%B %Y")

        return s

    def _get_first_author(self):
        """
        Get this entry first author
        """
        if not len(self.get_authors()):
            return ""
        return self.get_authors()[0]

    first_author = property(_get_first_author)

    def _get_last_author(self):
        """
        Get this entry last author
        """
        if not len(self.get_authors()):
            return ""
        return self.get_authors()[-1]

    last_author = property(_get_last_author)

    def get_authors(self):
        """
        Get ordered authors list
        Note that authorentryrank_set is ordered as expected while the authors
        queryset is not (M2M with a through case).
        """
        return [aer.author for aer in self.authorentryrank_set.all()]

    def get_storages(self):

        """
        Get ordered storage list
        Note that librarystorageentry_set is ordered as expected while the storages
        queryset is not (M2M with a through case).
        """
        return [stg.storage for stg in self.librarystorageentry_set.all()]

    def decrement_book(self, book_id):
        """

        :rtype: object
        """
        query = self.objects.get(id=book_id)
        if query.real_time_count > 0:
            query.real_time_count = query.real_time_count - 1

        return query.save()

    def increment_book(self, book_id):
        """

        :rtype: object
        """
        query = self.objects.get(id=book_id)
        if query.quantity > query.real_time_count:
            query.real_time_count = query.real_time_count + 1

        return query.save()


class Collection(models.Model):
    """Define a collection of entries"""

    name = models.CharField(_("Название"), max_length=100)
    short_description = models.TextField(_("Краткое описание"), blank=True, null=True)
    entries = models.ManyToManyField("Book", related_name="collections")

    class Meta:
        verbose_name = _("Коллекция")
        verbose_name_plural = _("Коллекции")

    def __str__(self):
        return self.name


class AuthorEntryRank(models.Model):
    """Give the author rank for an entry author sequence"""

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    entry = models.ForeignKey(Book, on_delete=models.CASCADE)
    rank = models.IntegerField(
        _("Ранг"), help_text=_("Место автора в последовательности авторов статьи")
    )

    class Meta:
        verbose_name = _("Авторский рейтинг")
        verbose_name_plural = _("Авторский рейтинг")
        ordering = ("rank",)

    def __str__(self):
        return "%(author)s:%(rank)d:%(entry)s" % {
            "author": self.author,
            "entry": self.entry,
            "rank": self.rank,
        }


class LibraryStorageEntry(models.Model):
    """Give the storage amount of entry"""

    storage = models.ForeignKey(LibraryStorage, on_delete=models.CASCADE)
    entry = models.ForeignKey(Book, on_delete=models.CASCADE)
    entry_number = models.IntegerField(
        _("Количество книг"), help_text=_("Количество книг в местах для хранения")
    )

    class Meta:
        verbose_name = _("Хранилище")
        verbose_name_plural = _("Хранилище")
        ordering = ("entry_number",)

    def __str__(self):
        return "%(storage)s:%(entry_number)d:%(entry)s" % {
            "storage": self.storage,
            "entry": self.entry,
            "entry_number": self.entry_number,
        }


class UDCImage(models.Model):
    udc = models.OneToOneField(UDC, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/udc', verbose_name='Иконка')
