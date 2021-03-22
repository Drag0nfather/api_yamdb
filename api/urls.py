from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet

router = DefaultRouter()

router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('token/', get_token_func, name='get_token'),
    path('email/', send_mail_func, name='get_verification_code'),
]
