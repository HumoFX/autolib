# Generated by Django 3.0 on 2020-12-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0020_auto_20201215_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
