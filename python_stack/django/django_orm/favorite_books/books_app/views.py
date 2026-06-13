from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method != "POST":
        return redirect('/')

    errors = User.objects.register_validator(request.POST)

    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/')

    hashed_pw = bcrypt.hashpw(
        request.POST['password'].encode(),
        bcrypt.gensalt()
    ).decode()

    user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=hashed_pw
    )

    request.session['user_id'] = user.id
    return redirect('/books')


def login(request):
    if request.method != "POST":
        return redirect('/')

    errors = User.objects.login_validator(request.POST)

    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/')

    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id

    return redirect('/books')


def logout(request):
    request.session.flush()
    return redirect('/')


def books(request):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'logged_user': User.objects.get(id=request.session['user_id']),
        'all_books': Book.objects.all()
    }

    return render(request, 'books.html', context)


def create_book(request):
    if 'user_id' not in request.session:
        return redirect('/')

    if request.method != "POST":
        return redirect('/books')

    errors = Book.objects.book_validator(request.POST)

    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/books')

    logged_user = User.objects.get(id=request.session['user_id'])

    book = Book.objects.create(
        title=request.POST['title'],
        description=request.POST['description'],
        uploaded_by=logged_user
    )

    book.users_who_like.add(logged_user)

    return redirect('/books')


def show_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'logged_user': User.objects.get(id=request.session['user_id']),
        'book': Book.objects.get(id=book_id)
    }

    return render(request, 'show_book.html', context)


def update_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')

    book = Book.objects.get(id=book_id)
    logged_user = User.objects.get(id=request.session['user_id'])

    if book.uploaded_by.id != logged_user.id:
        return redirect(f'/books/{book_id}')

    errors = Book.objects.book_validator(request.POST)

    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect(f'/books/{book_id}')

    book.title = request.POST['title']
    book.description = request.POST['description']
    book.save()

    return redirect(f'/books/{book_id}')


def delete_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')

    book = Book.objects.get(id=book_id)
    logged_user = User.objects.get(id=request.session['user_id'])

    if book.uploaded_by.id == logged_user.id:
        book.delete()

    return redirect('/books')


def add_favorite(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')

    logged_user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)

    book.users_who_like.add(logged_user)

    return redirect(f'/books/{book_id}')


def remove_favorite(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')

    logged_user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)

    book.users_who_like.remove(logged_user)

    return redirect(f'/books/{book_id}')


def user_page(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'logged_user': User.objects.get(id=request.session['user_id']),
        'page_user': User.objects.get(id=user_id)
    }

    return render(request, 'user_page.html', context)