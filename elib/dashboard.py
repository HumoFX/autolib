from controlcenter import Dashboard, widgets
from django.db.models import Count

from apps.book.models import *


class BookItemList(widgets.ItemList):
    title = "ТОП 30 часто используемых книг"
    queryset = Book.objects.order_by('-used')
    list_display = ('title', 'used')
    limit_to = 30


class MyBarChart(widgets.SingleBarChart):
    title = 'Количество книг в разделах УДК - ТОП 30'
    qs = UDC.objects.annotate(count=Count('book')).order_by('-count')
    values_list = ['name', 'count']
    limit_to = 30
    queryset = qs

    class Chartist:
        options = {
            # Displays only integer values on y-axis
            'onlyInteger': True,
            # Visual tuning
            'chartPadding': {
                'top': 24,
                'right': 0,
                'bottom': 0,
                'left': 0,
            }
        }

    def series(self):
        # Y-axis
        return [y for x, y in self.values]

    def labels(self):
        # Duplicates series on x-axis
        return self.series

    def legend(self):
        # Displays labels in legend
        return [x for x, y in self.values]


class MyDashboard(Dashboard):
    widgets = (
        BookItemList, MyBarChart,
    )
