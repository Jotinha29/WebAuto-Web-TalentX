from sqlalchemy.orm import Session
from sqlalchemy import update, select, delete
from src.schemas import schema
from src.infra.sqlalchemy.models import models

class RepositorioCarro():


    def __init__(self, db: Session):
        self.session = db


    def criar(self, carro: schema.Carro):
        db_carro = models.Carro(
            modelo = carro.modelo,
            marca = carro.marca,
            ano = carro.ano,
            preco = carro.preco,
            km = carro.km,
            local = carro.local,
            cor = carro.cor,
            usuario_id = carro.usuario_id
        )
        
        self.session.add(db_carro)
        self.session.commit()
        self.session.refresh(db_carro)
        return(db_carro)


    def listar(self):
        carros =  self.session.query(models.Carro).all()
        return carros


    def editar(self, id: int, carro: schema.Carro):
        update_stmt = update(models.Carro).where(
            models.Carro.id == id).values(modelo=carro.modelo,
                                            marca=carro.marca,
                                            ano=carro.ano,
                                            preco=carro.preco,
                                            km=carro.km,
                                            local=carro.local,
                                            cor=carro.cor,
                                            )
        self.session.execute(update_stmt)
        self.session.commit()


    def remover(self, id: int):
        delete_stmt = delete(models.Carro).where(
        models.Carro.id == id
    )

        self.session.execute(delete_stmt)
        self.session.commit()