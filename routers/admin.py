from fastapi import HTTPException, Depends, APIRouter
from starlette import status

from database import get_session
from sqlalchemy.orm import Session
import models
import schemas
import painting_service as service

router = APIRouter()


# INSERT SINGLE PAINTING
@router.post("/painting", status_code=status.HTTP_201_CREATED, response_model=schemas.Painting)
def add_painting(painting: schemas.PaintingCreate, session: Session = Depends(get_session)):
    return service.add_painting(session, painting)


# INSERT MULTIPLE PAINTINGS
@router.post("/paintings", status_code=status.HTTP_201_CREATED, response_model=list[schemas.Painting])
def add_paintings(paintings: list[schemas.PaintingCreate], session: Session = Depends(get_session)):
    created_paintings = []

    for painting in paintings:
        created_paintings.append(service.add_painting(session, painting))

    return created_paintings


# UPDATE PAINTING
@router.put("/painting/{id}", response_model=schemas.Painting)
def update_painting(id: int, painting_update: schemas.PaintingCreate, session: Session = Depends(get_session)):
    painting = session.query(models.Painting).get(id)

    if painting:
        print(f'a painting was found - title: {painting.title}')
    else:
        raise HTTPException(status_code=404, detail=f"painting with id {id} not found")

    if painting.id == id:
        print('found painting id, matches path variable')
        painting.title = painting_update.title
        painting.type = painting_update.type
        painting.dimension = painting_update.dimensions
        painting.sold = painting_update.sold
        painting.giclee = painting_update.giclee
        painting.imageUrl = painting_update.imageUrl
        painting.price = painting_update.price
        painting.info = painting_update.info
        session.commit()

    session.close()
    return painting


# DELETE BY ID
@router.delete("/paintings/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, session: Session = Depends(get_session)):
    painting = session.query(models.Painting).get(id)

    if painting:
        session.delete(painting)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"painting with id {id} not found")

    return None
