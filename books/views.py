from django.shortcuts import render
from django.views.generic import ListView

from books.models import Book

def home_page(request):
    return render(request, "books/home_page.html")

class BookListView(ListView):
    model = Book