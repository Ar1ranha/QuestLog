from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class GuideItem(Base):
    __tablename__ = "guide_items"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(150), nullable=False)
    tipo = Column(String(50), nullable=False)
    descricao = Column(Text, nullable=False)
    guide_id = Column(Integer, ForeignKey("guides.id"))
    video_url = Column(Text)
    guide = relationship("Guide", back_populates="itens")