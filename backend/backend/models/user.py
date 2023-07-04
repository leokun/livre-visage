from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class User:
    id: UUID = uuid4()
    first_name: str
    last_name: str
