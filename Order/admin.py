from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from .models import Order, BookInUse


# Register your models here.
class BookResource(resources.ModelResource):
    class Meta:
        model = BookInUse
        skip_unchanged = True


class BookAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    # fields = ('Факультет', 'Количество', 'Цена', ' Рейтинг', ' Использовано', 'Опубликовано', 'created')

    resource_class = BookResource


class AllResource(resources.ModelResource):
    class Meta:
        model = Order
        skip_unchanged = True


class ALLAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    # fields = ('Факультет', 'Количество', 'Цена', ' Рейтинг', ' Использовано', 'Опубликовано', 'created')

    resource_class = AllResource


admin.site.register(Order, ALLAdmin)
admin.site.register(BookInUse, BookAdmin)
