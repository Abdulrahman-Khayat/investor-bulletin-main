""" Model base """

from .model_base import Base

from .models import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from api.config import settings

engine = create_engine(settings.database_url, echo=True)
engine.connect()
# Create a session factory
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base.metadata.create_all(bind=engine)

def get_db():
    """Dependency to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
