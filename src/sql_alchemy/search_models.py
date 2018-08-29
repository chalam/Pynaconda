from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# from geoalchemy2 import Geometry
from sqlalchemy.orm import sessionmaker


# connecting engine to a SQL Dialect
# engine = create_engine("postgresql://user:password@localhost:5434/test")
engine = create_engine("sqlite:///search_models.db", echo=True)

# declaring entity mapping
Base = declarative_base()
class Thing(Base):
    __tablename__ = "thing"
    # create schema
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # geom = Column(Geometry('POLYGON'))

    def __repr__(self):
        return 'id: %d, name: %s' % (self.id, self.name)

# ORM handle to DB
Session = sessionmaker(bind=engine)
session = Session()

#http://docs.sqlalchemy.org/en/latest/orm/query.html
if __name__ == '__main__':
    Base.metadata.create_all(engine)

    print('schema')
    print(Thing.__table__)

    print('insert')
    t = Thing(name='thing1')
    session.add(t) # pending
    t = Thing(name='thing2')
    session.add(t) # pending
    session.commit() # flush
    for t in session.query(Thing):
        print(t)

    print('bulk insert')
    session.add_all([Thing(name='thing3'),
                 Thing(name='thing4'),
                 Thing(name='thing5')])
    session.commit()
    for t in session.query(Thing):
        print(t)

    print('delete')
    session.query(Thing).filter(Thing.name == 'thing1').delete(synchronize_session=False)
    session.query(Thing).filter(Thing.name == 'thing2').delete(synchronize_session=False)
    for t in session.query(Thing).distinct():
        print(t)

    print('row count: %d' % session.query(Thing).count())

    print('filter')
    for t in session.query(Thing).filter(Thing.name == 'thing5'):
        print(t)

    t = session.query(Thing). \
        filter_by(name='thing5', id=41)
    print(t)

    print('group-by/having')
    q = session.query(Thing.name). \
        group_by(Thing.name). \
        having(func.count(Thing.name) > 2)
    for t in q:
        print(t)

    print('update')
    session.query(Thing).filter(Thing.id == 41). \
        update({Thing.name: 'thing55'}, synchronize_session=False)
    t = session.query(Thing). \
        filter_by(id=41)
    print(t)
    t = session.query(Thing).filter(Thing.name == 'thing55')
    print(t)


    # patterns
    # Identity Map = all ops on single row within session is on a single object
    # Object states = transient (outside session) => pending (inside session, not flushed) => persistent (committed, refreshed)
