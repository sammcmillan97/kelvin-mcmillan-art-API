from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()





# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()





# GET ALL 
@app.get("/paintings", response_model=list[schemas.Painting])
def get_all(session: Session = Depends(get_session)):
    
    paintings = session.query(models.Painting).all()
    session.close()
    return paintings

# GET BY ID
@app.get("/paintings/{id}", response_model=schemas.Painting)
def get_by_id(id: int, session: Session = Depends(get_session)):

    
    painting = session.query(models.Painting).get(id)

    if not painting:
        raise HTTPException(status_code=404, detail=f"painting with id {id} not found")
        

    session.close()
    return painting

# GET PORTFOLIO PAGE
@app.get("/paintings/portfolio/{page}", response_model=list[schemas.Painting])
def get_page(page: str, session: Session = Depends(get_session)):
    return {f'message": "Get paintings for page: {page}'}



# SEARCH 
# later - would only be used for admin
# params: sold, type, catergory, 
@app.get("/paintings/search")
def get_paintings_by_search():
    return {"message": "Hello World"}










# INSERT SINGLE
@app.post("/painting", status_code=status.HTTP_201_CREATED, response_model=schemas.Painting)
def add_painting(painting: schemas.PaintingCreate, session: Session = Depends(get_session)):

    # INFO: While a connection represents the communication link,
    # a session encapsulates the user-specific context and ongoing activities within that connection
    

    newPainting = models.Painting(
        title = painting.title,
        type = painting.type, 
        dimensions = painting.dimensions,
        sold = painting.sold,
        giclee = painting.giclee,
        imageUrl = painting.imageUrl,
        price = painting.price,
        info = painting.info
        )
    
    session.add(newPainting)
    session.commit()

    # so we get the id that was just assigned when the new painting was inserted.
    session.refresh(newPainting)

    session.close()

    return newPainting



# INSERT BULK
@app.post("/paintings", status_code=status.HTTP_201_CREATED, response_model=list[schemas.Painting])
def add_paintings(paintings: list[schemas.PaintingCreate], session: Session = Depends(get_session)):

     
    return {"message": "Not yet implemented"}






# UPDATE
# Note: Painting request does not hold id but if it is given, nothing explodes, additional fields are fine
@app.put("/painting/{id}", response_model=schemas.Painting)
def update_Painting(id: int, paintingUpdate: schemas.PaintingCreate, session: Session = Depends(get_session)):

    
    painting = session.query(models.Painting).get(id)

    if painting:
        print(f'a painting was found - title: {painting.title}')
    else:
        raise HTTPException(status_code=404, detail=f"painting with id {id} not found")

    if painting.id == id:
        print('found painting id, matches path variable')
        painting.title = paintingUpdate.title
        painting.type = paintingUpdate.type
        painting.dimension = paintingUpdate.dimensions
        painting.sold = paintingUpdate.sold
        painting.giclee = paintingUpdate.giclee
        painting.imageUrl = paintingUpdate.imageUrl
        painting.price = paintingUpdate.price
        painting.info = paintingUpdate.info
        session.commit()

    session.close()

    # why is this here? the check on id causes explosion if we dont throw the error earlier
    if not painting:
        raise HTTPException(status_code=404, detail=f"painting with id {id} not found")
     
    return painting


# DELETE BY ID
@app.delete("/paintings/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_By_Id(id: int, session: Session = Depends(get_session)):
    
    painting = session.query(models.Painting).get(id)

    if painting:
        session.delete(painting)
        session.commit()
        session.close()
    else: 
        raise HTTPException(status_code=404, detail=f"painting with id {id} not found")

    return None


