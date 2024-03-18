from pydantic import BaseModel

class KelvBase(BaseModel) : 
    class Config: 
        orm_mode = True

class PaintingCreate (KelvBase) : 
    title: str
    type: str
    dimensions: str
    sold: bool
    giclee: bool
    imageUrl: str
    price: float
    info: str

class Painting (KelvBase) : 
    id: int
    title: str
    type: str
    dimensions: str
    sold: bool
    giclee: bool
    imageUrl: str
    price: float
    info: str


