from django.views import generic

from apps.book.models import Book, DocumentType
from apps.user.permissions import LibrarianAccess


class BookListView(LibrarianAccess, generic.ListView):
    model = Book
    template_name = 'librarian/book/datatable.html'

    def get_queryset(self):
        return Book.objects.filter(university=self.request.user.university_id)


class BookDetailView(LibrarianAccess, generic.DetailView):
    model = Book
    template_name = 'librarian/book/detail.html'

    def get_context_data(self, **kwargs):
        response = super(BookDetailView, self).get_context_data()
        response['doc_char_list'] = DocumentType.objects.all()

        return response
