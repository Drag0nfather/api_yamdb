from rest_framework.validators import UniqueTogetherValidator, ValidationError
from rest_framework import serializers

from django.contrib.auth import get_user_model

from api.models import Categories, Genres, Title, User

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


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('first_name', 'last_name', 'username',
                  'bio', 'email', 'role', 'confirmation_code')
        model = User


class ConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class CheckConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)
