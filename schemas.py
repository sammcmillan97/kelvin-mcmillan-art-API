from pydantic import BaseModel


class PaintingCreateSchema (BaseModel) : 
    title: str
    type: str
    dimensions: str
    sold: bool
    giclee: bool
    imageUrl: str
    price: float
    info: str

class PaintingSchema (BaseModel) : 
    id: int
    title: str
    type: str
    dimensions: str
    sold: bool
    giclee: bool
    imageUrl: str
    price: float
    info: str


