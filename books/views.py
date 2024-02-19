from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from books.models import Book
from books.forms import BookForm


def home_page(request):
    return render(request, "books/home_page.html")


class BookListView(ListView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy("get_books")


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy("get_books")
