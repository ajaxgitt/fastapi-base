from pydantic import BaseModel
from uuid import UUID

class UserBase(BaseModel):
    model_config = {"from_attributes": True}
    username: str

class UserCreate(BaseModel):
    username: str
    email: str


class UserResponse(UserBase):
    id: UUID
