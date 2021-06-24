from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Book
from .models import Category


def homepage(request):

    if request.user.is_authenticated:
        return redirect("book_list")
    return render(request, "books/homepage.html")


@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html",
                  {"books": books})


def show_categ(request, slug):
    categ = get_object_or_404(Category, slug=slug)
    books = categ.books.all()
    return render(request, "books/show_category.html", {"category": category, "books": books})
