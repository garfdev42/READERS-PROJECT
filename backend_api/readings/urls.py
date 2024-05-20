from django.urls import path
from .views import  list_books, create_books

urlpatterns = [
    #path('', index, name='index'),  # Página de inicio
    path('list_books/',list_books, name='list_books'),  # Lista de libros
    path('create_books/',create_books, name='create_books'),  # Crear un nuevo libro
    # Otras rutas...
]
