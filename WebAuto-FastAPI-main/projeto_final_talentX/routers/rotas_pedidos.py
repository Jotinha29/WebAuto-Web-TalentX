

from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schema import Compra



router = APIRouter()

@router.post('/pedidos', status_code= status.HTTP_201_CREATED, response_model= None)
def fazer_pedido():
    pass

@router.get('/pedidos/{id}')
def exibir_pedido():
    pass

@router.get('/pedidos')
def listar_pedido():
    pass