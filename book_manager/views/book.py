from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from book_manager.models import Author, Book, Kind
from book_manager.serializers import BookSerializer
from book_manager_core.serializers import BookManagerMixinViewset


class BookViewSet(BookManagerMixinViewset):
    queryset = Book.objects.all().order_by("title")
    serializer_class = BookSerializer

    def create(self, request: Request, *args, **kwargs):
        try:
            book_title = request.data["title"]
        except KeyError:
            super().create(request, *args, **kwargs)
        try:
            author_name = request.data["author"]
            author = Author.objects.get(name=author_name)
        except Author.DoesNotExist:
            author = None
        except KeyError:
            author = None

        try:
            kind_name = request.data["kind"]
            kind = Kind.objects.get(name=kind_name)
        except Kind.DoesNotExist:
            kind = None
        except KeyError:
            kind = None

        book = self.serializer_class.Meta.model.objects.create(title=book_title, author=author, kind=kind)
        serializer = self.serializer_class(book)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data),
        )

    def update(self, request: Request, *args, **kwargs):
        pk, partial = kwargs.get("pk"), kwargs.get("partial", False)
        book = self.serializer_class.Meta.model.objects.get(pk=pk)

        try:
            for field in (
                request.data
                if partial
                else map(lambda x: x.verbose_name, self.serializer_class.Meta.model._meta.get_fields())
            ):
                if field == "ID":
                    continue
                elif field == "author":
                    res = Author.objects.get(name=request.data[field])
                elif field == "kind":
                    res = Kind.objects.get(name=request.data[field])
                else:
                    res = request.data[field]
                setattr(book, field, res)
        except KeyError:
            return super().update(request, *args, **kwargs)

        book.save()
        serializer = self.serializer_class(book)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
            headers=self.get_success_headers(serializer.data),
        )
