from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.views import TitleViewSet, GenreViewSet, CategoryViewSet, UserViewSet, ReviewViewSet, CommentViewSet, send_confirmation_code, get_token

v1_router = DefaultRouter()

v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews_api_v1',
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments_api_v1',
)
v1_router.register('titles', TitleViewSet)
v1_router.register('genres', GenreViewSet)
v1_router.register('categories', CategoryViewSet)
v1_router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(v1_router.urls)),
]

urlpatterns += [
    path('token/', get_token, name='get_token'),
    path('email/', send_confirmation_code, name='get_verification_code'),




urlpatterns = [
    path('', include(v1_router.urls)),
]
