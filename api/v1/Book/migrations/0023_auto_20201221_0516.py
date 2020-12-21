# Generated by Django 3.0 on 2020-12-21 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0022_auto_20201221_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_initial',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Инициалы'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='book',
            name='udc_new',
            field=models.ForeignKey(help_text='Универасальная десятичная классификация', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Book.UDC', verbose_name='УДК*'),
        ),
        migrations.AlterField(
            model_name='editor',
            name='first_initial',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Инициалы'),
        ),
        migrations.AlterField(
            model_name='editor',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='editor',
            name='last_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Фамилия'),
        ),
    ]
