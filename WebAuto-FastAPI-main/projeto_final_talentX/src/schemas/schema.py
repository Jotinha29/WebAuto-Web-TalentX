from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[str] = None
    name: str
    CPF: str
    tel: str

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    cpf: str
    email: str
    telefone: str
    senha: str
    #produtos: List[ProdutoSimples] = []

    class Config:
        orm_mode = True


class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str

    class Config:
        orm_mode = True


class LoginData(BaseModel):
    senha: str
    email: str


class LoginSucesso(BaseModel):
    usuario: UsuarioSimples
    access_token: str
    
class Carro(BaseModel):
    id: Optional[str] = None
    modelo: str
    marca: str
    ano: int
    preco: float 
    
    class Config:
        orm_mode = True
    
class CarroSimples(BaseModel):
    marca: str
    modelo: str
    ano: int
    preco: float 
    
    class Config:
        orm_mode = True
        
class Compra(BaseModel):
    id: Optional[str] = None
    comprador: User
    vendedor: User
    compra: Carro 
    
class Venda(BaseModel):
    id: Optional[str] = None
    vendedor: User
    venda: Carro 