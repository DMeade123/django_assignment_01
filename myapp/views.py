from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book #import book model from models.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books' # for book in books

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author']
    success_url = reverse_lazy('myapp:book_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'myapp/book_form.html'
    success_url = reverse_lazy('myapp:book_list')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user or self.request.user.is_staff

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'myapp/book_confirm_delete.html'
    success_url = reverse_lazy('myapp:book_list')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user or self.request.user.is_staff

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filterset_fields = ['title', 'author_id'] # Fields for exact matches (e.g., ?field1=value)
    search_fields = ['title'] # Fields for ?search=... parameter
    ordering_fields = ['title', 'id']  # Fields allowed for ?ordering=...
    ordering = ['id'] # Default ordering if not specified by client

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)