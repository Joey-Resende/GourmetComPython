from sqlmodel import Field, SQLModel
from datetime import datetime
from typing import Optional


class Users(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    date: datetime = Field(default_factory=datetime.now)
    name: str
    user: str
    pswd: str
    cpf: str
    email: str
    birth: str
    phone: str
    address: str


class Products(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    date: datetime = Field(default_factory=datetime.now)
    type_product: str
    name: str
    isbn: str
    description: str
    price: str
    quant: str
