"""CRUD operations for User.

Password hashing uses the maintained `bcrypt` package directly. We dropped
`passlib`, which is effectively unmaintained and breaks against bcrypt >= 4.1.
"""

import bcrypt
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

# bcrypt operates on the first 72 bytes of the input; we truncate explicitly
# so long passwords hash deterministically instead of being silently cut.
_BCRYPT_MAX_BYTES = 72


def get_password_hash(password: str) -> str:
    pw = password.encode("utf-8")[:_BCRYPT_MAX_BYTES]
    return bcrypt.hashpw(pw, bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    pw = plain_password.encode("utf-8")[:_BCRYPT_MAX_BYTES]
    return bcrypt.checkpw(pw, hashed_password.encode("utf-8"))


def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)  # SQLAlchemy 2.0 identity lookup


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def get_user_by_username(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.password),
        is_active=user.is_active,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, db_user: User, user_update: UserUpdate) -> User:
    data = user_update.model_dump(exclude_unset=True)
    if "password" in data:
        db_user.hashed_password = get_password_hash(data.pop("password"))
    for field, value in data.items():
        setattr(db_user, field, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, db_user: User) -> None:
    db.delete(db_user)
    db.commit()
