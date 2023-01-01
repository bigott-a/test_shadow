from rest_framework import serializers

from book_manager.models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField("name", read_only=True)

    class Meta:
        model = Book
        fields = ("id", "name", "author")
