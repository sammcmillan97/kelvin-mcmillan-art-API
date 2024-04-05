
import models
import schemas
from sqlalchemy.orm import Session

def add_painting(session: Session, painting: schemas.PaintingCreate) -> models.Painting:
    print(f"adding painting: {painting.title}")

    newPainting = models.Painting(
        title = painting.title,
        type = painting.type, 
        dimensions = painting.dimensions,
        sold = painting.sold,
        giclee = painting.giclee,
        price = painting.price,
        info = painting.info
    )

    # handle optional fields
    if painting.galleryLink is not None:
        newPainting.galleryLink = painting.galleryLink
    if painting.galleryName is not None:
        newPainting.galleryName = painting.galleryName

    # add to db
    session.add(newPainting)
    session.commit() # need to generate the id field for related record creation
    session.refresh(newPainting)
    print(f"the id for the new painting: {newPainting.id}")


# Handle related record creation
# Create page item records
    if painting.pages:
        for page in painting.pages:
            new_page_item = models.PageItem(page=page, page_order=1, painting_id=newPainting.id)
            session.add(new_page_item)
    

    session.commit()
    session.close()
    return newPainting