from pydantic import BaseModel
from typing import List

class CatDogResponse(BaseModel):
    probs: List[float] = []
    best_prob: float = -1.0
    predicted_id: int = -1
    predicted_class: str = ""
    predictor_name: str = ""
