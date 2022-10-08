import os
from typing import List

import pandas as pd

from config import settings
from ml.config import RANKING_MODEL_PATH
from ml.models import RankingModel
from ml.utils import find_relevant_news


def get_dataframe(role: str) -> List[dict]:
    path = os.path.join(os.getcwd(), 'files', settings.FILE_BY_ROLE[role])
    df = pd.read_csv(path)
    df = df.to_dict("records")
    return df


def get_rel_news(role: str) -> List[dict]:
    df = get_dataframe(role=role)
    model = RankingModel(RANKING_MODEL_PATH)
    news_list = find_relevant_news(
        model, settings.ROLES[role], df[:settings.COUNT_INPUT], top_n=settings.COUNT_OUTPUT)
    return news_list