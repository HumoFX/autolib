from django.forms import ModelForm
from Book.models import Book
from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField


class DocumentForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
    tags = AutoCompleteSelectField('УДК', required=False, help_text=None)
