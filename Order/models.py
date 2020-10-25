from datetime import datetime

from dateutil.utils import today
from django.db import models


# from User.models import Users

# Create your models here.
from pytz import timezone

from elib.settings import TIME_ZONE


class Order(models.Model):
    user = models.ForeignKey('User.Profile', on_delete=models.CASCADE)
    book = models.ForeignKey('Book.Book', on_delete=models.CASCADE)
    time_of_get = models.DateTimeField(auto_now_add=False, verbose_name='Время получения книги(заказ)', null=False)
    time_of_order = models.DateTimeField(auto_now_add=True, verbose_name='Время заказа')
    time_of_take_away = models.DateTimeField(auto_now_add=False, verbose_name='Время унесения книги',
                                             blank=True, null=True)
    time_of_pass = models.DateTimeField(auto_now_add=False, verbose_name='Время возвращения книги',
                                        blank=True, null=True)
    active = models.BooleanField(verbose_name='Активный', default=True)
    done = models.BooleanField(verbose_name='Заказ получен', default=False)
    retrieved = models.BooleanField(verbose_name='Возвращен', default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return "{} - {}".format(self.id, self.user)


# class BookInUse(models.Model):
#     order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
#     user_id = models.ForeignKey('User.Profile', on_delete=models.CASCADE)
#     book = models.ForeignKey('Book.Book', on_delete=models.CASCADE, default='')
#     time_of_get = models.DateTimeField(auto_now_add=False, verbose_name='Время полчения книги', null=False)
#     time_of_pass = models.DateTimeField(auto_now_add=False, verbose_name='Время возврата книги', null=True)
#
#     class Meta:
#         verbose_name = 'Архив пользований книг'
#
#     def __str__(self):
#         return ", {}".format(self.time_of_get, self.time_of_pass)
