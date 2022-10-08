from typing import List
import numpy as np


def find_relevant_news(model, role: str, news_list: List[dict], top_n=3) -> List[dict]:
    'returns top_n relevant news'
    assert len(news_list) >= top_n, f'Недостаточно новостей: {len(news_list)} новостей при top_n = {top_n}'
    texts = [news['description'] for news in news_list]
    sims = model.get_sims(role, texts)
    indices = np.argsort(sims)[-top_n:]
    relevant_news = [news_list[idx] for idx in indices]
    return relevant_news
