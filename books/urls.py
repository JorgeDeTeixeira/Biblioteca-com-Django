from django.urls import path

from books.views import *

urlpatterns = [
    path("", home_page, name="home_page"),
    path("listar", BookListView.as_view(), name="get_books"),
    path("cadastrar", BookCreateView.as_view(), name="post_books"),
    path("update/<int:pk>", BookUpdateView.as_view(), name="put_books"),
]
