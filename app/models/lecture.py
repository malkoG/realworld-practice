from sqlalchemy import Column, Integer, String, Text

from app.database.base_class import Base


class Lecture(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
