from pydantic import BaseModel, ConfigDict

class GameCreate(BaseModel):
    nome: str
    desenvolvedora: str
    ano: int
    genero: str
    descricao: str

class GameResponse(GameCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)

class GameUpdate(BaseModel):
    nome: str
    desenvolvedora: str
    ano: int
    genero: str
    descricao: str