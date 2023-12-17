from pydantic import BaseModel
from typing import Optional, List

class CarroSimples(BaseModel):
    id: Optional[int] = None
    marca: str
    modelo: str
    ano: int
    preco: float 
    
    class Config:
        orm_mode = True

class Carro(BaseModel):
    id: Optional[str] = None
    modelo: str
    marca: str
    ano: int
    preco: float 
    km: float
    local: str
    cor: str
    usuario_id: Optional[int]
    #usuario = Optional[UsuarioSimples]
    
    class Config:
        orm_mode = True
    
        
class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    cpf: str
    telefone: str
    email: str
    senha: str
    produtos: List[CarroSimples] = []

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
    

class Compra(BaseModel):
    id: Optional[str] = None
    comprador: Usuario
    vendedor: Usuario
    compra: Carro 
    
class Venda(BaseModel):
    id: Optional[str] = None
    vendedor: Usuario
    venda: Carro 