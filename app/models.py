from sqlmodel import Field, SQLModel
from typing import Optional

# SQLModel é ao mesmo tempo um modelo Pydantic e um modelo SQLAlchemy
class ItemInventario(SQLModel, table=True):
    # O 'id' agora será gerenciado pelo banco (Primary Key)
    id: Optional[int] = Field(default=None, primary_key=True)
    
    nome: str = Field(index=True) # index=True melhora a velocidade de busca
    descricao: Optional[str] = None
    preco: float = Field(gt=0)
    quantidade: int = Field(ge=0)

# Não precisamos mais de um modelo de 'Resposta' separado,
# o SQLModel já lida com a criação (sem id) e resposta (com id).