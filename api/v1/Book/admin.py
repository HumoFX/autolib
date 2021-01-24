import tablib
from django.utils.translation import gettext_lazy as _

from django.conf.urls import url
from django.contrib import admin
from django.contrib.admin.templatetags.admin_urls import register
from django import forms
from django.contrib.auth import get_permission_codename
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_str
from django.views.decorators.http import require_POST
from import_export import resources, fields
from import_export.admin import ImportExportActionModelAdmin, ImportMixin, ImportExportMixinBase
from import_export.formats import base_formats
from import_export.formats.base_formats import DEFAULT_FORMATS
from import_export.forms import ImportForm, ConfirmImportForm
from import_export.resources import logger, modelresource_factory
from import_export.tmp_storages import TempFolderStorage, MediaStorage
from import_export.widgets import ForeignKeyWidget, DateTimeWidget, DateWidget, CharWidget
from mptt.admin import DraggableMPTTAdmin, MPTTModelAdmin

from elib import settings
from elib.settings import MEDIA_ROOT
from .convert import converter
from django.core.files.storage import default_storage
import csv
from .models import Category, UDC, Book, LibraryStorageEntry, LibraryStorage, DocumentType, UDCImage, CopyrightMark
from ajax_select.admin import AjaxSelectAdmin
from ajax_select import make_ajax_form

from .models import (
    Author,
    Editor,
    Journal,
    Publisher,
    Collection,
    AuthorEntryRank,
    Language
)

from django.core.paginator import Paginator
from django.core.files.storage import default_storage

from ..University.models import University


class NoCountPaginator(Paginator):
    @property
    def count(self):
        return 999999999  # Some arbitrarily large number,
        # so we can still get our page tab.


TMP_STORAGE_CLASS = getattr(settings, 'IMPORT_EXPORT_TMP_STORAGE_CLASS',
                            TempFolderStorage)


# ---------------------------- Custom Import Mixin ------------------------
# class CustomImportForm(ImportForm):
#     ...
#     # this is my custom field
#     input_contract = forms.ChoiceField(label="Contract", choices=())
#
#     def __init__(self, import_formats, *args, **kwargs):
#         super(CustomImportForm, self).__init__(import_formats, *args, **kwargs)
#         ...
#         # get values for select
#         choices = []
#         contracts = Contract.objects.all()
#         for c in contracts:
#             choices.append((str(c.pk), c.name))
#         choices.insert(0, ('', '---'))
#         self.fields['input_contract'].choices = choices


# class CustomConfirmImportForm(ConfirmImportForm):
#
#     # need to set custom field value to save after import preview
#     input_contract = forms.CharField(widget=forms.HiddenInput())
#
class MarcISOtoCSV(base_formats.CSV):
    tmp_storage_class = None

    def get_tmp_storage_class(self):
        if self.tmp_storage_class is None:
            return TMP_STORAGE_CLASS
        else:
            return self.tmp_storage_class

    def get_title(self):
        return "marc-iso"

    def create_dataset(self, in_stream, **kwargs):
        # print(self)
        # print(in_stream)

        # tmp_storage = self.get_tmp_storage_class()('1.ISO')
        # print(tmp_storage.name)
        # data = converter('USMARC UTF - 8.ISO')
        # print(1)
        # print(data)
        # if not input_format.is_binary() and self.from_encoding:
        #     data = force_str(data, self.from_encoding)
        # with open((MEDIA_ROOT + '/file/marc/csv/USMARC UTF - 8.csv'), 'r') as f:
        #     ds = tablib.import_set(f, format='csv')
        # print(ds)
        return in_stream


