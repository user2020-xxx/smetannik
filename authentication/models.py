
import jwt
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, **extra_fields):
        if username is None:
            raise TypeError('Пользователь должен иметь имя пользователя')

        if email is None:
            raise TypeError('Пользователь должен иметь электронный почтовый адрес')

        if password is None:
            raise TypeError('Пользователь должен иметь пароль')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password):
        return self._create_user(username, email, password)

    def create_superuser(self, username, email, password):
        return self._create_user(username, email, password, is_staff=True, is_superuser=True)


class RoleUserModel(models.Model):
    role = models.CharField(max_length=255, default='', null=True)

    def __str__(self):
        return self.role

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, verbose_name="Имя пользователя", max_length=255, unique=True)
    email = models.EmailField(db_index=True, verbose_name="Почтовый адрес", unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    role = models.ForeignKey(RoleUserModel, on_delete=models.CASCADE, related_name='roles', null=True, default=3)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)
        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')
        return token