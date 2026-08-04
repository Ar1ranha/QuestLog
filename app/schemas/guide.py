from pydantic import BaseModel, ConfigDict

class GuideCreate(BaseModel):
    titulo: str
    categoria: str
    conteudo: str
    game_id: int

class GuideResponse(GuideCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)

class GuideUpdate(BaseModel):
    titulo: str
    categoria: str
    conteudo: str
    game_id: int