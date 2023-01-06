from django.db import models

from book_manager.models.book import Book


class BookHistory(models.Model):
    msg = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
