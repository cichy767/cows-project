from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Cows API",
        default_version='v1',
        description="API documentation for the Cows project",
        contact=openapi.Contact(email="contact@cows.local"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
    url='http://localhost:8080/api/'
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cows.urls')),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'
    ),
]
