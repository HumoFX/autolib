from django.db import models
from Apps.Book.models import Book


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey('User.User', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    time_of_get = models.DateTimeField()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return "{} : {} - {}".format(self.user, self.book, self.time_of_get)


class BookInUse(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    user_id = models.ForeignKey('User.User', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    time_of_get = models.DateTimeField()
    time_of_pass = models.DateTimeField()

    class Meta:
        verbose_name = 'Архив пользований книг'

    def __str__(self):
        return "{} : {} - {} , {}".format(self.user_id, self.book, self.time_of_get, self.time_of_pass)