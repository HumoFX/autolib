# Generated by Django 3.0.7 on 2020-12-01 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0020_auto_20201130_0508'),
    ]

    operations = [
        migrations.CreateModel(
            name='CopyrightMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('abbreviation', models.CharField(blank=True, max_length=100, verbose_name='Аббревиатура/код объекта')),
            ],
            options={
                'verbose_name': 'Авторсикй знак',
                'verbose_name_plural': 'Авторский знак',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='copyright_mark',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Book.CopyrightMark', verbose_name='Авторский знак'),
        ),
    ]
