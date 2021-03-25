from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, send_confirmation_code, get_token

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('token/', get_token, name='get_token'),
    path('email/', send_confirmation_code, name='get_verification_code'),
]
