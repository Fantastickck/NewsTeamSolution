from django.contrib import admin
from django.urls import include, path

from news.views import get_news_by_role, get_news


urlpatterns = [
    # path('docs/'),

    path(r'news/', get_news, name='news'),
    path(r'news/<str:role>/', get_news_by_role, name='news_by_role')
]