from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
#from app import db

engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=False,
                                         bind=engine))
BaseModel = declarative_base()
BaseModel.query = db_session.query_property()

# Set your classes here.


class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(90))

    def __init__(self, name=None, password=None, email=None):
        self.name = name
        self.password = password
        self.email = email

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'User: {}'.format(self.name)

    def get_email(self):
        return self.email[:]


# Create tables.
BaseModel.metadata.create_all(bind=engine)
