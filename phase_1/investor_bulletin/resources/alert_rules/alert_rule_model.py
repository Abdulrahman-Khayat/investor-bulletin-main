""" Alert Rule Model """
from db.models.model_base import Base
from sqlalchemy import Column, String, Uuid, Float
from uuid import uuid4


class AlertRule(Base):
    __tablename__ = "alert-rules"

    id = Column(Uuid, primary_key=True, index=True, default=uuid4)
    name = Column(String, nullable=False)
    threshold = Column(Float, nullable=False)
    symbol = Column(String, nullable=False)
