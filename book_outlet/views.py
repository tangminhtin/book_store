from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg, Min, Max
from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    agg_rating = books.aggregate(Avg("rating"), Min("rating"), Max("rating"))

    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": num_books,
        "average_rating": round(agg_rating['rating__avg'], 1),
        "min_rating": agg_rating['rating__min'],
        "max_rating": agg_rating['rating__max']
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "is_bestseller": book.is_bestselling,
    })
