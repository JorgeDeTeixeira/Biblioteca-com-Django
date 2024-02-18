from django.shortcuts import render


def home_page(request):
    return render(request, "books/home_page.html")
