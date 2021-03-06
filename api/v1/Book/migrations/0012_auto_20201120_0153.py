# Generated by Django 3.0.7 on 2020-11-19 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0011_auto_20201120_0145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('-publication_date',), 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='journal',
            options={'verbose_name': 'Журнал', 'verbose_name_plural': 'Журналы'},
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='entries', through='Book.AuthorEntryRank', to='Book.Author', verbose_name='Авторы'),
        ),
        migrations.AlterField(
            model_name='book',
            name='doi',
            field=models.CharField(blank=True, help_text='Идентификатор цифрового объекта этого ресурса', max_length=100, verbose_name='DOI'),
        ),
        migrations.AlterField(
            model_name='book',
            name='editors',
            field=models.ManyToManyField(blank=True, related_name='entries', to='Book.Editor', verbose_name='Редакторы'),
        ),
        migrations.AlterField(
            model_name='book',
            name='is_partial_publication_date',
            field=models.BooleanField(default=True, help_text='Отметьте это, если дата публикации не указана (например, если действителен только год)', verbose_name='Дата частичной публикации?'),
        ),
        migrations.AlterField(
            model_name='book',
            name='journal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='Book.Journal', verbose_name='Журнал'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(null=True, verbose_name='Дата издания'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='Book.Publisher', verbose_name='Издатель'),
        ),
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Book.DocumentType', verbose_name='Характер документа'),
        ),
    ]
