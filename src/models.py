import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()





class Usuarios(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    apellido = Column(String(250))
    mail = Column(String(250))
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    created = Column(String(250))
    diameter = Column(String(250))
    gravity = Column(String(250))
    rotation_period = Column(String(250))
    rotation_period = Column(String(250))


class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    cargo_capacity = Column(String(250))
    cost_in_credit = Column(String(250))
    length = Column(String(250))
    model = Column(String(250))
    passengers = Column(String(250))

class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    cargo_capacity = Column(String(250))
    cost_in_credit = Column(String(250))
    length = Column(String(250))
    model = Column(String(250))
    passengers = Column(String(250))
   




class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    vehiculos_id = Column(Integer, ForeignKey('vehiculos.id'))
    starships_id = Column(Integer, ForeignKey('starships.id'))
    usuarios = relationship(Usuarios)
    personajes = relationship(Personajes)
    planetas = relationship(Planetas)
    vehiculos = relationship (Vehiculos)
    starships = relationship(Starships)




    def to_dict(self):
        return {}
    
    



# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
