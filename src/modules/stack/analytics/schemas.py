from pydantic import BaseModel, ConfigDict, Field
from typing import Any, Dict, List, Optional


class StackItem(BaseModel):
    model_config = ConfigDict(extra="allow")


class StackStats(BaseModel):
    model_config = ConfigDict(extra="allow")

    total: int
    answered: int
    not_answered: int


class HighestReputation(BaseModel):
    model_config = ConfigDict(extra="allow")


class LowestViews(BaseModel):
    model_config = ConfigDict(extra="allow")


class QuestionAge(BaseModel):
    model_config = ConfigDict(extra="allow")