from django.db import models
from django.utils import timezone

from book_manager.models.author import Author
from book_manager.models.kind import Kind


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, default=None)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE, null=True, blank=True, default=None)
    is_out = models.BooleanField(blank=True, default=False)
    last_update = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return str(self.title)

    def borrow_book(self):
        """
        Update book that is borrowed
        """
        return False if self.is_out else self.update_book_status("Book was borrowed", True)

    def return_book(self):
        """
        Update book that is returned
        """
        return self.update_book_status("Book was returned", False) if self.is_out else False

    def update_book_status(self, msg: str, is_out: bool):
        """
        Update status of book
        ...
        :param str msg: description of changes
        :param bool is_out: is the book borrowed or not
        """
        from book_manager.models.book_history import BookHistory  # pylint: disable=import-outside-toplevel

        try:
            t_now = timezone.now()
            BookHistory.objects.create(msg=msg, date_time=t_now, book=self)
            self.is_out = is_out
            self.last_update = t_now
            self.save()
            return True
        except Exception:
            return False
