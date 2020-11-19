from django.forms import ModelForm
from .models import Book
from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField


class DocumentForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    udc = AutoCompleteSelectField('udc', required=False, help_text=None)
    udc_new = AutoCompleteSelectField('udc_new', required=False, help_text=None)
    editors = AutoCompleteSelectMultipleField('editors', required=False, help_text=None)

    # tags_new = AutoCompleteSelectField('udc_new', required=True, help_text='Должен совпадать с полем УДК')
