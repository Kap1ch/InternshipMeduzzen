import hashlib
import uuid

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.db import Session
from app.db.models import User
from app.schemas.user_schemas import UserSignUp, UserDetailResponse, UserListResponse, GetUser, UserUpdateRequest

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)


async def get_db():
    db = Session()
    try:
        yield db
    finally:
        await db.close()


@user_router.post("/create/", response_model=UserSignUp)
async def create_user(user: UserSignUp, db: Session = Depends(get_db)):
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    user.password = hashed_password

    new_user: User = await User.create(db=db, **user.dict())
    return new_user.to_dict(schema=UserSignUp)


@user_router.get("/{user_id}", response_model=UserDetailResponse)
async def get_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        user: User = await User.get(db=db, obj_id=user_id)
        return user.to_dict(schema=UserDetailResponse)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@user_router.get("/", response_model=UserListResponse)
async def get_all_user(db: Session = Depends(get_db)):
    users = await User.get_all(db=db)
    users_data = [GetUser(**user.to_dict(schema=GetUser)) for user in users]
    return {"user": users_data}


@user_router.delete("/delete/{user_id}")
async def delete_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    await User.delete(db=db, obj_id=user_id)
    return 'User deleted'


@user_router.put("/update/{user_id}", response_model=GetUser)
async def update_user(user_id: uuid.UUID, user_update: UserUpdateRequest, db: Session = Depends(get_db)):
    hashed_password = hashlib.sha256(user_update.password.encode()).hexdigest()
    user_update.password = hashed_password

    try:
        user = await User.get(db=db, obj_id=user_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    updated_user = await user.update(db=db, **user_update.dict())

    return updated_user.to_dict(schema=GetUser)
