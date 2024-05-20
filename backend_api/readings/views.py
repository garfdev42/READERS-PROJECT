from django.shortcuts import render
from django.http import HttpResponse
from .Books import Book
from .serializers import BookSerializer
  

def list_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return render(request, 'readings/listar_books.html', {'books': serializer.data})

def create_books(request):
    if request.method == "POST":
        serializer = BookSerializer(data=request.POST)
        if serializer.is_valid():
           serializer.save()
           #return redirect('list')
    else:
        serializer = BookSerializer()

    return render(request, 'readings/create_books.html', {'form': serializer})
