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
    title = models.CharField(max_length=512, unique=True)
    author = models.CharField(max_length=512, unique=True)
    udc = models.ForeignKey(Category, on_delete=models.CASCADE)
    key_words = models.TextField(name="ключевые слова", default='')
    img = models.ImageField(upload_to='img/books')
    # university = models.ForeignKey(University, on_delete=models.CASCADE)
    faculty = models.ForeignKey('University.Faculty', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField(name='Цена')
    rating = models.FloatField(name='Рейтинг')
    used = models.IntegerField()
    e_book = models.BooleanField(name='Электроная версия', default=False)
    file = models.FileField(upload_to='file/e_books', null=True, blank=True)
    printed_book = models.BooleanField(name='Печатная версия', default=False)
    special_books = models.BooleanField(name='Спец книги')
    work_book = models.BooleanField(name='Учебное пособие')
    date_of_pub = models.DateField(name='Дата публикации')
    date_of_get = models.DateField(name='Дата получения')

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return "{} - {}".format(self.title, self.udc_id)
        # return self.name

