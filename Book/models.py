from datetime import time

from django.conf import settings
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
from requests import Response


class UDC(models.Model):
    id_number = models.CharField(max_length=128, default='0')

    class Meta:
        verbose_name = 'УДК'
        verbose_name_plural = 'УДК'

    def __str__(self):
        return self.id_number


class Category(models.Model):
    udc_id = models.CharField(max_length=64, unique=True, )
    name = models.TextField(unique=True)
    parent = models.ForeignKey('self', null=True, default="", blank=True, related_name='children',
                               on_delete=models.CASCADE)

    # class MPTTMeta:
    #     order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категорий'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return "{} - {}".format(self.name, self.udc_id)
        # return self.name


class Book(models.Model):
    title = models.CharField(max_length=512, verbose_name='Название', blank=False, default='')
    author = models.CharField(max_length=512, verbose_name='Автор', default='', unique=False)
    udc = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='УДК', null=True, to_field='udc_id')
    isbn = models.CharField(max_length=512, default='')
    key_words = models.TextField(verbose_name="Ключевые слова", default='')
    img = models.ImageField(upload_to='img/books', verbose_name='Обложка(Фото)', null=True)
    university = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Университет',
                                   blank=False)
    faculty = models.ForeignKey('University.Faculty', on_delete=models.CASCADE, verbose_name='Факультет', null=True,
                                blank=False)
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество', default=0)
    real_time_count = models.PositiveSmallIntegerField(verbose_name='Кол-во книги на данный момент', default=0)
    price = models.FloatField(verbose_name='Цена', default=0)
    rating = models.FloatField(verbose_name='Рейтинг', default=0)
    used = models.PositiveIntegerField(verbose_name='Использовано', default=0)
    e_book = models.BooleanField(verbose_name='Электроная_версия', default=False)
    file = models.FileField(upload_to='file/e_books', null=True, blank=True, verbose_name='Файл')
    printed_book = models.BooleanField(verbose_name='Печатная версия', default=False)
    special_books = models.BooleanField(verbose_name='Редкая книга', default=False)
    work_book = models.BooleanField(verbose_name='Учебное пособие', default=False)
    date_pub = models.DateField(auto_now_add=False, verbose_name='Опубликовано', null=True)
    date_get = models.DateField(auto_now_add=False, verbose_name='Получено', null=True)
    created = models.DateField(auto_now_add=True, )

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'

    # def __str__(self):
    #     return "{} - {}".format(self.title, self.udc)
    # return self.name

    def __str__(self):
        return '%s - %s' % (self.title, self.author)

    def decrement_book(self, book_id):
        """

        :rtype: object
        """
        query = self.objects.get(id=book_id)
        # print(query.real_time_count, '\n')
        if query.real_time_count > 0:
            query.real_time_count = query.real_time_count - 1
        # else:
        #     query.real_time_count = 0
        # print('query= ', query)
        # print('\n query.count=', query.real_time_count)
        return query.save()

    def increment_book(self, book_id):
        """

        :rtype: object
        """
        query = self.objects.get(id=book_id)
        # print(query.real_time_count, '\n')
        if query.quantity > query.real_time_count:
            query.real_time_count = query.real_time_count + 1
        # else:
        #     query.real_time_count = query.quantity
        # print('query= ', query)
        # print('\n query.count=', query.real_time_count)
        return query.save()
# class ALL(models.Model):
#     title = models.TextField(verbose_name='Название')
#     author = models.TextField(verbose_name='Автор')
#     udc = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='УДК')
#     key_words = models.TextField(verbose_name='ключевые_слова', default='')
#     img = models.ImageField(upload_to='img/books', verbose_name='Обложка(Фото)')
#     e_book = models.BooleanField(name='Электроная_версия', default=False)
#     file = models.FileField(upload_to='file/e_books', null=True, blank=True, verbose_name='Файл')
#     date_pub = models.DateField(auto_now_add=False, verbose_name='Опубликовано', null=True)

# class Meta:
#     verbose_name = 'Книгу'
#     verbose_name_plural = 'Все Книги'
#     constraints = [models.UniqueConstraint(fields=['id', 'title', 'author', 'pub_date'], name='allbooks')]
