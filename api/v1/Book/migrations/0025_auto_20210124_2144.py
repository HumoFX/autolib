# Generated by Django 3.0 on 2021-01-24 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0024_auto_20201225_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publisher', to='Book.Publisher', verbose_name='Издатель'),
        ),
    ]