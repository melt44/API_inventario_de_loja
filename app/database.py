import os
from sqlmodel import SQLModel
# ESTA É A LINHA CORRIGIDA:
from sqlalchemy.ext.asyncio import create_async_engine 
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from dotenv import load_dotenv

# Carrega as variáveis de ambiente (do docker-compose)
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Criamos o "motor" (engine) assíncrono
# O 'echo=True' é ótimo para debug, pois mostra os comandos SQL no terminal
engine = create_async_engine(DATABASE_URL, echo=True)

# Função para criar as tabelas no banco (se não existirem)
async def create_db_and_tables():
    async with engine.begin() as conn:
        # 'metadata.create_all' cria as tabelas
        await conn.run_sync(SQLModel.metadata.create_all)

# Função para obter uma sessão (conexão) com o banco
async def get_session():
    # Cria uma fábrica de sessões
    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        # 'yield' entrega a sessão para a função que a pediu
        # e garante que ela será fechada no final, mesmo se der erro.
        try:
            yield session
        finally:
            await session.close()