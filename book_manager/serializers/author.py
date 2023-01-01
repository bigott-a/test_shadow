from rest_framework import serializers

from book_manager.models import Author


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "name")
