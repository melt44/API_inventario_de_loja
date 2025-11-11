from sqlmodel import Field, SQLModel
from typing import Optional

class ItemInventario(SQLModel, table=True):
    # Desse modo, o 'id' será gerenciado pelo bd
    id: Optional[int] = Field(default=None, primary_key=True)
    
    nome: str = Field(index=True) # index=True -> a indexação melhora a velocidade dd busca
    descricao: Optional[str] = None
    preco: float = Field(gt=0)
    quantidade: int = Field(ge=0)
