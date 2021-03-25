from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from .models import Title, Genres, Categories
from .serializers import TitleSerializer, GenresSerializer, CategoriesSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        return title.name.all()

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save()

    
class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
