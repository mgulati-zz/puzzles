import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Table, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///:memory:', echo=True)
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








