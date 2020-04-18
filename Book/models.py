from django.conf import settings
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class UDC(models.Model):
    id_number = models.CharField(max_length=128, default='0')

    class Meta:
        verbose_name = 'УДК'
        verbose_name_plural = 'УДК'

    def __str__(self):
        return self.id_number


class Category(models.Model):
    udc_id = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    # class MPTTMeta:
    #     order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категорий'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return "{} - {}".format(self.name, self.udc_id)
        # return self.name


class Book(models.Model):
    title = models.CharField(max_length=512, name='Название')
    author = models.CharField(max_length=512, name='Автор')
    udc = models.ForeignKey(Category, on_delete=models.CASCADE, name='УДК')
    isbn = models.CharField(max_length=512, default='')
    key_words = models.TextField(name="ключевые_слова", default='')
    img = models.ImageField(upload_to='img/books', name='Обложка(Фото)', null=True)
    university = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name='Университет')
    faculty = models.ForeignKey('University.Faculty', on_delete=models.CASCADE, name='Факультет', null=True)
    quantity = models.IntegerField(name='Количество', default=0)
    price = models.FloatField(name='Цена', default=0)
    rating = models.FloatField(name='Рейтинг', default=0)
    used = models.IntegerField(name='Использовано', default=0)
    e_book = models.BooleanField(name='Электроная_версия', default=False)
    file = models.FileField(upload_to='file/e_books', null=True, blank=True, name='Файл')
    printed_book = models.BooleanField(name='Печатная_версия', default=False)
    special_books = models.BooleanField(name='Редкая_книга')
    work_book = models.BooleanField(name='Учебное_пособие')
    date_pub = models.DateField(auto_now_add=False, name='Опубликовано', null=True)
    date_get = models.DateField(auto_now_add=False, name='Получено', null=True)
    created = models.DateField(auto_now_add=True, )

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'
        constraints = [models.UniqueConstraint(fields=['Название', 'Автор', 'Опубликовано'], name='book')]

    def __str__(self):
        return "{} - {}".format(self.Название, self.УДК)
        # return self.name


class ALL(models.Model):
    title = models.CharField(max_length=512, name='Название')
    author = models.CharField(max_length=512, name='Автор')
    udc = models.ForeignKey(Category, on_delete=models.CASCADE, name='УДК')
    key_words = models.TextField(name="ключевые_слова", default='')
    img = models.ImageField(upload_to='img/books', name='Обложка(Фото)')
    e_book = models.BooleanField(name='Электроная_версия', default=False)
    file = models.FileField(upload_to='file/e_books', null=True, blank=True, name='Файл')
    date_pub = models.DateField(auto_now_add=False, name='Опубликовано', null=True)

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Все Книги'
        constraints = [models.UniqueConstraint(fields=['id', 'Название', 'Автор', 'Опубликовано'], name='allbooks')]