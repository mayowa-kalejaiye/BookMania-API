from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'language', 'genre', 'content')
    search_fields= ('title', 'author', 'genre', 'content', 'language')

admin.site.register(Book, BookAdmin)
