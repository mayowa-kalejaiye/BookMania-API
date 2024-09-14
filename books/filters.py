# filters.py
from django_filters.rest_framework import FilterSet, CharFilter
from .models import Book

class BookFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')
    author = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'author']
