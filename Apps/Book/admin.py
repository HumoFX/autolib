from django.contrib import admin
from .models import Category, UDC, Book


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'udc', 'author', 'special_books')
    ordering = ('title', 'author')
    search_fields = ('title', 'udc', 'author', 'date_of_pub', 'date_of_get')


admin.site.register(Category)
admin.site.register(UDC)
# admin.site.register(Book)

