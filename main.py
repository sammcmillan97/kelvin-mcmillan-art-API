from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas
import painting_service as service

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


# GET PAGE ITEMS
## getting the weird af bug 
@app.get("/paintings/pageitems/all", response_model=list[schemas.PageItem])
def get_page_items_all(session: Session = Depends(get_session)):

    print("Getting page items")
    page_items = session.query(models.PageItem).all()
    session.close()
    return page_items


# GET ALL
@app.get("/paintings", response_model=list[schemas.Painting])
def get_all(session: Session = Depends(get_session)):
    
    paintings = session.query(models.Painting).all()
    session.close()
    return paintings

# GET ORIGINALS
@app.get("/paintings/originals", response_model=list[schemas.Original])
def get_originals(session: Session = Depends(get_session)):
    
    print("Get Orgininals")
    paintings = session.query(models.Painting).filter(models.Painting.sold==False).all()
    #paintings = session.query(models.Painting).all()
    session.close()
    return paintings


# [WIP] GET ORIGINALS BY (Painting) ID
@app.get("/paintings/original/{id}", response_model=schemas.Original)
def get_originals(session: Session = Depends(get_session)):
    
    print("Get Orgininals")
    paintings = session.query(models.Painting).filter(models.Painting.sold==False).all()
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



# GET PORTFOLIO PAGE - duplicated because bug that I keep causing
@app.get("/paintings/portfolio/{page}", response_model=list[schemas.Painting])
def get_portfolio_page(page: str, session: Session = Depends(get_session)):

    paintings = session.query(models.Painting).join(models.PageItem).filter(models.PageItem.page == page).all()

    if not paintings:
        raise HTTPException(status_code=404, detail=f"No paintings found for given page: {page}")
    
    return paintings



# GET PAGE ITEMS
## getting the weird af bug 
@app.get("/paintings/pageitems", response_model=list[schemas.PageItem])
def get_page_items(session: Session = Depends(get_session)):

    print("Getting page items")
    page_items = session.query(models.PageItem).all()
    session.close()
    return page_items




# SEARCH 
# later - would only be used for admin
# params: sold, type, catergory, 
@app.get("/paintings/search")
def get_paintings_by_search():
    return {"message": "Hello World"}


# GET PORTFOLIO PAGE
@app.get("/paintings/{page}", response_model=list[schemas.Painting])
def get_page(page: str, session: Session = Depends(get_session)):

    paintings = session.query(models.Painting).join(models.PageItem).filter(models.PageItem.page == page).all()

    if not paintings:
        raise HTTPException(status_code=404, detail=f"No paintings found for given page: {page}")
    
    return paintings





# INSERT SINGLE
@app.post("/painting", status_code=status.HTTP_201_CREATED, response_model=schemas.Painting)
def add_painting(painting: schemas.PaintingCreate, session: Session = Depends(get_session)):

    return service.add_painting(session, painting)



# INSERT BULK
@app.post("/paintings", status_code=status.HTTP_201_CREATED, response_model=list[schemas.Painting])
def add_paintings(paintings: list[schemas.PaintingCreate], session: Session = Depends(get_session)):

    created_paintings = []

    for painting in paintings:
        created_paintings.append(service.add_painting(session,painting)) 

    return created_paintings

        





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



