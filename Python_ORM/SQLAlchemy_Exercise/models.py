from sqlalchemy import create_engine, Integer, Column, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

DATABASE_URL = 'postgresql+psycopg2://postgres:5432@127.0.0.1/postgres'
engine = create_engine(DATABASE_URL)
Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    ingredients = Column(Text, nullable=False)
    instructions = Column(Text, nullable=False)
    chef_id = Column(Integer, ForeignKey('chefs.id'))
    chef = relationship('Chef', back_populates='recipes')  # Object


class Chef(Base):
    __tablename__ = 'chefs'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    recipes = relationship('Recipe', back_populates='chef')  # back_populates == related_name


# The two relationships present the bidirectional model
# Chef.recipes is possible and Recipe.chef is possible
