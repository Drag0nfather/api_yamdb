from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator, ValidationError

from django.contrib.auth import get_user_model

from .models import Categories, Genres, Title

User = get_user_model()


class CategoriesSerializer(serializers.ModelSerializer):
    search = serializers.CharField()

    class Meta:
        fields = '__all__'
        model = Categories


class GenresSerializer(serializers.ModelSerializer):
    search = serializers.CharField()

    class Meta:
        fields = '__all__'
        model = Genres


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='search'
    )

    class Meta:
        fields = '__all__'
        model = Title