class CameraAdmin(ImportExportActionModelAdmin):
    #: template for change_list view
    change_list_template = 'admin/import_export/change_list_import.html'
    #: template for import view
    import_template_name = 'admin/import_export/import.html'
    #: resource class
    resource_class = None
    #: available import formats
    formats = DEFAULT_FORMATS
    #: import data encoding
    from_encoding = "utf-8"
    skip_admin_log = None
    # storage class for saving temporary files
    tmp_storage_class = None
    # print('fuck')
    IMPORT_EXPORT_TMP_STORAGE_CLASS = 'import_export.tmp_storages.MediaStorage'

    # def get_export_filename(self, file_format):
    #     filename = "%s.%s" % ("cocos",
    #                           file_format.get_extension())
    #     return filename
    def get_tmp_storage_class(self):
        if self.tmp_storage_class is None:
            return TMP_STORAGE_CLASS
        else:
            return self.tmp_storage_class

    def has_import_permission(self, request):
        """
        Returns whether a request has import permission.
        """
        IMPORT_PERMISSION_CODE = getattr(settings, 'IMPORT_EXPORT_IMPORT_PERMISSION_CODE', None)
        if IMPORT_PERMISSION_CODE is None:
            return True

        opts = self.opts
        codename = get_permission_codename(IMPORT_PERMISSION_CODE, opts)
        return request.user.has_perm("%s.%s" % (opts.app_label, codename))

    def get_urls(self):
        urls = super().get_urls()
        info = self.get_model_info()
        print('asd')
        my_urls = [
            url(r'^process_import/$',
                self.admin_site.admin_view(self.process_import),
                name='%s_%s_process_import' % info),
            url(r'^import/$',
                self.admin_site.admin_view(self.import_action),
                name='%s_%s_import' % info),
        ]
        return my_urls + urls

    def get_resource_kwargs(self, request, *args, **kwargs):
        return {}

    def get_import_resource_kwargs(self, request, *args, **kwargs):
        """Prepares/returns kwargs used when initializing Resource"""
        return self.get_resource_kwargs(request, *args, **kwargs)

    def get_resource_class(self):
        """Returns ResourceClass"""
        if not self.resource_class:
            return modelresource_factory(self.model)
        else:
            return self.resource_class

    def get_import_resource_class(self):
        """
        Returns ResourceClass to use for import.
        """
        return self.get_resource_class()

    def get_import_formats(self):
        """
        Returns available import formats.
        """
        if not self.formats.__contains__(MarcISOtoCSV):
            self.formats += [MarcISOtoCSV]
        return [f for f in self.formats if f().can_import()]

    @method_decorator(require_POST)
    def process_import(self, request, *args, **kwargs):
        # super(CameraAdmin, self).process_import(request)
        print('here')
        if not self.has_import_permission(request):
            raise PermissionDenied

        form_type = self.get_confirm_import_form()
        confirm_form = form_type(request.POST)
        print(confirm_form)
        if confirm_form.is_valid():
            import_formats = self.get_import_formats()
            input_format = import_formats[
                int(confirm_form.cleaned_data['input_format'])
            ]()
            tmp_storage = self.get_tmp_storage_class()(name=confirm_form.cleaned_data['import_file_name'])
            data = tmp_storage.read(input_format.get_read_mode())
            if input_format.get_title() == MarcISOtoCSV().get_title():
                print(confirm_form.cleaned_data['original_file_name'])
                file_name = confirm_form.cleaned_data['original_file_name'].split('.')[0] + '.csv'
                print(file_name)
                data = MEDIA_ROOT + '/file/marc/csv/' + file_name
                with open(data, 'r') as f:
                    ds = tablib.import_set(f, format='csv')
                data = ds
            elif not input_format.is_binary() and self.from_encoding:
                data = force_str(data, self.from_encoding)
            dataset = input_format.create_dataset(data)

            result = self.process_dataset(dataset, confirm_form, request, *args, **kwargs)

            tmp_storage.remove()

            return self.process_result(result, request)

    def import_action(self, request, *args, **kwargs):
        """
        Perform a dry_run of the import to make sure the import will not
        result in errors.  If there where no error, save the user
        uploaded file to a local temp file that will be used by
        'process_import' for the actual import.
        """
        if not self.has_import_permission(request):
            raise PermissionDenied

        context = self.get_import_context_data()

        import_formats = self.get_import_formats()
        form_type = self.get_import_form()
        form_kwargs = self.get_form_kwargs(form_type, *args, **kwargs)
        form = form_type(import_formats,
                         request.POST or None,
                         request.FILES or None,
                         **form_kwargs)

        if request.POST and form.is_valid():
            input_format = import_formats[
                int(form.cleaned_data['input_format'])
            ]()
            import_file = form.cleaned_data['import_file']
            # first always write the uploaded file to disk as it may be a
            # memory file or else based on settings upload handlers
            tmp_storage = self.write_to_tmp_storage(import_file, input_format)

            # then read the file, using the proper format-specific mode
            # warning, big files may exceed memory
            try:
                data = tmp_storage.read(input_format.get_read_mode())
                if input_format.get_title() == MarcISOtoCSV().get_title():
                    data = converter(import_file.name, request.user.university_id.id)
                    with open(data, 'r') as f:
                        ds = tablib.import_set(f, format='csv')
                    data = ds
                elif not input_format.is_binary() and self.from_encoding:
                    data = force_str(data, self.from_encoding)

                dataset = input_format.create_dataset(data)
                print(dataset)
            except UnicodeDecodeError as e:
                return HttpResponse(_(u"<h1>Imported file has a wrong encoding: %s</h1>" % e))
            except Exception as e:
                return HttpResponse(
                    _(u"<h1>%s encountered while trying to read file: %s</h1>" % (type(e).__name__, import_file.name)))

            # prepare kwargs for import data, if needed
            res_kwargs = self.get_import_resource_kwargs(request, form=form, *args, **kwargs)
            resource = self.get_import_resource_class()(**res_kwargs)

            # prepare additional kwargs for import_data, if needed
            imp_kwargs = self.get_import_data_kwargs(request, form=form, *args, **kwargs)
            result = resource.import_data(dataset, dry_run=True,
                                          raise_errors=False,
                                          file_name=import_file.name,
                                          user=request.user,
                                          **imp_kwargs)

            context['result'] = result

            if not result.has_errors() and not result.has_validation_errors():
                initial = {
                    'import_file_name': tmp_storage.name,
                    'original_file_name': import_file.name,
                    'input_format': form.cleaned_data['input_format'],
                }
                confirm_form = self.get_confirm_import_form()
                initial = self.get_form_kwargs(form=form, **initial)
                context['confirm_form'] = confirm_form(initial=initial)
        else:
            res_kwargs = self.get_import_resource_kwargs(request, form=form, *args, **kwargs)
            resource = self.get_import_resource_class()(**res_kwargs)

        context.update(self.admin_site.each_context(request))

        context['title'] = _("Import")
        context['form'] = form
        context['opts'] = self.model._meta
        context['fields'] = [f.column_name for f in resource.get_user_visible_fields()]

        request.current_app = self.admin_site.name
        return TemplateResponse(request, [self.import_template_name],
                                context)

    def write_to_tmp_storage(self, import_file, input_format):
        tmp_storage = self.get_tmp_storage_class()()
        default_storage.save('file/marc/' + import_file.name, import_file)
        data = bytes()
        print(import_file.name)
        for chunk in import_file.chunks():
            data += chunk

        tmp_storage.save(data, input_format.get_read_mode())
        return tmp_storage


