from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database.connection import Base

class Guide(Base):
    __tablename__ = "guides"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(150), nullable=False)
    categoria = Column(String(100), nullable=False)
    conteudo = Column(Text, nullable=False)

    game_id = Column(Integer, ForeignKey("games.id"))

    game = relationship("Game", back_populates="guides")

    itens = relationship(
        "GuideItem",
        back_populates="guide",
        cascade="all, delete"
    )