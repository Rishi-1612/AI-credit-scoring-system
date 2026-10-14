import os

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base

# Authentication uses a separate database from the scoring/audit database.
# Configure these values in alternate_credit_backend/.env.
from app.config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD

AUTH_DB_NAME = os.getenv("AUTH_DB_NAME", "credit_auth_db")

DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=AUTH_DB_NAME,
)

engine = create_engine(
    DATABASE_URL,
    echo=os.getenv("SQLALCHEMY_ECHO", "false").lower() == "true",
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
