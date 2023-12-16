from sqlalchemy import Column, Integer, String, Float
from src.infra.sqlalchemy.config.database import Base

class Carro(Base):
    __tablename__ = 'Carro'
    
    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String)
    marca = Column(String)
    ano = Column(Integer)
    preco = Column(Float)
    
class User(Base):
    __tablename__ = 'User'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    CPF = Column(String)
    tel = Column(String)
    
