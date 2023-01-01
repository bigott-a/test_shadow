from django.db import models

from book_manager.models.author import Author


class Book(models.Model):
    name = models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("name", "author")

    def __str__(self):
        return str(self.name)
