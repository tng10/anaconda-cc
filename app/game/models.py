from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
from sqlalchemy.orm import relationship

from app.database import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(String, primary_key=True, index=True)
    state = Column(String)
    # state = Column(JSON)
