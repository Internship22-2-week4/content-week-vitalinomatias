from django.shortcuts import render

from django.http import HttpResponse

from .models import Author, Category, Book

# Create your views here.

def index(request):
    books = Book.objects.all()
    for book in books:
      print(book.title, book.author.first_name, book.category.name)
    return render(request, 'books/index.html', {
      "books_list": books
    })
  # return HttpResponse('app book')

def author(request, author_id):
  author = Author.objects.get(id=author_id)
  return render(request, 'books/author.html', {
      "author": author
    })
  # return HttpResponse('Author id {}'.format(author_id))

def category(request, category_id):
  return HttpResponse('Category id: {}'.format(category_id))