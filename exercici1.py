from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    name: str = Field(max_length=200)
    last_name: str = Field(max_length=200)
    email: str
    description: Optional[str] = Field(max_length=1000)
    course: str = Field(max_length=100)
    year: int = Field(gt=0)
    postal_code: Optional[int] = Field(gt=0)
    password: str = Field(min_length=10)