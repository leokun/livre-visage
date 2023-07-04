from dataclasses import dataclass
from uuid import UUID, uuid4

from pydantic import EmailStr



@dataclass
class Login:
    id: UUID = uuid4()
    user_id: UUID
    login: EmailStr
    password: str