from django.contrib import admin
from import_export import resources, widgets, fields
from import_export.admin import ImportExportModelAdmin, ExportActionMixin, ImportExportActionModelAdmin

from .forms import DocumentForm
from .models import Category, UDC, Book, ALL
from University.models import University
from ajax_select.admin import AjaxSelectAdmin
from ajax_select import make_ajax_form


# Register your models here.
class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        skip_unchanged = True

        fields = ('id', 'Название', 'Автор', 'УДК', 'ключевые_слова', 'Обложка(Фото)', 'Электроная_версия', 'Файл',
                  'Опубликовано')
        # exlude = 'id'


class AllResource(resources.ModelResource):
    class Meta:
        model = ALL
        skip_unchanged = True
        import_id_fields = ('Название', 'Автор', 'Опубликовано')
        fields = ('id', 'Название', 'Автор', 'УДК', 'ключевые_слова', 'Обложка(Фото)', 'Электроная_версия', 'Файл',
                  'Опубликовано')


class ALLAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    # fields = ('Факультет', 'Количество', 'Цена', ' Рейтинг', ' Использовано', 'Опубликовано', 'created')

    ordering = ('Автор', 'УДК__name')
    search_fields = ['УДК__name', 'УДК__udc_id__id_number', 'Название', 'Автор']
    list_display = ('Название', 'Автор', 'УДК', 'Опубликовано')
    resource_class = AllResource


class CategoryAdmin(AjaxSelectAdmin):
    form = make_ajax_form(Category, {
        # fieldname: channel_name
        'udc_id': 'category',
        'parent': 'parent_id'
    })


class BookAdmin(AjaxSelectAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    # fields = ('Факультет', 'Количество', 'Цена', ' Рейтинг', ' Использовано', 'Опубликовано', 'created')
    form = make_ajax_form(Book, {
        # fieldname: channel_name
        'УДК': 'УДК'
    })

    ordering = ('Автор', 'УДК__name')
    search_fields = ['УДК__name', 'УДК__udc_id__id_number', 'Название', 'Автор', 'Получено', 'Опубликовано']
    list_filter = ('УДК', 'Университет')
    list_display = ('Название', 'Автор', 'УДК', 'Получено', 'Опубликовано', 'Рейтинг', 'Использовано')
    resource_class = BookResource

    # skip_unchanged = True

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Book.objects.all()
        if request.user.is_staff:
            univer = request.user.university_id.id
            return Book.objects.filter(Университет__university_id__id=univer)


#    # def has_change_permission(self, request, obj=None):
#     univer = request.user.university_id.id
#     obj = Book.objects.all()
#     if request.user.is_staff:
#         for objs in obj:
#             print(objs)
#             print(objs.Университет.university_id.id)
#             print(request.user.university_id.id)
#             if objs.Университет.university_id.id == request.user.university_id.id:
#                 return True
#             else:
#                 return False


# class BookAdmin( admin.ModelAdmin):
#     pass

#
# class BookAdmin(ImportExportModelAdmin):
#     resource_class = BookResource


admin.site.register(Book, BookAdmin)
admin.site.register(ALL, ALLAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UDC)
# admin.site.register(Book)
