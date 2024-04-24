import uuid

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    user_name: str
    first_name: str
    last_name: str


class GetUser(UserBase):
    id: uuid.UUID
    phone_number: str


class UserSignIn(BaseModel):
    user_name: str
    password: str


class UserSignUp(UserBase):
    password: str
    phone_number: str


class UserUpdateRequest(UserBase):
    phone_number: str
    password: str


class UserListResponse(BaseModel):
    user: list[GetUser]


class UserDetailResponse(GetUser):
    id: uuid.UUID
    is_active: bool
