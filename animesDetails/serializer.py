from rest_framework import serializers

from .models import AnimeDetails


class AnimeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeDetails
        fields = ['id', 'title', 'text', 'thumb', ]
        