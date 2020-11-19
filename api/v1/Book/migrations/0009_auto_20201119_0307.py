# Generated by Django 3.0.7 on 2020-11-18 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0008_auto_20201119_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='entries', through='Book.AuthorEntryRank', to='Book.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Book.DocumentType'),
        ),
    ]