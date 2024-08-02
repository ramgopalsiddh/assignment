from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

# database url for access database
DATABASE_URL = "postgresql://ram@localhost:5432/assignment"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
models.Base.metadata.create_all(bind=engine)
