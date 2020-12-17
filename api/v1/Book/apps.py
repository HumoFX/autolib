from django.apps import AppConfig


class BookConfig(AppConfig):
    name = 'Book'

    class Meta:
        verbose_name = 'Книгa'
        verbose_plural_name = 'Книги'
