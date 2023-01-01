from book_manager.models import Author
from book_manager.serializers import AuthorSerializer
from book_manager_core.serializers import BookManagerMixinViewset


class AuthorViewSet(BookManagerMixinViewset):
    queryset = Author.objects.all().order_by("name")
    serializer_class = AuthorSerializer
