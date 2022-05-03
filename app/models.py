from sqlalchemy import Column, Integer, String, DateTime

from database import Base


class Quiz(Base):
    __tablename__ = 'quiz'

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String(500))
    answer = Column(String(500))
    created_at = Column(DateTime)
