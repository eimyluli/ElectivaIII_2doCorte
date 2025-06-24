from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///estudio_unas.db", echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()