# class CustomImportMixin(ImportMixin):
#
#     def get_import_formats(self):
#         """
#         Returns available import formats.
#         """
#         if not self.formats.__contains__(MarcISOtoCSV):
#             self.formats += [MarcISOtoCSV]
#         return [f for f in self.formats if f().can_import()]


# --------------------------------------------------------------------------


@register.filter
def publication_date(entry):
    """We expect an entry object to filter"""
    if entry.is_partial_publication_date:
        fmt = "%Y"
    else:
        fmt = "%F %Y"
    return entry.publication_date.strftime(fmt)


class LibraryStorageAdmin(admin.ModelAdmin):
    model = LibraryStorage
    fields = ['name', 'abbreviation']

    def save_model(self, request, obj, form, change):
        university = request.user.university_id
        obj.university = university
        obj.save()


class LibraryStorageEntryInline(admin.StackedInline):
    extra = 1
    model = LibraryStorageEntry
    ordering = ("entry_number",)

    def get_queryset(self, request):
        queryset = LibraryStorageEntry.objects.filter(storage__university_id=request.user.university_id)
        print(queryset)
        return queryset


class AuthorEntryRankInline(admin.StackedInline):
    extra = 1
    model = AuthorEntryRank
    ordering = ("rank",)


class AbstractHumanAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
    ordering = ("last_name", "first_name")


