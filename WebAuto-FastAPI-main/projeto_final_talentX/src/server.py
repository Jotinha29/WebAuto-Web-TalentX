from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schema import Carro, CarroSimples, Usuario
from src.infra.sqlalchemy.repositorios.carro import RepositorioCarro
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db, criar_db

#criar_db()

app = FastAPI()

#CARRO

@app.post('/add-carro', status_code=status.HTTP_201_CREATED, response_model=CarroSimples)
def criar_carro(carro: Carro, db: Session = Depends(get_db)):
    new_carro = RepositorioCarro(db).criar(carro)
    return new_carro

@app.get('/carros-disponiveis', status_code=status.HTTP_200_OK, response_model=List[CarroSimples])
def listar_carros(db: Session = Depends(get_db)):
    carros = RepositorioCarro(db).listar()
    return carros

@app.put('/carros/{id}', response_model=CarroSimples)
def atualizar_carros(id: int, carro: Carro, session: Session = Depends(get_db)):
    RepositorioCarro(session).editar(id, carro)
    #carro.id = id
    return carro

@app.delete('/carros/{id}')
def remover_carro(id: int, session: Session = Depends(get_db)):
    RepositorioCarro(session).remover(id)
    return {"mensagem": "carro removido!"}

#USUARIO

@app.post('/cadastro', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def cadastrar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@app.get('/usuarios', response_model=List[Usuario])
def listar_usuario(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios


