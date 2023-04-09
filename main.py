from fastapi import FastAPI
import sqlite3
from routers import painting_routers

app = FastAPI()

app.include_router(painting_routers.router)

con = sqlite3.connect("kelvin.db")
cur = con.cursor()
cur.execute("CREATE TABLE PAINTING (title, price)")

cur.execute("""
    INSERT INTO painting VALUES
        ('Lindis Pass', 200)
""")


@app.get("/")
async def root():
    res = cur.execute("SELECT * FROM painting")
    return_painting = res.fetchone()
    return {"Painting": return_painting}
