# Generated by Django 3.0.7 on 2020-11-20 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='Логотип',
        ),
        migrations.AddField(
            model_name='university',
            name='logo',
            field=models.ImageField(null=True, upload_to='img/universities', verbose_name='Логотип'),
        ),
    ]
