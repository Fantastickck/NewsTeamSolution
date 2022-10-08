import os

from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd

from config import settings
from config.settings import ROLES

from ml.config import RANKING_MODEL_PATH, ACCOUNTANT, DIRECTOR
from ml.models import RankingModel
from ml.utils import find_relevant_news


def get_news(request) -> HttpResponse:
    context = {
        'roles': ROLES
    }
    return render(request=request, template_name='news/home.html', context=context)


def get_news_by_role(request, role: str) -> HttpResponse:
    if role in ROLES:
        path = os.path.join(os.getcwd(), 'files', settings.FILE_BY_ROLE[role])
        df = pd.read_csv(path)
        df = df.to_dict("records")
        model = RankingModel(RANKING_MODEL_PATH)
        news_list = find_relevant_news(
            model, ACCOUNTANT, df[:settings.COUNT_INPUT], top_n=settings.COUNT_OUTPUT)
        trend = settings.TREND_BY_ROLE[role]
        insite = settings.INSITE_BY_ROLE[role]
        context = {
            'news_list': news_list,
            'trend': trend,
            'insite': insite,
            'roles': settings.ROLES,
            'current_role': settings.ROLES[role]
        }
        return render(request=request, template_name='news/news.html', context=context)
    else:
        return render(request=request, template_name='news/error.html', context={'role': role})
