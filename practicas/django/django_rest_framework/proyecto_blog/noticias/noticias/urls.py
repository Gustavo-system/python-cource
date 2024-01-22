from django.contrib import admin
from django.urls import path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
		title="Documentacion Noticias",
		default_version='v0.0.1',
		description="Documentacion del api de noticias",
		license=openapi.License(name="BSD License"),
   ),
   public=True,
)


urlpatterns = [
	path("docs/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("redocs/", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("admin/", admin.site.urls),
]
