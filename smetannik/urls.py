from django.conf.urls import url
from django.contrib import admin
from rest_framework import permissions
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Smetannik API",
      default_version='v1',
      description="Welcome",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="vadya_i@mail.ru"),
      license=openapi.License(name="SMETA License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('authentication.urls', namespace='authentication')),
    path('api/v1/', include('references.urls', namespace='sndirectory')),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
