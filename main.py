from fastapi import FastAPI, Depends
import sqlite3
#from routers import painting_routers
from database.pydantic_schemas import GetPortfolioPageResponse, GetOriginalsResponse, GetGicleesResponse


import sys
import os

project_root = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, project_root)


app = FastAPI(arbitrary_types_allowed=True)

@app.get("/paintings/{page}", response_model=GetPortfolioPageResponse)
async def get_paintings_for_page(page: str):
    return {"Id": 1, "Title": "A Title", "Type": "Watercolour", "Dimensions": "760x480mm", "Page": page }

@app.get("/paintings/originals", response_model=GetOriginalsResponse)
async def get_orginals(page: str):
    return {"Id": 1, "Title": "A Title", "Type": "Watercolour", "Dimensions": "760x480mm", "Page": page }


@app.get("/paintings/giclees", response_model=GetGicleesResponse)
async def get_giclees(page: str):
    return {"Id": 1, "Title": "A Title", "Type": "Watercolour", "Dimensions": "760x480mm", "Page": page }


# app = FastAPI()

# app.include_router(painting_routers.router)

# con = sqlite3.connect("kelvin.db")
# cur = con.cursor()
# cur.execute("CREATE TABLE PAINTING (title, price)")

# cur.execute("""
#     INSERT INTO painting VALUES
#         ('Lindis Pass', 200)
# """)

# @app.get("/")
# async def root():
#     res = cur.execute("SELECT * FROM painting")
#     return_painting = res.fetchone()
#     return {"Painting": return_painting}

# Dependency to print information
def print_dependency():
    print("This is being executed")
    print("Executing print_dependency")
    print(sys.path)
    return True

@app.get("/")
async def read_root(print_info: bool = Depends(print_dependency)):
    return {print(sys.path)}
