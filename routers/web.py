from fastapi import HTTPException, Depends, APIRouter
from database import get_session
from sqlalchemy.orm import Session
import models
import schemas

router = APIRouter()


# GET ALL PAINTINGS
@router.get("/paintings", response_model=list[schemas.Painting])
def get_all(session: Session = Depends(get_session)):
    paintings = session.query(models.Painting).all()
    session.close()
    return paintings


# GET ALL ORIGINALS
@router.get("/paintings/originals", response_model=list[schemas.Original])
def get_originals(session: Session = Depends(get_session)):
    paintings = session.query(models.Painting).filter(not models.Painting.sold).all()
    session.close()
    return paintings


# GET ORIGINAL BY ID
@router.get("/paintings/originals/{id}", response_model=schemas.Original)
def get_original_by_id(id: int, session: Session = Depends(get_session)):
    painting = session.query(models.Painting).get(id)
    if not painting:
        raise HTTPException(status_code=404, detail=f"no painting found with given id: {id}")

    if painting.sold:
        raise HTTPException(status_code=400,
                            detail=f"painting {id} - {painting.title} was found but is not available as an original")
    session.close()
    return painting


# GET BY ID
@router.get("/paintings/{id}", response_model=schemas.Painting)
def get_by_id(id: int, session: Session = Depends(get_session)):
    painting = session.query(models.Painting).get(id)

    if not painting:
        raise HTTPException(status_code=404, detail=f"painting with id {id} not found")

    session.close()
    return painting


# GET PORTFOLIO PAGE
@router.get("/paintings/{page}", response_model=list[schemas.Painting])
def get_page(page: str, session: Session = Depends(get_session)):
    paintings = session.query(models.Painting).join(models.PageItem).filter(models.PageItem.page == page).all()

    if not paintings:
        raise HTTPException(status_code=404, detail=f"No paintings found for given page: {page}")

    return paintings
