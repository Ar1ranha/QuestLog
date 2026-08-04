from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 

from app.database.dependencies import get_db
from app.models.guide import Guide
from app.schemas.guide import GuideCreate, GuideUpdate

router = APIRouter()

@router.post("/guides")
def cadastrar_guide(guide: GuideCreate, db: Session = Depends(get_db)):
    novo_guide = Guide(
        titulo=guide.titulo,
        categoria=guide.categoria,
        conteudo=guide.conteudo,
        game_id=guide.game_id
    )

    db.add(novo_guide)
    db.commit()
    db.refresh(novo_guide)

    return novo_guide

@router.get("/guides")
def listar_guides(db: Session = Depends(get_db)):
    return db.query(Guide).all()

@router.get("/guides/{guide_id}")
def buscar_guide(guide_id: int, db: Session = Depends(get_db)):
    guide = db.query(Guide).filter(Guide.id == guide_id).first()

    if guide is None:
        raise HTTPException(
            status_code=404,
            detail="Guia não encontrado."
        )
    return guide 

@router.put("/guides/{guide_id}")
def atualizar_guide(
    guide_id: int,
    guide_atualizado: GuideUpdate,
    db: Session = Depends(get_db)
):
    guide = db.query(Guide).filter(Guide.id == guide_id).first()

    if guide is None:
        raise HTTPException(
            status_code=404,
            detail="Guia não encontrado."
        )
    
    guide.titulo = guide_atualizado.titulo
    guide.categoria = guide_atualizado.categoria
    guide.conteudo = guide_atualizado.conteudo
    guide.game_id = guide_atualizado.game_id

    db.commit()
    db.refresh(guide)

    return guide

@router.delete("/guides/{guide_id}")
def deletar_guide(guide_id: int, db: Session = Depends(get_db)):
    guide = db.query(Guide).filter(Guide.id == guide_id).first()

    if guide is None:
        raise HTTPException(
            status_code=404,
            detail="Guia não encontrado."
        )
    
    db.delete(guide)
    db.commit()

    return {
        "mensagem": "Guia removido com sucesso."
    }

@router.get("/games/{game_id}/guides/{categoria}")
def listar_guides_por_categoria(
    game_id: int,
    categoria: str,
    db: Session = Depends(get_db)
):
    return db.query(Guide).filter(
        Guide.game_id == game_id,
        Guide.categoria == categoria
    ).all()