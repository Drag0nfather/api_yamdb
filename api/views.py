from rest_framework import viewsets

from .models import Title

# TODO: GenreViewSet, UserViewSet, CategoryViewSet, ReviewViewSet, CommemntViewSet
class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()