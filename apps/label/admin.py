from django.contrib import admin

from apps.label.models import Label, UserLabel


class LabelAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'inventory', 'password', 'tag_id']
    search_fields = ["inventory"]


class UserLabelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'inventory', 'tag_id']


admin.site.register(Label, LabelAdmin)
admin.site.register(UserLabel, UserLabelAdmin)
