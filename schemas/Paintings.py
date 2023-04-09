from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum
from pydantic import BaseModel


class PaintingType(str, Enum):
    Marine = "Marine"
    Rural = "Rural"
    Landscape = "Landscape"
    Architectural = "Architectural"
    Portrait = "Portrait"
    Sport = "Sport"


class Painting(BaseModel):
    id: Optional[UUID] = uuid4()
    title: str
    type: List[PaintingType]
    isSold: bool
    isGiclee: bool
    price: int
    image_path: str

