from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register
from library.models import Book
# Register your models here.
@register(Book)
class BookModel(MaterialModelAdmin):
    list_display = ['bookTitle', 'bookAuthor', 'bookPublisher', '_datePublished']
    list_filter = ['bookTitle', 'bookAuthor']
    search_fields = ['bookTitle', 'bookAuthor']

    icon_name = 'local_library'
