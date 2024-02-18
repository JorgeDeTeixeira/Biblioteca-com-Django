from django.urls import path

from books.views import *

urlpatterns = [
    path("", home_page, name="home_page"),
]
