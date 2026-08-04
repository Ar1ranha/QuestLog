from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from fastapi import HTTPException 

from app.database.dependencies import get_db
from app.models.game import Game
from app.schemas.game import GameCreate, GameUpdate
from app.models.guide import Guide

router = APIRouter()

@router.post("/games")
def cadastrar_game(game: GameCreate, db: Session = Depends(get_db)):
    novo_game = Game(
        nome=game.nome,
        desenvolvedora=game.desenvolvedora,
        ano=game.ano,
        genero=game.genero,
        descricao=game.descricao
    )

    db.add(novo_game)
    db.commit()
    db.refresh(novo_game)

    return novo_game

@router.get("/games")
def listar_games(db: Session = Depends(get_db)):
    return db.query(Game).all()

@router.get("/games/{game_id}")
def buscar_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()

    if game is None:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado."
        ) 
    return game

@router.put("/games/{game_id}")
def atualizar_game(
    game_id: int,
    game_atualizado: GameUpdate,
    db: Session = Depends(get_db)
):
    game = db.query(Game).filter(Game.id == game_id).first()

    if game is None:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado."
        )
    
    game.nome = game_atualizado.nome
    game.desenvolvedora = game_atualizado.desenvolvedora
    game.ano = game_atualizado.ano
    game.genero = game_atualizado.genero
    game.descricao = game_atualizado.descricao

    db.commit()
    db.refresh(game)

    return game

@router.delete("/games/{game_id}")
def deletar_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()

    if game is None:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado."
        )
    
    db.delete(game)
    db.commit()

    return {
        "mensagem": "Jogo removido com sucesso."
    }

@router.get("/games/{game_id}/guides")
def listar_guides_do_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()
    if game is None:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado."
        )
    return game.guides

@router.get("/games/{game_id}/categorias")
def listar_categorias(game_id: int, db: Session = Depends(get_db)):
    categorias = db.query(Guide.categoria).filter(
        Guide.game_id == game_id
    ).distinct().all()

    return [categoria[0] for categoria in categorias]