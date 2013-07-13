import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key = True)
	name = Column(String)
	zoom = Column(Integer)
	location = Column(String)

	def __init__(self, name, email, zoom, location):
		self.name = name
		self.zoom = zoom
		self.email = email
		self.location = location

	def __repr__(self):
		return "<User('%s','%i','%s', '%s')>" % (self.name, self.zoom, self.email, self.location)


Base.metadata.create_all(engine)







