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


class Category(MPTTModel):
    udc_id = models.OneToOneField(UDC, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['name']

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
    key_words = models.TextField(name="ключевые слова", default='')
    img = models.ImageField(upload_to='img/books', name='Обложка(Фото)')
    university = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name='Университет')
    faculty = models.ForeignKey('University.Faculty', on_delete=models.CASCADE, name='Факультет')
    quantity = models.IntegerField(name='Количество')
    price = models.FloatField(name='Цена')
    rating = models.FloatField(name='Рейтинг')
    used = models.IntegerField(name='Использовано')
    e_book = models.BooleanField(name='Электроная версия', default=False)
    file = models.FileField(upload_to='file/e_books', null=True, blank=True, name='Файл(Книга)')
    printed_book = models.BooleanField(name='Печатная версия', default=False)
    special_books = models.BooleanField(name='Редкая книга')
    work_book = models.BooleanField(name='Учебное пособие')
    date_pub = models.DateField(auto_now_add=False, name='Опубликовано')
    date_get = models.DateField(auto_now_add=False, name='Получено')
    created = models.DateField(auto_now_add=True,)

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'
        # ordering=['created',]

    def __str__(self):
        return "{} - {}".format(self.Название, self.УДК)
        # return self.name
