from django.shortcuts import render
from django.http import HttpResponse

from config import settings
from news import default_data
from services import get_rel_news


def get_news(request) -> HttpResponse:
    context = {
        'roles': settings.ROLES
    }
    return render(request=request, template_name='news/home.html', context=context)


def get_news_by_role(request, role: str) -> HttpResponse:
    if role in settings.ROLES:
        news_list = default_data.NEWS_LIST_BY_ROLE[role]
        trend_list = default_data.TREND_BY_ROLE[role]
        insite = default_data.INSITE_BY_ROLE[role]
        context = {
            'news_list': news_list,
            'trend_list': trend_list,
            'insite': insite,
            'roles': settings.ROLES,
            'current_role': settings.ROLES[role]
        }
        return render(request=request, template_name='news/news.html', context=context)
    else:
        return render(request=request, template_name='news/error.html', context={'role': role})
