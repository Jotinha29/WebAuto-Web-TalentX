

import dbm
from sqlalchemy.orm import Session
from src.schemas import schema
from src.infra.sqlalchemy.models import models

class RepositorioPedido():

    def __init__(self, db: Session) -> None:
        self.db = db
        pass


    def salvar_pedido(self, pedido: schema.Compra):
        pass


    def buscar_pedido(self, id: int):
        pass


    def carros_comprados_id(self, usuario_id: int):
        pass


    def carros_vendidos_id(self, usuario_id: int):
        pass