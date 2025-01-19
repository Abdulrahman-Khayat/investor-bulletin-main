""" Alert Rule Schema """
"""_summary_
This file to abstract any validation logic for the Alert Rules
"""
from pydantic import BaseModel
from uuid import UUID


class AlertRuleCreate(BaseModel):
    name: str
    threshold: float
    symbol: str


class AlertRuleRead(BaseModel):
    id: UUID
    name: str
    threshold: float
    symbol: str
