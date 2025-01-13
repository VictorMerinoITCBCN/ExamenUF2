from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    last_name: str
    email: str
    description: Optional[str]
    course: str
    year: int
    postal_code: Optional[int]
    password: str