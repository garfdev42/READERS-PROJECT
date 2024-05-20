from django.contrib import admin
from .Books import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'published_year', 'isbn', 'publisher', 'pages', 'language', 'description', 'cover_image')

admin.site.register(Book, BookAdmin)
