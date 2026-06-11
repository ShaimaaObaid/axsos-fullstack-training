from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.

# ---------------- BOOKS ----------------

def books(request):
    return render(request, "books.html", {
        "all_books": Book.objects.all()
    })


def add_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc']
        )
    return redirect('/')


def book_details(request, id):
    book = Book.objects.get(id=id)

    context = {
        "book": book,
        "authors": book.authors.all(),

        # BONUS: only authors NOT linked yet
        "available_authors": Author.objects.exclude(id__in=book.authors.all())
    }
    return render(request, "book_details.html", context)


def add_author_to_book(request, id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        author = Author.objects.get(id=request.POST['author'])
        book.authors.add(author)

    return redirect(f'/books/{id}/')


# ---------------- AUTHORS ----------------

def authors(request):
    return render(request, "authors.html", {
        "all_authors": Author.objects.all()
    })


def add_author(request):
    if request.method == "POST":
        Author.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            notes=request.POST['notes']
        )
    return redirect('/authors/')


def author_details(request, id):
    author = Author.objects.get(id=id)

    context = {
        "author": author,
        "books": author.books.all(),

        # BONUS: only books NOT linked yet
        "available_books": Book.objects.exclude(id__in=author.books.all())
    }
    return render(request, "author_details.html", context)


def add_book_to_author(request, id):
    if request.method == "POST":
        author = Author.objects.get(id=id)
        book = Book.objects.get(id=request.POST['book'])
        author.books.add(book)

    return redirect(f'/authors/{id}/')