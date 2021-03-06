# Generated by Django 3.0.7 on 2020-11-18 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Book', '0007_auto_20201118_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('first_initial', models.CharField(blank=True, max_length=10, verbose_name='First Initial(s)')),
                ('alias', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aliases', related_query_name='alias_human', to='Book.Author')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('abbreviation', models.CharField(blank=True, max_length=100, verbose_name='Аббревиатура/код объекта')),
            ],
            options={
                'verbose_name': 'Характер документа',
                'verbose_name_plural': 'Характер документов',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('abbreviation', models.CharField(blank=True, max_length=100, verbose_name='Аббревиатура/код объекта')),
            ],
            options={
                'verbose_name': 'Журанл',
                'verbose_name_plural': 'Журналы',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('abbreviation', models.CharField(blank=True, max_length=100, verbose_name='Аббревиатура/код объекта')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
            },
        ),
        migrations.CreateModel(
            name='LibraryStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('abbreviation', models.CharField(blank=True, max_length=100, verbose_name='Аббревиатура/код объекта')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='University.University')),
            ],
            options={
                'verbose_name': 'Место хранения документов',
                'verbose_name_plural': 'Места хранения документов',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('abbreviation', models.CharField(blank=True, max_length=100, verbose_name='Аббревиатура/код объекта')),
            ],
            options={
                'verbose_name': 'Издатель',
                'verbose_name_plural': 'Издатели',
            },
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('-publication_date',), 'verbose_name': 'Entry', 'verbose_name_plural': 'Entries'},
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='date_pub',
        ),
        migrations.RemoveField(
            model_name='book',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='book',
            name='work_book',
        ),
        migrations.RemoveField(
            model_name='udc',
            name='id_number',
        ),
        migrations.AddField(
            model_name='book',
            name='address',
            field=models.CharField(blank=True, help_text='Адрес издателя', max_length=250, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='book',
            name='annote',
            field=models.CharField(blank=True, help_text='Аннотация', max_length=250, verbose_name='Аннотация'),
        ),
        migrations.AddField(
            model_name='book',
            name='booktitle',
            field=models.CharField(blank=True, help_text='Название книги, если цитируется только ее часть', max_length=50, verbose_name='Название книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='chapter',
            field=models.CharField(blank=True, max_length=50, verbose_name='Количество глав'),
        ),
        migrations.AddField(
            model_name='book',
            name='crossref',
            field=models.ManyToManyField(blank=True, related_name='_book_crossref_+', to='Book.Book'),
        ),
        migrations.AddField(
            model_name='book',
            name='doi',
            field=models.CharField(blank=True, help_text='Идентификатор цифрового объекта для этого ресурса', max_length=100, verbose_name='DOI'),
        ),
        migrations.AddField(
            model_name='book',
            name='edition',
            field=models.CharField(blank=True, help_text='Издание книги', max_length=100, verbose_name='Издание'),
        ),
        migrations.AddField(
            model_name='book',
            name='is_partial_publication_date',
            field=models.BooleanField(default=True, help_text='Check this if the publication date is incomplete (for example if only the year is valid)', verbose_name='Partial publication date?'),
        ),
        migrations.AddField(
            model_name='book',
            name='issn',
            field=models.CharField(blank=True, help_text='Международный стандартный серийный номер', max_length=20, verbose_name='ISSN'),
        ),
        migrations.AddField(
            model_name='book',
            name='note',
            field=models.TextField(blank=True, help_text='Разная дополнительная информация', verbose_name='Заметка'),
        ),
        migrations.AddField(
            model_name='book',
            name='organization',
            field=models.CharField(blank=True, help_text='Спонсор конференции', max_length=50, verbose_name='Организция'),
        ),
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.CharField(blank=True, help_text='Номера страниц, разделенные запятыми или двойным дефисом', max_length=50, verbose_name='Страницы'),
        ),
        migrations.AddField(
            model_name='book',
            name='pmid',
            field=models.CharField(blank=True, help_text='Pubmed ID', max_length=20, verbose_name='PMID'),
        ),
        migrations.AddField(
            model_name='book',
            name='publication_date',
            field=models.DateField(null=True, verbose_name='Publication date'),
        ),
        migrations.AddField(
            model_name='book',
            name='school',
            field=models.CharField(blank=True, help_text='Школа, в которой была написана диссертация', max_length=50, verbose_name='Школа'),
        ),
        migrations.AddField(
            model_name='book',
            name='volume',
            field=models.CharField(blank=True, help_text='Том книги/журнала', max_length=50, verbose_name='Том'),
        ),
        migrations.AddField(
            model_name='udc',
            name='level',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='udc',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='udc',
            name='name',
            field=models.TextField(default='12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='udc',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='Book.UDC', verbose_name='Родительский удк'),
        ),
        migrations.AddField(
            model_name='udc',
            name='rght',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='udc',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='udc',
            name='udc',
            field=models.CharField(default='1', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='e_book',
            field=models.BooleanField(default=False, verbose_name='Электроная версия'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, help_text='Международный стандартный номер книги', max_length=20, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(blank=True, max_length=512, verbose_name='Заглавие'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='Book.Category', verbose_name='Родительский удк'),
        ),
        migrations.CreateModel(
            name='LibraryStorageEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_number', models.IntegerField(help_text='Количество книг в местах для хранения', verbose_name='Количество книг')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.Book')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.LibraryStorage')),
            ],
            options={
                'verbose_name': 'Хранилище',
                'verbose_name_plural': 'Хранилище',
                'ordering': ('entry_number',),
            },
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('first_initial', models.CharField(blank=True, max_length=10, verbose_name='First Initial(s)')),
                ('alias', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aliases', related_query_name='alias_human', to='Book.Editor')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Редактор',
                'verbose_name_plural': 'Редакторы',
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='Краткое описание')),
                ('entries', models.ManyToManyField(related_name='collections', to='Book.Book')),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
            },
        ),
        migrations.CreateModel(
            name='AuthorEntryRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(help_text='Место автора в последовательности авторов статьи', verbose_name='Ранг')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.Author')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.Book')),
            ],
            options={
                'verbose_name': 'Авторский рейтинг',
                'verbose_name_plural': 'Авторский рейтинг',
                'ordering': ('rank',),
            },
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='entries', through='Book.AuthorEntryRank', to='Book.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='editors',
            field=models.ManyToManyField(blank=True, related_name='entries', to='Book.Editor'),
        ),
        migrations.AddField(
            model_name='book',
            name='journal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='Book.Journal'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='Book.Publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Book.DocumentType'),
        ),
    ]
