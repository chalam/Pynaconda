from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# from geoalchemy2 import Geometry
from sqlalchemy.orm import sessionmaker


# engine = create_engine("postgresql://user:password@localhost:5434/test")
engine = create_engine("sqlite:///search_models.db", echo=True)
Base = declarative_base()

class Thing(Base):
    __tablename__ = "thing"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # geom = Column(Geometry('POLYGON'))

Session = sessionmaker(bind=engine)
session = Session()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    t = Thing(name='thing1')
    session.add(t)
    t = Thing(name='thing2')
    session.add(t)
    session.commit()
