from rest_framework import serializers
from .models import Book, Category, UDC


class BookSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=256)
    # author = serializers.CharField(style={'base_template': 'textarea.html'})
    # udc = serializers.BooleanField(required=False)
    # key_words = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # img = serializers.ImageField(use_url=False)
    # faculty = serializers.ForeignKey('University.Faculty', on_delete=models.CASCADE)
    # quantity = serializers.IntegerField()
    # price = serializers.FloatField(name='Цена')
    # rating = serializers.FloatField(name='Рейтинг')
    # used = serializers.IntegerField()
    # e_book = serializers.BooleanField(name='Электроная версия', default=False)
    # file = serializers.FileField(upload_to='file/e_books', null=True, blank=True)
    # printed_book = serializers.BooleanField(name='Печатная версия', default=False)
    # special_books = serializers.BooleanField(name='Спец книги')
    # work_book = special_books.BooleanField(name='Учебное пособие')
    # date_of_pub = special_books.DateField(name='Дата публикации')
    # date_of_get = special_books.DateField(name='Дата получения')
    class Meta:
        model = Book
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UDCSerializer(serializers.ModelSerializer):
    class Meta:
        model = UDC
        fields = '__all__'
