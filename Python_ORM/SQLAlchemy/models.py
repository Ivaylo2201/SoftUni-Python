from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Boolean

# These 3 can be placed in a settings.py file to increase abstraction
DATABASE_URL = 'postgresql+psycopg2://postgres:5432@127.0.0.1/postgres'
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    is_completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')  # a JOIN is created
#   With the relationship field this is possible -> <Оrder>.user.username
