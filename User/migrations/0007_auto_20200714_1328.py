# Generated by Django 3.0.4 on 2020-07-14 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0001_initial'),
        ('User', '0006_auto_20200714_1305'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]
