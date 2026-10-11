from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from src.utils.settings import settings


Base = declarative_base()

# engine = create_engine(url=settings.DB_CONNECTION)
engine = create_engine(url=settings.DB_CONNECTION)

with engine.connect() as connection:
    print("Database connected successfully!")


LocalSesion =sessionmaker(bind=engine)


def get_db():
    session=LocalSesion()
    try:
        yield session
    finally:
        session.close()    