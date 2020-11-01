from django.db import models


# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=25)
    logo = models.ImageField(name="Логотип", upload_to='img/universities', null=True)
    faculties = models.ManyToManyField(Faculty)

    class Meta:
        verbose_name = 'Университет'
        verbose_name_plural = 'Университеты'

    def __str__(self):
        return self.short_name
