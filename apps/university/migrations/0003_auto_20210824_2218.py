# Generated by Django 3.2.6 on 2021-08-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_auto_20201121_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='university',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]