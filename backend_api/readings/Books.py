from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    published_year = models.IntegerField()
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=100)
    pages = models.IntegerField()
    language = models.CharField(max_length=50)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='books/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.author} - {self.genre} - {self.published_year} - {self.isbn} - {self.publisher} - {self.pages} - {self.language} - {self.description}"
