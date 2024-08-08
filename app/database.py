from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = postgresql://database_username:database_password@database_hostname/database_name
SQLALCHEMY_DATABASE_URL = "postgresql://neondb_owner:rYVAD7h5QgyX@ep-snowy-hall-a566vdo7.us-east-2.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
