from django.urls import path

from api.views import GetRelativeData

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="Relative News Api",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)


urlpatterns = [
    path('docs/', schema_view.with_ui(cache_timeout=0)),
    path(r'relative-data/',  GetRelativeData.as_view()),
]

