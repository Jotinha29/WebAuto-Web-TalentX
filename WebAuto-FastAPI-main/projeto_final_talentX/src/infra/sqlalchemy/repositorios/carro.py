from sqlalchemy.orm import Session
from sqlalchemy import select
from src.schemas import schema
from src.infra.sqlalchemy.models import models

class RepositorioCarro():
    
    def __init__(self, db: Session):
        self.db = db

    def criar(self, carro: schema.Carro):
        db_carro = models.Carro(
            modelo = carro.modelo,
            marca = carro.marca,
            ano = carro.ano,
            preco = carro.preco
        )
        
        self.db.add(db_carro)
        self.db.commit()
        self.db.refresh(db_carro)
        return(db_carro)
    
    def listar(self):
        carros =  self.db.query(models.Carro).all()
        return carros
    
    def obter(self):
        pass
    
    def remover(self):
        pass