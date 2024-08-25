from django.db import models
import uuid
from string import ascii_letters,digits
from django.urls import reverse
from random import choice

# Create your models here.
def autoGenId():
    uniqueId = ''.join(choice(ascii_letters + digits) for _ in range(13))
    return uniqueId

class Book(models.Model):
    CONTENT_CHOICE = (
            ('pg', 'PG'),
            ('pg13', 'PG13'),
            ('17', '17'),
            ('18+', '18+'),
        )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique_for_date='published_date', default="")
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.PositiveIntegerField()
    cover = models.URLField(blank=True)
    language = models.CharField(max_length=20)
    genre = models.CharField(max_length=100, null=False, default="")
    content = models.CharField(max_length=20, choices=CONTENT_CHOICE, default="PG")

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title
    
    @staticmethod
    def get_Book_by_id(ids):
        return Book.objects.filter(id__in=ids)
    
    def get_absolute_url(self):
        return reverse("Books:Book details", 
                       args=[self.published_date.year,
                             self.published_date.month,
                             self.published_date.day,
                             self.slug])
    
    
