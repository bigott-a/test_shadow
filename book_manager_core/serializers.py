from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated


class BookManagerMixinViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in (
            "retrieve",
            "list",
        ):
            self.permission_classes = [AllowAny]
        return super().get_permissions()