class AuthorAdmin(AbstractHumanAdmin):
    list_display = ("last_name", "first_name", "user")
    raw_id_fields = ("user",)


class EditorAdmin(AbstractHumanAdmin):
    raw_id_fields = ("user",)


class AbstractEntityAdmin(admin.ModelAdmin):
    ordering = ("name",)


class JournalAdmin(AbstractEntityAdmin):
    pass


class PublisherAdmin(AbstractEntityAdmin):
    pass


class CategoryAdmin(AjaxSelectAdmin, ImportExportActionModelAdmin):
    form = make_ajax_form(Category, {
        # fieldname: channel_name
        'udc_id': 'category',
        'parent': 'parent_id'
    })


class CopyrightResources(resources.ModelResource):
    class Meta:
        model = CopyrightMark
        use_bulk = True
        batch_size = 1000
        skip_diff = True


class CopyrightAdmin(ImportExportActionModelAdmin, AbstractEntityAdmin):
    resource_class = CopyrightResources
    list_display = ['name', 'abbreviation']
    search_fields = ['name', 'abbreviation']
    # paginator = NoCountPaginator
    # show_full_result_count = False


class UDCImageAdmin(admin.ModelAdmin):
    autocomplete_fields = ('udc',)


class UDCResources(resources.ModelResource):
    parent = fields.Field(
        column_name='parent',
        attribute='parent',
        widget=ForeignKeyWidget(UDC, 'udc'))

    class Meta:
        model = UDC
        use_bulk = True
        batch_size = 100
        skip_diff = True
        force_init_instance = True
        # fields = ['udc', 'name', 'parent', 'id']


class UDCAdmin(ImportExportActionModelAdmin, AjaxSelectAdmin, DraggableMPTTAdmin):
    resource_class = UDCResources
    form = make_ajax_form(UDC, {
        # fieldname: channel_name
        'udc': 'udc_num',
        'parent': 'parent'
    })
    list_display = (
        'tree_actions',
        'indented_title',
        'name',
        'udc',
        'get_descendant_count'
    )
    search_fields = ("name", "udc")
    # paginator = NoCountPaginator
    # show_full_result_count = False


# class BulkSaveMixin:
#     """
#     Overridden to store instance so that it can be imported in bulk.
#     https://github.com/django-import-export/django-import-export/issues/939#issuecomment-509435531
#     """
#     bulk_instances = []
#
#     def save_instance(self, instance, using_transactions=True, dry_run=False):
#         self.before_save_instance(instance, using_transactions, dry_run)
#         if not using_transactions and dry_run:
#             # we don't have transactions and we want to do a dry_run
#             pass
#         else:
#             self.bulk_instances.append(instance)
#         self.after_save_instance(instance, using_transactions, dry_run)
#
#     def after_import(self, dataset, result, using_transactions, dry_run, **kwargs):
#         if self.bulk_instances:
#             try:
#                 self._meta.model.objects.bulk_create(self.bulk_instances)
#             except Exception as e:
#                 # Be careful with this
#                 # Any exceptions caught here will be raised.
#                 # However, if the raise_errors flag is False, then the exception will be
#                 # swallowed, and the row_results will look like the import was successful.
#                 # Setting raise_errors to True will mitigate this because the import process will
#                 # clearly fail.
#                 # To be completely correct, any errors here should update the result / row_results
#                 # accordingly.
#                 logger.error("caught exception during bulk_import: %s", str(e), exc_info=1)
#                 raise e
#             finally:
#                 self.bulk_instances.clear()


