from rest_framework import serializers

from book_manager.models import Kind


class KindSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kind
        fields = ("id", "name")
