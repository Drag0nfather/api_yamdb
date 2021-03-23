from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TitleViewSet#, GenreViewSet, UserViewSet, CategoryViewSet, ReviewViewSet, CommemntViewSet

router = DefaultRouter()
router.register('titles', TitleViewSet)
# router.register('genres', GenreViewSet)
# router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]