from rest_framework import serializers
from readings.Books import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta: 
        Model = Book
        field  = [
            'title',
            'author',
            'genre',
            'published_year',
            'isbn',
            'publisher',
            'pages',
            'lenguage',
            'description',
            'cover_image',
        ] 