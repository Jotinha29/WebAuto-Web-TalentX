from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()

@router.post('/pedidos')
def fazer_pedido():
    pass

@router.get('/pedidos/{id}')
def exibir_pedido():
    pass

@router.get('/pedidos')
def listar_pedido():
    pass