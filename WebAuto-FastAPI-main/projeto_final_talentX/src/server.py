from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schema import Carro, CarroSimples
from src.infra.sqlalchemy.repositorios.carro import RepositorioCarro
from src.infra.sqlalchemy.config.database import get_db, criar_db

criar_db()

app = FastAPI()

@app.post('/add-carro', status_code=status.HTTP_201_CREATED, response_model=CarroSimples)
def criar_carro(carro: Carro, db: Session = Depends(get_db)):
    new_carro = RepositorioCarro(db).criar(carro)
    return new_carro

@app.get('/carros-disponiveis', status_code=status.HTTP_200_OK, response_model=List[CarroSimples])
def listar_carros(db: Session = Depends(get_db)):
    carros = RepositorioCarro(db).listar()
    return carros