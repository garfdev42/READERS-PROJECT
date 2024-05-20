from django.core.management.base import BaseCommand
from readings.Books import Book
import json

class Command(BaseCommand):
    help = 'Make a database backup in JSON format'

    def handle(self, *args, **options):
        books = Book.objects.all()
        data = [{
                 'title': book.title,
                 'author': book.author,
                 'genre': book.genre,
                 'published_year': book.published_year,
                 'isbn': book.isbn,
                 'publisher': book.publisher,
                 'pages': book.pages,
                 'language': book.language,
                 'description': book.description,
                 'cover_image': book.cover_image_url,
                 }
                for book in books]
        with open('backup_db.json', 'w') as file:
            json.dump(data, file, indent=4)