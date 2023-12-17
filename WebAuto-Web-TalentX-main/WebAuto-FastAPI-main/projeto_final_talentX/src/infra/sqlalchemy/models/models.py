from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

class Carro(Base):
    __tablename__ = 'carro'
    
    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String)
    marca = Column(String)
    ano = Column(Integer)
    preco = Column(Float)
    km = Column(Float)
    local = Column(String)
    cor = Column (String)
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='fk_usuario'))

    usuario = relationship('Usuario', back_populates='carros')
    
class Usuario(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cpf = Column(String)
    telefone = Column(String)
    email = Column(String)
    senha = Column(String)
    
    carros = relationship('Carro', back_populates= 'usuario')


    #produtos = relationship('Produto', back_populates='usuario')
    #pedidos = relationship('Pedido', back_populates='usuario')
