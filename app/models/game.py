from sqlalchemy import Column, Integer, String, Text
from app.database.connection import Base
from sqlalchemy.orm import relationship

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    desenvolvedora = Column(String(100), nullable=False)
    ano = Column(Integer, nullable=False)
    genero = Column(String(100), nullable=False)
    descricao = Column(Text)

    guides = relationship("Guide", back_populates="game", cascade="all, delete")

