from django.contrib import admin
from .models import University, Faculty


# Register your models here.
class FacultyAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Faculty, FacultyAdmin)
admin.site.register(University)
