from django.db import models

from book_manager.models.author import Author
from book_manager.models.kind import Kind


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, default=None)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return str(self.title)
