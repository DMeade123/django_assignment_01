from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book #import book model from models.py

# Create your views here.
class BookListView(ListView):
    model = Book
    context_object_name = 'books' # for book in books

class BookDetailView(DetailView):
    model = Book

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author']
    success_url = reverse_lazy('myapp:book_list')

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author']
    success_url = reverse_lazy('myapp:book_list')

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('myapp:book_list')
    