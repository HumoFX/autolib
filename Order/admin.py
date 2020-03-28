from django.contrib import admin
from .models import Order, BookInUse

# Register your models here.

admin.site.register(Order)
admin.site.register(BookInUse)
