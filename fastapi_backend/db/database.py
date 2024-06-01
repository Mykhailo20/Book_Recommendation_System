from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
from config.db_config import get_db_config
 
db_config_dict = get_db_config()
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_config_dict ['user']}:{db_config_dict ['password']}@localhost:5432/{db_config_dict ['database']}"
 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
 
Base = declarative_base()
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()