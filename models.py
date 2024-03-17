
from sqlalchemy import  Column, Integer, String, Boolean, Float
from database import Base


# TABLES: 
class Painting(Base):
    __tablename__ = 'paintings'
    id = Column(Integer, primary_key=True)
    title = Column(String(256), unique=True)
    type = Column(String, nullable=False)
    dimensions = Column(String, nullable=False)
    sold = Column(Boolean, nullable=False)
    giclee = Column(Boolean, default=False)
    imageUrl = Column(String, nullable=False)
    price = Column(Float)
    info = Column(String)