from django.urls import path

from .views import (
    RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView, LogoutAPIView, ListGroupApiView, ListUserRole, updateRole, getUser
)

app_name = 'authentication'
urlpatterns = [
    path('user/update/', UserRetrieveUpdateAPIView.as_view()),
    path('registrate/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view(), name="logout_user"),
    path('user/role_list/', ListGroupApiView.as_view()),
    path('user/role_user/', ListUserRole.as_view()),
    path('user/role_user_change/<int:pk>/<int:role>', updateRole),
    path('user/get/<str:token>', getUser),
]