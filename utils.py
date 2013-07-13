import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Table, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/puzzles')
Base = declarative_base()

goodie_group = Table('association', Base.metadata,
	Column('user_id', Integer, ForeignKey('users.id')),
	Column('goodie_id', Integer, ForeignKey('goodies.id'))
)

class User(Base):
	__tablename__ = 'users'

	goodies = relationship("Goodie",
		secondary=goodie_group,
		backref="users")

	id = Column(Integer, primary_key = True)
	name = Column(String)
	zoom = Column(Integer)
	email = Column(String)
	location = Column(String)

	def __init__(self, name, email, zoom, location):
		self.name = name
		self.zoom = zoom
		self.email = email
		self.location = location

	def __repr__(self):
		return "<User('%s','%i','%s', '%s')>" % (self.name, self.zoom, self.email, self.location)


class Goodie(Base):
	__tablename__ = 'goodies'

	id = Column(Integer, primary_key = True)
	name = Column(String)
	group_size = Column(Integer)
	picture = Column(String)
	description = Column(Text)
	location = Column(String)

	def __init__(self, name, group_size, picture, description, location):
		self.name = name
		self.group_size = group_size
		self.picture = picture
		self.description = description
		self.location = location

	def __repr__(self):
		return "<Goodie('%s','%i','%s','%s','%s')>" % (self.name, self.group_size, self.picture, self.description, self.location)


Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()


#####----- Tests -----#####

# test1 = User('jared','jared@me.com',10,'here')
# test2 = User('mary','mary@gmail.com',10,'there')
# test3 = User('joe','joe@me.com',10,'somewhere')
# test4 = User('chris','chris@me.com',10,'over there')
# test5 = User('lauren','lauren@gmail.com',10,'not here')
# test6 = User('alex','alex@me.com',10,'anywhere')

# goodie = Goodie('coupon',4,'----','free stuff!!','nearby')

# session.add(test1)
# session.add(test2)
# session.add(test3)
# session.add(test4)
# session.add(test5)
# session.add(test6)

# session.commit()

# our_user = session.query(User).filter_by(name='jared').first()

# goodie1 = Goodie






