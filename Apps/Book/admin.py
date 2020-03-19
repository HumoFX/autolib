from django.contrib import admin
from .models import Category, UDC, Book

# Register your models here.

admin.site.register(Category)
admin.site.register(UDC)
admin.site.register(Book)

    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     extra_context = extra_context or {}
    #     extra_context['resort_to_country'] = Category.objects.all().values_list('pk', 'udc_id', 'name')
    #     return super().change_view(
    #         request, object_id, form_url, extra_context=extra_context,
    #     )

# admin.site.register(Book, BookAdmin)
