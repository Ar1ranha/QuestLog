from pydantic import BaseModel, ConfigDict

class GuideItemCreate(BaseModel):
    titulo: str
    tipo: str
    descricao: str
    video_url: str
    guide_id: int

class GuideItemResponse(GuideItemCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)