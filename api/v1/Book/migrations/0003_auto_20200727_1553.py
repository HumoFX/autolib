# Generated by Django 3.0.4 on 2020-07-27 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_auto_20200527_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]
