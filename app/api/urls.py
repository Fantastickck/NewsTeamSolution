from django.urls import path

from api.views import GetRelativeData

urlpatterns = [
    path(r'relative-data/',  GetRelativeData.as_view()),
]

