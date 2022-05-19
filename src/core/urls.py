from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.helpers import get_full_url

schema_view = get_schema_view(
   openapi.Info(
      title="TN CHARITY API",
      default_version='v1',
      description="API for Tatneft Charity",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   url=get_full_url()
)

api_urls = [
    path('', include('charity.urls'), name='charity'),
]

if settings.DEBUG:
    api_urls.extend([
        re_path(r'^swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
