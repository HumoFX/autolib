from django.contrib import admin
from django.contrib.admin.templatetags.admin_urls import register
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from mptt.admin import DraggableMPTTAdmin, MPTTModelAdmin
from .models import Category, UDC, Book, LibraryStorageEntry, LibraryStorage, DocumentType, UDCImage
from ajax_select.admin import AjaxSelectAdmin
from ajax_select import make_ajax_form

from .models import (
    Author,
    Editor,
    Journal,
    Publisher,
    Collection,
    AuthorEntryRank,
    Language
)


@register.filter
def publication_date(entry):
    """We expect an entry object to filter"""
    if entry.is_partial_publication_date:
        fmt = "%Y"
    else:
        fmt = "%F %Y"
    return entry.publication_date.strftime(fmt)


class LibraryStorageAdmin(admin.ModelAdmin):
    model = LibraryStorage
    fields = ['name', 'abbreviation']

    def save_model(self, request, obj, form, change):
        university = request.user.university_id
        obj.university = university
        obj.save()


class LibraryStorageEntryInline(admin.TabularInline):
    extra = 1
    model = LibraryStorageEntry
    ordering = ("entry_number",)

    def get_queryset(self, request):
        queryset = LibraryStorageEntry.objects.filter(storage__university_id=request.user.university_id)
        print(queryset)
        return queryset


class AuthorEntryRankInline(admin.TabularInline):
    extra = 1
    model = AuthorEntryRank
    ordering = ("rank",)


class AbstractHumanAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
    ordering = ("last_name", "first_name")


class AuthorAdmin(AbstractHumanAdmin):
    list_display = ("last_name", "first_name", "user")
    raw_id_fields = ("user",)


class EditorAdmin(AbstractHumanAdmin):
    raw_id_fields = ("user",)


class AbstractEntityAdmin(admin.ModelAdmin):
    ordering = ("name",)


class JournalAdmin(AbstractEntityAdmin):
    pass


class PublisherAdmin(AbstractEntityAdmin):
    pass


class CategoryAdmin(AjaxSelectAdmin):
    form = make_ajax_form(Category, {
        # fieldname: channel_name
        'udc_id': 'category',
        'parent': 'parent_id'
    })


class UDCAdmin(AjaxSelectAdmin, DraggableMPTTAdmin):
    form = make_ajax_form(UDC, {
        # fieldname: channel_name
        'udc': 'udc_num',
        'parent': 'parent'
    })
    list_display = (
        'tree_actions',
        'indented_title',
        'name',
        'udc',
        'get_descendant_count'
    )


class BookAdmin(AjaxSelectAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    # fields = ('Факультет', 'Количество', 'Цена', ' Рейтинг', ' Использовано', 'Опубликовано', 'created')
    form = make_ajax_form(Book, {
        # fieldname: channel_name
        'udc': 'udc',
        'udc_new': 'udc_new'
    })

    def has_change_permission(self, request, obj=None):
        univer = request.user.university_id.id
        if request.user.is_superuser:
            return True
        if obj is not None and obj.university.id == univer:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        univer = request.user.university_id.id
        if request.user.is_superuser:
            return True
        if obj is not None and obj.university.id == univer:
            return True
        else:
            return False


class EntryAdmin(BookAdmin, admin.ModelAdmin):
    # date_hierarchy = "publication_date"
    form = make_ajax_form(Book, {
        # fieldname: channel_name
        'udc': 'udc',
        'udc_new': 'udc_new',
        'editors': 'editors',
        'journal': 'journal',
        'publisher': 'publisher'
    })
    fieldsets = (
        (
            "Основные поля публикации",
            {
                "fields": (
                    "type",
                    "title",
                    "journal",
                    "volume",
                    ("pages", "language"),
                    ("publication_date", "is_partial_publication_date"),
                )
            },
        ),
        ("Идентификаторы", {"fields": (("doi", "issn", "pmid"), ("isbn", "isbn2", "inventory_number"))}),
        ("Книжные поля", {"fields": (("booktitle", "edition", "chapter"), ("udc", "udc_new"))}),
        ("Кандидатская диссертация", {"fields": ("school",)}),
        ("Труды", {"fields": ("organization",)}),
        (
            "Разное",
            {"fields": ("editors", "publisher", "address", "annote", "note")},
        ),
        ("Перекрестные ссылки", {"fields": ("crossref",)}),
        (
            "Дополнительная информациия",
            {
                "fields": (
                    ("printed_book", "e_book", "special_books"),
                    ("img", "file"),
                    "key_words",
                    ("quantity", "real_time_count"),
                    "price",
                    "used",
                    "date_get"
                )
            }
        )
    )
    inlines = (AuthorEntryRankInline, LibraryStorageEntryInline)
    list_display = ("title", "first_author", "type", "publication_date", "journal")
    list_filter = ("publication_date", "journal", "authors", "type")
    list_per_page = 100
    list_select_related = True
    ordering = ("-publication_date",)
    raw_id_fields = ("authors", "crossref")
    search_fields = ("title",)
    # save_as = True
    # save_on_top = True
    # change_list_template = 'Book/books.html'

    def save_model(self, request, obj, form, change):
        university = request.user.university_id
        obj.university = university
        print(obj)
        obj.save()


class CollectionAdmin(admin.ModelAdmin):
    def size(self, obj):
        """Get the number of entries in each collection"""
        return obj.entries.count()

    list_display = ("name", "size")
    raw_id_fields = ("entries",)


admin.site.register(LibraryStorageEntry)
admin.site.register(LibraryStorage, LibraryStorageAdmin)
admin.site.register(Language)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Editor, EditorAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, EntryAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UDC, UDCAdmin)
admin.site.register(UDCImage)
admin.site.register(DocumentType)
