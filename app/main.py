from fastapi import FastAPI, HTTPException, status, Depends
from sqlmodel import SQLModel, select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from contextlib import asynccontextmanager

from .database import create_db_and_tables, get_session
from models import ItemInventario
# Criação de um "gerenciador de contexto" para o ciclo de vida da API
@asynccontextmanager
async def lifespan(app: FastAPI):
    # O que vai rodar ANTES da API iniciar (antigo 'startup')
    print("Iniciando... Criando tabelas se necessário.")
    await create_db_and_tables()

    yield
    
    # É o que vai rodar DEPOIS que a API terminar ('shutdown')
    print("Finalizando...")

app = FastAPI(
    title="API de Controle de Inventário com SQLModel",
    version="2.0.0",
    lifespan=lifespan 
)

# AinNda vou documentar esses métodos

@app.post("/itens/", 
          response_model=ItemInventario, 
          status_code=status.HTTP_201_CREATED,
          tags=["Itens"])
async def adicionar_item(item: ItemInventario, 
                         session: AsyncSession = Depends(get_session)):
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item

@app.get("/itens/", 
         response_model=List[ItemInventario],
         tags=["Itens"])
async def listar_itens(session: AsyncSession = Depends(get_session)):
    query = select(ItemInventario)
    resultado = await session.execute(query)
    itens = resultado.scalars().all()
    return itens

@app.get("/itens/{item_id}", 
         response_model=ItemInventario,
         tags=["Itens"])
async def buscar_item(item_id: int, 
                      session: AsyncSession = Depends(get_session)):
    item = await session.get(ItemInventario, item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Item não encontrado"
        )
    return item

@app.put("/itens/{item_id}", 
         response_model=ItemInventario,
         tags=["Itens"])
async def atualizar_item(item_id: int, 
                         item_atualizado: ItemInventario, 
                         session: AsyncSession = Depends(get_session)):
    
    item_db = await session.get(ItemInventario, item_id)
    if not item_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Item não encontrado"
        )
    
    dados_item = item_atualizado.model_dump(exclude_unset=True)
    for key, value in dados_item.items():
        setattr(item_db, key, value)
    
    session.add(item_db)
    await session.commit()
    await session.refresh(item_db)
    return item_db

@app.delete("/itens/{item_id}", 
            status_code=status.HTTP_204_NO_CONTENT,
            tags=["Itens"])
async def remover_item(item_id: int, 
                       session: AsyncSession = Depends(get_session)):
    
    item = await session.get(ItemInventario, item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Item não encontrado"
        )
    
    await session.delete(item)
    await session.commit()
    return

# fui pedir ajuda pra IA e ela cagou tudo entao tive que refatorar boa parte
