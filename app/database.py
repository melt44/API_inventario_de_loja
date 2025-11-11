import os
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine 
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from dotenv import load_dotenv

# serve para carregar as variáveis de ambiente definidas no docker-compose
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# A função desse 'echo=True' é para mostrar os comandos SQL no terminal (Gabriel disse que ajuda na hora de debugar)
engine = create_async_engine(DATABASE_URL, echo=True)

# Função para criar as tabelas no banco (caso não existam)
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

# Função para obter uma sessão/conexão com o banco
async def get_session():
    # Cria um 'fazedor' de sessões (nao sei as melhores palavras pra explicar isso)
    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        # O yield entrega a sessão para a função que a pediu e garante que ela será fechada no final, mesmo que de erro.
        try:
            yield session
        finally:
            await session.close()