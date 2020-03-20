# Generated by Django 3.0.4 on 2020-03-18 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Order', '__first__'),
        ('Book', '0001_initial'),
        ('University', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_number', models.CharField(max_length=16)),
                ('Ф.И.О.', models.CharField(max_length=256)),
                ('Аватар', models.ImageField(upload_to='img/users')),
                ('role', models.CharField(max_length=20)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Факультет', to='University.Faculty')),
                ('time_of_get_book', models.ManyToManyField(to='Order.BookInUse')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Университет', to='University.University')),
                ('Полученные книги', models.ManyToManyField(to='Book.Book')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]