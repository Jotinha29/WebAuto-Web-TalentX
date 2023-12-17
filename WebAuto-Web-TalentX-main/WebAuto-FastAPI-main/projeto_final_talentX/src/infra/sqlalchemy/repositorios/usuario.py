import email
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas import schema
from src.infra.sqlalchemy.models import models


class RepositorioUsuario():

    def __init__(self, session: Session):
        self.session = session


    def criar(self, usuario: schema.Usuario):
        usuario_bd = models.Usuario(nome=usuario.nome,
                                    cpf=usuario.cpf,
                                    telefone=usuario.telefone,
                                    email=usuario.email,
                                    senha=usuario.senha)
        self.session.add(usuario_bd)
        self.session.commit()
        self.session.refresh(usuario_bd)
        return usuario_bd


    def listar(self):
        stmt = select(models.Usuario)
        usuarios = self.session.execute(stmt).scalars().all()
        return usuarios


    def obter_por_email(self, email) -> models.Usuario:
        query = select(models.Usuario).where(
            models.Usuario.email == email)
        return self.session.execute(query).scalars().first()