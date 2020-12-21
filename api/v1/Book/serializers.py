from rest_framework import serializers

from .models import Book, Category, UDC, Author
import serpy


class BookSerpy(serpy.Serializer):
    # time = datetime.now()
    id = serpy.MethodField()
    title = serpy.StrField()
    # author = serpy.StrField()
    udc = serpy.MethodField()
    isbn = serpy.StrField()
    key_words = serpy.StrField()
    university = serpy.MethodField()
    # faculty = serpy.MethodField()
    quantity = serpy.IntField()
    price = serpy.FloatField()
    rating = serpy.FloatField()
    used = serpy.IntField()
    img = serpy.StrField()
    e_book = serpy.BoolField()
    file = serpy.StrField()
    printed_book = serpy.BoolField()
    special_books = serpy.BoolField()
    # work_book = serpy.BoolField()
    # date_pub = serpy.Field()
    # date_get = serpy.Field()
    created = serpy.Field()

    def get_id(self, obj):
        if obj is not None:
            return obj.pk

    def get_udc(self, obj):
        if obj is not None:
            return obj.udc.pk

    def get_university(self, obj):
        if obj is not None:
            return obj.university.pk

    def get_faculty(self, obj):
        if obj is not None:
            return obj.faculty.pk


class UDCSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='udcimage.image', read_only=True)

    class Meta:
        model = UDC
        fields = [
            'id',
            'udc',
            'name',
            'parent',
            'image',
        ]


class CategorySerializer(serializers.ModelSerializer):
    # udc_id = UDCSerializer

    class Meta:
        model = Category
        # fields = ('id', 'udc_id', 'name', 'parent')
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    initial_name = serializers.SerializerMethodField()

    def get_initial_name(self, obj):
        return obj.get_formatted_name()

    class Meta:
        model = Author
        fields = [
            'id',
            'initial_name'
        ]


class BookSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(read_only=True)
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'authors',
            'udc',
            'key_words',
            'university',
            'rating',
            'img',
            'publication_date'
        ]


class BookDetailSerializer(serializers.ModelSerializer):
    img = serializers.ImageField()
    file = serializers.FileField()
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'authors',
            'udc',
            'isbn',
            'university',
            'quantity',
            'rating',
            'img',
            'e_book',
            'file',
            'printed_book',
            'special_books',
            'publication_date'
        ]
