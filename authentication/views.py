import jwt
from django.conf import settings
from django.http import JsonResponse
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import RoleUserModel, User

from .serializers import (
    RegistrationSerializer, LoginSerializer, UserSerializer, LogoutSerializer, RoleSerilizer, UserRoleSerializer,
    ChangeUserRoleSerializer)
from .renderers import UserJSONRenderer


class RegistrationAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        """
            post:Регистрация нового пользователя
            """
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(GenericAPIView):
    """
        post: Представление для авторизации пользователя по почте и паролю
        """
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """
        put: Обновление пользователя

        patch: Частичное обновление пользователя
        """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data

        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(GenericAPIView):
    """
        post: Разлогирование пользователя
        """
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """Validate token and save."""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ListGroupApiView(generics.ListAPIView):
    """
        get: Вывод списка существующих ролей
        """
    queryset = RoleUserModel.objects.all()
    serializer_class = RoleSerilizer


class ListUserRole(generics.ListAPIView):
    """
        get: Вывод пользователей с их ролью
        """
    queryset = User.objects.all()
    serializer_class = UserRoleSerializer
    filterset_fields = ['id']


@api_view(['GET'])
def updateRole(request, pk, role):
    """
    get: Обновление роли пользователя
    :param request:
    :param pk:
    :param role:
    :return:
    """
    User.objects.filter(pk=pk).update(role=role)
    return Response("User role changed")


@api_view(['GET'])
def getUser(request, token):
    """
    get: Возвращение данных пользователя по токену
    :param request:
    :param token:
    :return:
        """
    tokenData = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    user = User.objects.all().get(id=tokenData['id'])

    data = {"user":
        {
            'email': user.email,
            'username': user.username,
            'role': user.role.role,
        }
    }

    return JsonResponse(data, status=status.HTTP_200_OK)
