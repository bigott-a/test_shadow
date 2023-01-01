from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return str(self.name)
