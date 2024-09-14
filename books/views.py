from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes 
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from rest_framework import filters
from .permissions import IsAuthor
from django_ratelimit.decorators import ratelimit
from .filters import BookFilter
import logging


logger = logging.getLogger(__name__)


class BookPagination(PageNumberPagination):
    page_size = 3



@permission_classes([IsAuthenticated])
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination
    permission_classes = [IsAuthor]
    filterset_class = BookFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'genre', 'language']
    search_fields = ['title', 'author', 'genre']
    ordering_fields = ['published_date', 'title']

    def list(self, request, *args, **kwargs):
        logger.debug(f"Request method: {request.method}")
        return super().list(request, *args, **kwargs)
    
    @ratelimit(key='ip', rate='5/m', method='ALL', block=True)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @ratelimit(key='ip', rate='5/m', method='POST', block=True)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
