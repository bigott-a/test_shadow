from book_manager.models import Kind
from book_manager.serializers import KindSerializer
from book_manager_core.serializers import BookManagerMixinViewset


class KindViewSet(BookManagerMixinViewset):
    queryset = Kind.objects.all().order_by("name")
    serializer_class = KindSerializer
