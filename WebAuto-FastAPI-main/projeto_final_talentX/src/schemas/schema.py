from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    name: str
    CPF: str
    tel: str
    
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
    compra: Carro 
    
class Venda(BaseModel):
    id: Optional[str] = None
    vendedor: User
    venda: Carro 