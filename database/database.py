import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm as orm

# no idea
Base = declarative_base()


# setup sqlachemy....

DATABASE_URL = "sqlite:///./database.db";

engine = sql.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

