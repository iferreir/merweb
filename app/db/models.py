from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Publication(Base):
    __tablename__ = "publications"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    authors = Column(String)
    year = Column(Integer)
    journal = Column(String)
    link = Column(String)       # URL to paper
    notes = Column(Text)        # short description

