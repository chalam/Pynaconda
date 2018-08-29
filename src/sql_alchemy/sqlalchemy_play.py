from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# from geoalchemy2 import Geometry
from sqlalchemy.orm import sessionmaker


# connecting engine to a SQL Dialect
# engine = create_engine("postgresql://user:password@localhost:5434/test")
engine = create_engine("sqlite:///users_model.db", echo=True)

# declaring entity mapping
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % \
               (self.name, self.fullname, self.password)

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id')) # values in this column should be constrained to be values
                                                      # present in the named remote column.

    user = relationship("User", back_populates="addresses") # many-to-one link since Foreign key on child

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

# http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#relationship-patterns
# create link on the Parent model
User.addresses = relationship("Address", order_by=Address.id, back_populates="user",
                              cascade="all, delete, delete-orphan")

# ORM handle to DB
Session = sessionmaker(bind=engine)
session = Session()

#http://docs.sqlalchemy.org/en/latest/orm/query.html
if __name__ == '__main__':
    # create tables
    Base.metadata.create_all(engine)

    print('schema')
    print(User.__table__)

    # insert
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    session.add(ed_user)

    print(session)
    print(session.dirty)

    our_user = session.query(User).filter_by(name='ed').first()
    assert our_user.name == ed_user.name

    print('rowcount: ', session.query(User).count())

    session.add_all([
            User(name='wendy', fullname='Wendy Williams', password='foobar'),
            User(name='mary', fullname='Mary Contrary', password='xxg527'),
            User(name='fred', fullname='Fred Flinstone', password='blah')])

    ed_user.password = 'f8s7ccs'

    print(session.dirty)

    print(session.new)

    print(ed_user.id) # pending

    session.commit()

    print(ed_user.id)  # presistent

    print('rowcount: ', session.query(User).count())

    ed_user.name = 'Edwardo'
    print(ed_user)
    fake_user = User(name='fakeuser', fullname='Invalid', password='12345')
    session.add(fake_user)

    print(session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all())

    session.rollback()
    print(ed_user)
    print(fake_user in session)

    print(session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all())

    for instance in session.query(User).order_by(User.id):
        print(instance.name, instance.fullname)

    # many-to-one mapping
    jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
    print(jack.addresses)

    jack.addresses = [Address(email_address='jack@google.com'),
                      Address(email_address='j25@yahoo.com')]

    print(jack.addresses[1])
    print(jack.addresses[1].user)

    session.add(jack)
    session.commit()

    jack = session.query(User).filter_by(name='jack').first()
    print(jack)
    print(jack.addresses) # lazy loading Address


    # join
    for u, a in session.query(User, Address). \
            filter(User.id == Address.user_id). \
            filter(Address.email_address == 'jack@google.com'). \
            all():
        print(u)
        print(a)

    print(session.query(User).join(Address). \
        filter(Address.email_address == 'jack@google.com'). \
        all())


    # delete
    session.delete(jack)
    print(session.query(User).filter_by(name='jack').count()) # 0

    # jack = session.query(User).get(5)
    # del jack.addresses[1]
    print(session.query(Address).filter(
        Address.email_address.in_(['jack@google.com', 'j25@yahoo.com'])
        ).count()) # 0 since casade delete