import torch
from transformers import AutoTokenizer, AutoModel, AutoConfig
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import requests
import json
from typing import Optional, List
from .config import *


class RankingModel:
    roles = {
        ACCOUNTANT: ACCOUNTANT_DESCRIPTION,
        DIRECTOR: DIRECTOR_DESCRIPTION
    }

    def __init__(self, model_path: str):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModel.from_pretrained(model_path)
        self.roles_embeds = {role: self.get_embed(descr) for role, descr in self.roles.items()}

    def get_sims(self, role: str, texts: List[str]) -> np.array:
        assert role in self.roles_embeds, f'Нет такой роли: {role}. Доступно: {list(self.roles)}'
        role_embed = self.roles_embeds[role]
        embeds = [self.get_embed(text) for text in texts]
        return cosine_similarity([role_embed], embeds)[0]

    def get_embed(self, text: str) -> np.array:
        t = self.tokenizer(text, padding=True, truncation=True, return_tensors='pt')
        with torch.no_grad():
            model_output = self.model(**{k: v.to(self.model.device) for k, v in t.items()})
        embeddings = model_output.last_hidden_state[:, 0, :]
        embeddings = torch.nn.functional.normalize(embeddings)
        return embeddings[0].cpu().numpy()


class Rewriter:
    @staticmethod
    def get_rewrite(text: str) -> Optional[str]:
        """
        Rewrites text api
        :param text: original text
        :return: rewritten version of the text
        """
        try:
            r = requests.post('https://api.aicloud.sbercloud.ru/public/v2/rewriter/predict',
                              json={
                                  "instances": [
                                    {
                                        "text": text,
                                        "temperature": 0.9,
                                        "top_k": 50,
                                        "top_p": 0.7,
                                        "range_mode": "bertscore"
                                    }
                                  ]
                                })
            print(r.status_code)
            if r.status_code != 200:
                raise RuntimeError(f"Сбер вернул {r.status_code}")
            print(r.text)
            d = json.loads(r.text)
            return d['prediction_best']['bertscore']
        except Exception as exc:
            print('Ошибка', exc)
            return text
