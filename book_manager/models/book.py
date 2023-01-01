import uuid

from django.db import models

from book_manager.models.author import Author


class Book(models.Model):
    name = models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    ref = models.UUIDField(blank=True, default=uuid.uuid1())

    def __str__(self):
        return str(self.name)
