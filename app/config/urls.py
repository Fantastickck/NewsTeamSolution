from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('news.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

