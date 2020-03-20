from django.contrib import admin
from .models import Category, UDC, Book


# Register your models here.
class NewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, NewAdmin)
admin.site.register(UDC)
admin.site.register(Book)

