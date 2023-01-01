from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from book_manager.models import Author, Book
from book_manager.serializers import BookSerializer
from book_manager_core.serializers import BookManagerMixinViewset


class BookViewSet(BookManagerMixinViewset):
    queryset = Book.objects.all().order_by("name")
    serializer_class = BookSerializer

    def create(self, request: Request, *args, **kwargs):
        if "author" not in request.data:
            return Response(data={"author": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)
        elif not request.data["author"]:
            return Response(data={"author": ["This field may not be blank."]}, status=status.HTTP_400_BAD_REQUEST)

        try:
            author_name = request.data["author"]
            book_name = request.data["name"]
            author = Author.objects.get(name=author_name)
            book = self.serializer_class.Meta.model.objects.create(name=book_name, author=author)
            serializer = self.serializer_class(book)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=self.get_success_headers(serializer.data),
            )
        except Author.DoesNotExist:
            return Response(
                data={"author": [f"'{author_name}' is not a valid author, add it first."]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except IntegrityError:
            return Response(
                data={"name": [f"'Book {book_name}' is already registered with same author."]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except KeyError:
            return super().create(request, *args, **kwargs)
