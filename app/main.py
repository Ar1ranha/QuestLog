from fastapi import FastAPI

from app.database.connection import Base, engine
from app.models.game import Game
from app.models.guide import Guide
from app.routes.game_routes import router as game_router
from app.routes.guide_routes import router as guide_router
from fastapi.middleware.cors import CORSMiddleware
from app.models.guide_item import GuideItem
from app.routes.guide_item_routes import router as guide_item_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="QuestLog API",
    description="API para gerenciamento de guias de jogos.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(game_router)
app.include_router(guide_router)
app.include_router(guide_item_router)

@app.get("/")
def home():
    return{
        "mensagem": "Bem-vindo à QuestLog API!"
    }
