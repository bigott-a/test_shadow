from django.urls import include, path
from rest_framework import routers

from book_manager.views import AuthorViewSet, BookViewSet, KindViewSet

router = routers.DefaultRouter()
router.register(r"authors", AuthorViewSet)
router.register(r"books", BookViewSet)
router.register(r"kinds", KindViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
