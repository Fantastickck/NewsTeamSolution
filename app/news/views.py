from django.shortcuts import render
from django.http import HttpResponse

from config.settings import ROLES


def get_news(request) -> HttpResponse:
    context = {
        'roles': ROLES
    }
    return render(request=request, template_name='news/home.html', context=context)


def get_news_by_role(request, role: str) -> HttpResponse:
    if role in ROLES:
        context = {
            'roles': ROLES,
            'current_role': ROLES[role]
        }
        return render(request=request, template_name='news/news.html', context=context)
    else:
        return render(request=request, template_name='news/error.html', context={'role': role})
