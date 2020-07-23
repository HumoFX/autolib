from django.db import models
# from User.models import Users

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey('User.Profile', on_delete=models.CASCADE)
    book = models.ForeignKey('Book.Book', on_delete=models.CASCADE)
    time_of_get = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(verbose_name='Активный', default=False)
    done = models.BooleanField(verbose_name='Заказ получен', default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return "{} - {}".format(self.user, self.time_of_get)


class BookInUse(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    # user_id = models.ForeignKey('User.User', on_delete=models.CASCADE)
    book = models.ForeignKey('Book.Book', on_delete=models.CASCADE, default='')
    time_of_get = models.DateTimeField()
    time_of_pass = models.DateTimeField()

    class Meta:
        verbose_name = 'Архив пользований книг'

    def __str__(self):
        return ", {}".format(self.time_of_get, self.time_of_pass)