import datetime

from django.db import models

# from User.models import Users
from apps.user.models import Profile
from apps.book.models import Book


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # time_of_get = models.DateTimeField(auto_now_add=False, verbose_name='Время получения книги(заказ)', null=False)
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

    @property
    def status(self):
        status = ''
        if self.active:
            status = 'активный заказ'
        elif self.done:
            status = 'книга выдана'
        elif self.retrieved:
            status = 'книга возвращена'
        return status

    def progress(self):
        if self.active and not self.done:
            self.active = False
            self.done = True
            self.time_of_take_away = datetime.datetime.now()
        elif self.done and not self.retrieved:
            self.done = False
            self.retrieved = True
            self.time_of_pass = datetime.datetime.now()
        self.save()
        return self

    # @property
    # def is_order_expired(self):
    #     tz = timezone(TIME_ZONE)
    #     if self.time_of_get >= datetime.today(tz)

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
