from django.contrib import admin
from .models import Category, UDC, Book
from University.models import University


# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ordering = ('Автор', 'УДК__name')
    search_fields = ['УДК__name', 'УДК__udc_id__id_number', 'Название', 'Автор', 'Получено', 'Опубликовано']
    list_filter = ('УДК', 'Университет')
    list_display = ('Название', 'Автор', 'УДК', 'Получено', 'Опубликовано', 'Рейтинг', 'Использовано')

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Book.objects.all()
        if request.user.is_staff:
            univer = request.user.university_id.id
            return Book.objects.filter(Университет__university_id__id=univer)


admin.site.register(Category)
admin.site.register(UDC)
# admin.site.register(Book)
