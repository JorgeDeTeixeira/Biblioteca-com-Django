from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
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


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("get_books")


class BookReadView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.book_read()
        return redirect("get_books")
