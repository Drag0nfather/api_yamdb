from django.contrib.auth.hashers import make_password, check_password
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from rest_framework.decorators import action, api_view, permission_classes
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.pagination import BasePagination, PageNumberPagination
from rest_framework.response import Response
from rest_framework import mixins, viewsets, filters
from rest_framework import status

from api.models import Title, Genre, Category, User, Review
from api.mail import generate_confirm_code, send_mail_func
from api.permissions import IsAdminPermission, IsAuthorOrStuffOrReadOnly, IsAdminOrReadOnlyPermission
from api.serializers import (
    TitleSerializer,
    GenresSerializer,
    CategoriesSerializer,
    UserSerializer,
    ReviewSerializer,
    CommentSerializer,
    ConfirmationCodeSerializer,
    CheckConfirmationCodeSerializer
)

BASE_USERNAME = 'User'


@api_view(['POST'])
@permission_classes([AllowAny])
def send_confirmation_code(request):
    serializer = ConfirmationCodeSerializer(data=request.data)
    email = request.data.get('email', False)
    if serializer.is_valid():
        confirmation_code = generate_confirm_code()
        user = User.objects.filter(email=email).exists()
        if not user:
            User.objects.create_user(email=email)
        User.objects.filter(email=email).update(
            confirmation_code=make_password(
                confirmation_code,
                salt=None,
                hasher='default'
            )
        )
        send_mail_func(email=email, confirmation_code=confirmation_code)
        return Response(
            f'Код отправлен на адрес {email}',
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_token(request):
    serializer = CheckConfirmationCodeSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.data.get('email')
        confirmation_code = serializer.data.get('confirmation_code')
        user = get_object_or_404(User, email=email)
        if check_password(confirmation_code, user.confirmation_code):
            token = AccessToken.for_user(user)
            return Response({'token': f'{token}'}, status=status.HTTP_200_OK)
        return Response({'confirmation_code': 'Неверный код подтверждения'},
                        status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
    permission_classes = (IsAuthenticated, IsAdminPermission,)

    @action(detail=False, permission_classes=(IsAuthenticated,),
            methods=['get', 'patch'], url_path='me')
    def get_or_update_self(self, request):
        if request.method != 'GET':
            serializer = self.get_serializer(
                instance=request.user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            serializer = self.get_serializer(request.user, many=False)
            return Response(serializer.data)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnlyPermission,)
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save()


class GenresViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (IsAdminOrReadOnlyPermission,)
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)
    lookup_field = 'slug'


class CategoriesViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsAdminOrReadOnlyPermission,)
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)
    lookup_field = 'slug'


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = BasePagination
    permission_classes = (IsAuthorOrStuffOrReadOnly, IsAuthenticatedOrReadOnly)
    filter_backends = (DjangoFilterBackend,)
    fiterser_fields = ('title',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = BasePagination
    permission_classes = (IsAuthorOrStuffOrReadOnly, IsAuthenticatedOrReadOnly)
    filter_backends = (DjangoFilterBackend,)
    fiterser_fields = ('review',)

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)

    def get_queryset(self):
        review_id = self.kwargs.get('review_id', '')
        review = get_object_or_404(Review, pk=review_id)
        return review.comments.all()
