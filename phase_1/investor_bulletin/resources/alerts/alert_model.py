""" Alert Model """
from db.models.model_base import Base
from sqlalchemy import Column, String, Uuid, Float

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Uuid, primary_key=True, index=True)
    name = Column(String, nullable=False)
    threshold = Column(Float, nullable=False)
    symbol = Column(String, nullable=False)
