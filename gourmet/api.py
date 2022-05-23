from typing import List, Optional

from fastapi import FastAPI, Response, status

from gourmet.core import get_users_from_database
from gourmet.database import get_session
from gourmet.models import Users
from gourmet.serializers import UsersIn, UsersOut

api = FastAPI(title='gourmet')


@api.get('/users', response_model=List[UsersOut])
async def list_users(style: Optional[str] = None):
    """Lists users from the database"""
    users = get_users_from_database(style)
    return users


@api.post('/users', response_model=UsersOut)
async def add_users(users_in: UsersIn, response: Response):
    users = Users(**users_in.dict())
    with get_session() as session:
        session.add(users)
        session.commit()
        session.refresh(users)

    response.status_code = status.HTTP_201_CREATED
    return users