class BookResource(ImportMixin, resources.ModelResource):

    def before_import_row(self, row, **kwargs):
        Publisher.objects.get_or_create(name=row.get('publisher'))

    publisher = fields.Field(
        column_name='publisher',
        attribute='Publisher',
        widget=ForeignKeyWidget(Publisher, 'name'))
    publication_date = fields.Field(
        column_name='publication_date',
        attribute='publication_date',
        widget=CharWidget()
    )

    class Meta:
        model = Book


class BookAdmin(CameraAdmin, AjaxSelectAdmin, admin.ModelAdmin):
    formats = (MarcISOtoCSV, base_formats.XLS, base_formats.CSV)
    resource_class = BookResource
    # fields = ('Факультет', 'Количество', 'Цена', ' Рейтинг', ' Использовано', 'Опубликовано', 'created')
    form = make_ajax_form(Book, {
        # fieldname: channel_name
        'udc': 'udc',
        'udc_new': 'udc_new'
    })

    def has_change_permission(self, request, obj=None):
        univer = request.user.university_id.id
        if request.user.is_superuser:
            return True
        if obj is not None and obj.university.id == univer:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        univer = request.user.university_id.id
        if request.user.is_superuser:
            return True
        if obj is not None and obj.university.id == univer:
            return True
        else:
            return False


class EntryAdmin(BookAdmin, admin.ModelAdmin):
    # date_hierarchy = "publication_date"
    form = make_ajax_form(Book, {
        # fieldname: channel_name
        'udc': 'udc',
        'udc_new': 'udc_new',
        'editors': 'editors',
        'journal': 'journal',
        'publisher': 'publisher',
        'copyright_mark': 'copyright_mark',
    })
    fieldsets = (
        (
            "Основные поля публикации",
            {
                "fields": (
                    "type",
                    "title",
                    "journal",
                    "volume",
                    ("pages", "language"),
                    ("publication_date", "is_partial_publication_date"),
                )
            },
        ),
        ("Идентификаторы", {"fields": ("doi", "issn", "pmid", "inventory_number", "isbn", "isbn2")}),
        ("Книжные поля", {"fields": ("booktitle", "edition", "chapter", "udc", "udc_new", 'copyright_mark')}),
        ("Кандидатская диссертация", {"fields": ("school",)}),
        ("Труды", {"fields": ("organization",)}),
        (
            "Разное",
            {"fields": ("editors", "publisher", "address", "annote", "note")},
        ),
        ("Перекрестные ссылки", {"fields": ("crossref",)}),
        (
            "Дополнительная информациия",
            {
                "fields": (
                    ("printed_book", "e_book", "special_books"),
                    "img", "file",
                    "key_words",
                    "quantity", "real_time_count",
                    "price",
                    "used",
                    "rating",
                    "date_get"
                )
            }
        )
    )
    inlines = (AuthorEntryRankInline, LibraryStorageEntryInline)
    list_display = ("title", "first_author", "type", "publication_date", "journal")
    list_filter = ("publication_date", "journal", "authors", "type")
    list_per_page = 100
    list_select_related = True
    ordering = ("-publication_date",)
    raw_id_fields = ("authors", "crossref")
    search_fields = ("title",)

    # save_as = True
    # save_on_top = True
    # change_list_template = 'Book/books.html'

    def save_model(self, request, obj, form, change):
        university = request.user.university_id
        obj.university = university
        print(obj)
        obj.save()


class CollectionAdmin(admin.ModelAdmin):
    def size(self, obj):
        """Get the number of entries in each collection"""
        return obj.entries.count()

    list_display = ("name", "size")
    raw_id_fields = ("entries",)


admin.site.register(LibraryStorageEntry)
admin.site.register(LibraryStorage, LibraryStorageAdmin)
admin.site.register(Language)
admin.site.register(Author, AuthorAdmin)
admin.site.register(AuthorEntryRank)
admin.site.register(Editor, EditorAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, EntryAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UDC, UDCAdmin)
admin.site.register(UDCImage, UDCImageAdmin)
admin.site.register(CopyrightMark, CopyrightAdmin)
admin.site.register(DocumentType)
