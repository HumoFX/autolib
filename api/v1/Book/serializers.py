from rest_framework import serializers

from .models import Book, Category, UDC
import serpy


class BookSerpy(serpy.Serializer):
    # time = datetime.now()
    id = serpy.MethodField()
    title = serpy.StrField()
    author = serpy.StrField()
    udc = serpy.MethodField()
    isbn = serpy.StrField()
    key_words = serpy.StrField()
    university = serpy.MethodField()
    faculty = serpy.MethodField()
    quantity = serpy.IntField()
    price = serpy.FloatField()
    rating = serpy.FloatField()
    used = serpy.IntField()
    img = serpy.StrField()
    e_book = serpy.BoolField()
    file = serpy.StrField()
    printed_book = serpy.BoolField()
    special_books = serpy.BoolField()
    work_book = serpy.BoolField()
    date_pub = serpy.Field()
    date_get = serpy.Field()
    created = serpy.Field()

    def get_id(self, obj):
        if obj is not None:
            return obj.pk

    def get_udc(self, obj):
        if obj is not None:
            return obj.udc.pk

    def get_university(self, obj):
        # a = Profile.objects.get(pk=obj.university)
        # print(a)
        # print(obj.university.pk)
        if obj is not None:
            return obj.university.pk

    def get_faculty(self, obj):
        if obj is not None:
            return obj.faculty.pk

    # time1 = datetime.now()
    # print('\n serpy=', time1 - time)


class CategorySerpy(serpy.Serializer):
    id = serpy.MethodField()
    udc_id = serpy.StrField()
    name = serpy.StrField()
    parent = serpy.MethodField()

    def get_id(self, obj):
        if obj is not None:
            return obj.pk

    def get_parent(self, obj):
        if obj is not None:
            return obj.parent


# class UDCSerpy(serpy.Serializer):
#     id = serpy.MethodField()
#     id_number = serpy.StrField()

#     def as_getter(self, serializer_field_name, serializer_cls):
#         return partial(get_related, serializer_field_name)
#
#
# def get_related(name, instance):
#     value = getattr(instance, name, None)
#     if value and is_related(instance._meta, value):
#         value = value.all()
#     return value
#
#
# def is_related(opts, value):
#     field = None
#     if hasattr(value, 'field'):
#         field = value.field
#     if not field and hasattr(value, 'source_field'):
#         field = value.source_field
#     if field and hasattr(field, 'remote_field'):
#         return (
#                 field.remote_field in related_fields(opts) or value.field in many_to_many_fields(opts)
#         )
#     return False
#
#
# def related_fields(opts):
#     return (
#         f for f in opts.get_fields(include_hidden=True)
#         if f.auto_created and not f.concrete and (f.one_to_one or f.one_to_many)
#     )
#
#
# def many_to_many_fields(opts):
#     return (
#         f for f in opts.get_fields(include_hidden=True)
#         if f.many_to_many and f.auto_created
#     )


# def serialize_user(obj: Book) -> Dict[str, Any]:
#     return {
#         "id": obj.id,
#         "title": obj.title,
#         "author": obj.author,
#         "isbn": obj.isbn,
#         "key_words": obj.key_words,
#         "img": obj.img,
#         "quantity": obj.quantity,
#         "price": obj.price,
#         "rating": obj.rating,
#         "used": obj.used,
#         "e_book": obj.e_book,
#         "file": obj.file,
#         "printed_book": obj.printed_book,
#         "special_books": obj.special_books,
#         "work_book": obj.work_book,
#         "date_pub": obj.date_pub,
#         "date_get": obj.date_get,
#         "created": obj.created,
#         "udc": obj.udc,
#         "university": obj.university,
#         "faculty": obj.faculty
#     }

class UDCSerializer(serializers.ModelSerializer):
    class Meta:
        model = UDC
        # fields = ('id', 'id_number')

    fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    # udc_id = UDCSerializer

    class Meta:
        model = Category
        # fields = ('id', 'udc_id', 'name', 'parent')
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        response = super(BookSerializer, self).to_representation(instance)
        print(instance.file)
        if instance.img:
            response['img'] = instance.img.url
        if instance.file:
            response['file'] = instance.file.url
        return response
