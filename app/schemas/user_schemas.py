import uuid
from typing import List

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    user_name: str
    first_name: str
    last_name: str


class UserSignIn(BaseModel):
    user_name: str
    password: str


class UserSignUp(UserBase):
    password: str
    phone_number: str


class UserUpdateRequest(UserBase):
    phone_number: str
    password: str


class UserListResponse(UserBase):
    user: List[UserBase]


class UserDetailResponse(UserBase):
    id: uuid.UUID
    is_active: bool
