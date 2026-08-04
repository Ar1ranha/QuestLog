from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.guide_item import GuideItem
from app.schemas.guide_item import GuideItemCreate

router = APIRouter()

@router.post("/guide-items")
def cadastrar_item(item: GuideItemCreate, db: Session = Depends(get_db)):
    novo_item = GuideItem(
        titulo=item.titulo,
        tipo=item.tipo,
        descricao=item.descricao,
        video_url=item.video_url,
        guide_id=item.guide_id
    )

    db.add(novo_item)
    db.commit()
    db.refresh(novo_item)

    return novo_item

@router.get("/guide-items")
def listar_itens(db: Session = Depends(get_db)):
    return db.query(GuideItem).all()

@router.get("/guide-items/{item_id}")
def buscar_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(GuideItem).filter(GuideItem.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return{
        "id": item.id,
        "titulo": item.titulo,
        "tipo": item.tipo,
        "descricao": item.descricao,
        "video_url": item.video_url,
        "guide_id": item.guide_id,
        "game_id": item.guide.game.id,
        "game_nome": item.guide.game.nome
    }

@router.get("/guides/{guide_id}/items")
def listar_itens_do_guia(
    guide_id: int,
    db: Session = Depends(get_db)
):
    return db.query(GuideItem).filter(
        GuideItem.guide_id == guide_id
    ).all()