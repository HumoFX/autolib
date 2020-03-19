from django.db import models
from Apps.Book.models import Book
from Apps.Order.models import BookInUse


# Create your models here.

class User(models.Model):
    qr_number = models.CharField(max_length=16)
    full_name = models.CharField(max_length=256, name='Ф.И.О.')
    logo = models.ImageField(name="Аватар", upload_to='img/users')
    role = models.CharField(max_length=20)
    university = models.ForeignKey('University.University', on_delete=models.PROTECT, related_name='Университет')
    faculty = models.ForeignKey('University.Faculty', on_delete=models.PROTECT, related_name='Факультет')
    reading_books = models.ManyToManyField(Book, name='Полученные книги')
    # used_books = models.ManyToManyField(Book, name='Сданные книги')
    time_of_get_book = models.ManyToManyField(BookInUse)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.full_name
