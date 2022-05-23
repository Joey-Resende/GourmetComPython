from sqlmodel import Field, SQLModel
from datetime import datetime


class Customers(SQLModel, table=True):
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
