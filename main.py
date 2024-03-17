from fastapi import FastAPI, status, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine
from models import Painting
from schemas import PaintingSchema, PaintingCreateSchema

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()




# GET ALL 
@app.get("/paintings", response_model=list[PaintingSchema])
def get_all():
    session = Session(bind=engine, expire_on_commit=False)
    paintings = session.query(Painting).all()
    session.close()
    return paintings

# GET BY ID
@app.get("/paintings/{id}", response_model=PaintingSchema)
def get_by_id(id: int):

    session = Session(bind=engine, expire_on_commit=False)
    painting = session.query(Painting).get(id)

    if not painting:
        raise HTTPException(status_code=404, detail=f"painting with id {id} not found")
        

    session.close()
    return painting

# GET PORTFOLIO PAGE
@app.get("/paintings/portfolio/{page}", response_model=list[PaintingSchema])
def get_page(page: str):
    return {f'message": "Get paintings for page: {page}'}



# SEARCH 
# later - would only be used for admin
# params: sold, type, catergory, 
@app.get("/paintings/search")
def get_paintings_by_search():
    return {"message": "Hello World"}










# INSERT SINGLE
@app.post("/painting", status_code=status.HTTP_201_CREATED, response_model=str)
def add_painting(painting: PaintingCreateSchema):

    # INFO: While a connection represents the communication link,
    # a session encapsulates the user-specific context and ongoing activities within that connection
    session = Session(bind=engine, expire_on_commit=False)

    newPainting = Painting(
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

    # get the id - it was added automatically presumably because there was a field called id - magic
    id = newPainting.id

    return {f'New Painting Added. Title: {newPainting.title}, id: {id}'}



# INSERT BULK
@app.post("/paintings", status_code=status.HTTP_201_CREATED)
def add_paintings(paintings: list[PaintingCreateSchema]):

     
    return {"message": "Not yet implemented"}






# UPDATE
# Note: Painting request does not hold id but if it is given, nothing explodes, additional fields are fine
@app.put("/painting/{id}", response_model=PaintingSchema)
def update_Painting(id: int, paintingUpdate: PaintingCreateSchema):

    session = Session(bind=engine, expire_on_commit=False)
    painting = session.query(Painting).get(id)

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
def delete_By_Id(id: int):
    session = Session(bind=engine, expire_on_commit=False)
    painting = session.query(Painting).get(id)

    if painting:
        session.delete(painting)
        session.commit()
        session.close()
    else: 
        raise HTTPException(status_code=404, detail=f"painting with id {id} not found")

    return None


