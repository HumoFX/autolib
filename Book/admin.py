from django.contrib import admin
from import_export import resources, widgets, fields
from import_export.admin import ImportExportModelAdmin, ExportActionMixin, ImportExportActionModelAdmin

from .forms import DocumentForm
from .models import Category, UDC, Book
from University.models import University
from ajax_select.admin import AjaxSelectAdmin
from ajax_select import make_ajax_form
from .permissions import IsOwnerOrReadOnly


# Register your models here.
class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        skip_unchanged = True

        fields = ('id', 'title', 'author', 'udc', 'keywords', 'img', 'e_book', 'file',
                  'date_pub')
        # exlude = 'id'


# class AllResource(resources.ModelResource):
#     class Meta:
#         model = ALL
#         skip_unchanged = True
#         import_id_fields = ('title', 'author', 'date_pub')
#         fields = ('id', 'title', 'author', 'udc', 'keywords', 'img', 'e_book', 'file',
#                   'date_pub')
#
#
# class ALLAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
#     # fields = ('Факультет', 'Количество', 'Цена', ' Рейтинг', ' Использовано', 'Опубликовано', 'created')
#
#     ordering = ('author', 'udc')
#     search_fields = ['udc', 'udc__udc_id__id_number', 'title', 'author']
#     list_display = ('title', 'author', 'udc', 'date_pub')
#     resource_class = AllResource


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
        'udc': 'udc'
    })

    ordering = ('author', 'udc__name')
    search_fields = ['udc__name', 'udc__udc_id', 'title', 'author', 'date_get', 'date_pub']
    list_filter = ('university', 'rating')
    list_display = ('title', 'author', 'udc', 'date_get', 'date_pub', 'rating', 'used')
    resource_class = BookResource

    # skip_unchanged = True
    # class IsOwnerOrReadOnly(permissions.BasePermission):
    #     def has_object_permission(self, request, view, obj):
    #         if request.method in permissions.SAFE_METHODS:
    #             return True
    #         return obj.user == request.user
    def has_change_permission(self, request, obj=None):
        univer = request.user.university_id.id
        if request.user.is_superuser:
            return True
        if obj is not None and obj.university.university_id.id != univer:
            return False

    def has_delete_permission(self, request, obj=None):
        univer = request.user.university_id.id
        if request.user.is_superuser:
            return True
        if obj is not None and obj.university.university_id.id != univer:
            return False

    # def get_queryset(self, request):
    #     if request.user.is_superuser:
    #         return Book.objects.all()
    #     if request.user.is_staff:
    #         univer = request.user.university_id.id
    #         return Book.objects.filter(university__university_id__id=univer)


admin.site.register(Book, BookAdmin)
# admin.site.register(ALL, ALLAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UDC)
# admin.site.register(Book)
