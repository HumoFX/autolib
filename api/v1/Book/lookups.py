from ajax_select import register, LookupChannel
from django.db.models import Q

from .models import Book, UDC, Category, Editor, Journal, Publisher


@register('udc')
class BookLookup(LookupChannel):
    model = Category

    def get_query(self, q, request):
        return self.model.objects.filter(Q(udc_id__contains=q) | Q(name__contains=q)).order_by('udc_id')

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item


@register('udc_new')
class BookLookup(LookupChannel):
    model = UDC

    def get_query(self, q, request):
        return self.model.objects.filter(Q(udc__contains=q) | Q(name__contains=q)).order_by('udc')

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item


@register('editors')
class BookLookup(LookupChannel):
    model = Editor

    def get_query(self, q, request):
        return self.model.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q)).order_by('first_name')

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item


@register('editors')
class BookLookup(LookupChannel):
    model = Editor

    def get_query(self, q, request):
        return self.model.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q)).order_by('first_name')

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item


@register('journal')
class BookLookup(LookupChannel):
    model = Journal

    def get_query(self, q, request):
        return self.model.objects.filter(Q(abbreviation__icontains=q) | Q(name__icontains=q)).order_by('abbreviation')

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item


@register('publisher')
class BookLookup(LookupChannel):
    model = Publisher

    def get_query(self, q, request):
        return self.model.objects.filter(Q(abbreviation__contains=q) | Q(name__contains=q)).order_by('abbreviation')

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item


@register('category')
class CategoryLookup(LookupChannel):
    model = Category

    def get_query(self, q, request):
        return self.model.objects.filter(Q(udc_id__contains=q)).order_by('udc_id')

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item


@register('parent_id')
class CategoryLookup(LookupChannel):
    model = Category

    def get_query(self, q, request):
        return self.model.objects.filter(Q(udc_id__contains=q) | Q(name__contains=q))

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item


@register('udc_num')
class UDCLookup(LookupChannel):
    model = UDC

    def get_query(self, q, request):
        return self.model.objects.filter(Q(udc__contains=q)).order_by('udc')

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item


@register('parent')
class UDCLookup(LookupChannel):
    model = UDC

    def get_query(self, q, request):
        return self.model.objects.filter(Q(udc__contains=q) | Q(name__contains=q))

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item
