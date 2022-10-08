Модель для нахождения релевантных статей
```python3
from ml.config import RANKING_MODEL_PATH, ACCOUNTANT, DIRECTOR
from ml.models import RankingModel
from ml.utils import find_relevant_news
model = RankingModel(RANKING_MODEL_PATH)
news_list = [
    {'description': 'новость 1'},
    {'description': 'новость 2'},
    {'description': 'новость 3'}
]
print(find_relevant_news(model, ACCOUNTANT, news_list, top_n=3))
```
Модель, формирующая тему по словам
```python3
from ml.models import Rewriter
model = Rewriter()
print(model.get_rewrite('рухнули на открытие цены биржи нефть'))
```