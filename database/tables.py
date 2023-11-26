import sqlalchemy as sql
import sqlalchemy.orm as orm
import enum

import database.database as db

class TypeEnum(enum.Enum):
    watercolor = 1
    acrylic = 2

class Painting(db.Base):
    __tablename__ = "Paintings"
    id = sql.column(sql.Integer, primary_key=True, index=True)
    title = sql.column(sql.String, unique=True, index=True)
    type = sql.column(sql.Enum(TypeEnum))
    dimensions = sql.column(sql.String, nullable=False)
    sold = sql.column(sql.Boolean)
    isGiclee = sql.column()
    imagePath = sql.column(sql.String)
    price = sql.column(sql.String)
    




# it would be a lot simpler to have a seperate table per portfolio page.. or would it, would that really make sense. We can just create views.
class PortfolioItem(db.Base):
    __tablename__ = "PortfoliItem"
    id = sql.column(sql.Integer, primary_key=True) # hmmm pointless, we would identify a row by the paitingID and pageName
    paintintgId = sql.column(sql.String, sql.ForeignKey("Paintings.id"))
    pageName = sql.column(sql.String, sql.ForeignKey("PortfolioPages.name"))
    position = sql.column(sql.Integer) 


class PortfolioPage(db.Base):
        __tablename__ = "PortfolioPages"
        pageName = sql.column(sql.String, primary_key=True)



     

class Original(db.Base):
     __tablename__ = "Originals"
     id = sql.column(sql.Integer, primary_key=True)
     price = sql.column(sql.Double, sql.ForeignKey("Paintings.price"))
     framed = sql.column(sql.Boolean, default=False)
     location = sql.column(sql.String, default="unknown")





class Giclee(db.Base):
    __tablename__ = "Giclees"
    id = sql.column(sql.Integer, primary_key=True, index=True) #do we need this field? could we use paintingId or paintingTitle?
    paintingId = sql.column(sql.String, sql.ForeignKey("Paintings.id"), unique=True)

# A Giclee will have a number of size options
class GicleeSizeOption(db.Base):
    __tablename__ = "GicleeSizeOptions"
    id = sql.column(sql.String, primary_key=True)
    paintingId = (sql.String, sql.ForeignKey("Paintings.id"))
    dimensions = sql.column(sql.String, sql.ForeignKey("GicleeSizeOptionAttributes.dimensions"))


# the size and price of a Gicleee size option
class GicleeSizeOptionAttributes(db.Base):
    __tablename__ = "GicleeSizeOptionAttributes"
    dimensions = sql.column(sql.String, primary_key=True) # this can be the foreign key for Giclee Size Options
    price = sql.column(sql.Column)



    