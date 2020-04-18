from ajax_select import register, LookupChannel
from django.db.models import Q

from .models import Book, UDC, Category


@register('УДК')
class BookLookup(LookupChannel):
    model = Category

    def get_query(self, q, request):
        return self.model.objects.filter(Q(udc_id__contains=q) | Q(name__contains=q)).order_by('udc_id')

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % format(item.name, item.udc_id)


@register('category')
class CategoryLookup(LookupChannel):
    model = Category

    def get_query(self, q, request):
        return self.model.objects.filter(Q(udc_id__contains=q)).order_by('udc_id')

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % format(item.name, item.udc_id)


@register('parent_id')
class CategoryLookup(LookupChannel):
    model = Category

    def get_query(self, q, request):
        return self.model.objects.filter(Q(parent__udc_id__contains=q))

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % format(item.name, item.udc_id)
