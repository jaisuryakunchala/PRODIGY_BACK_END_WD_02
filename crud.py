from sqlalchemy.orm import Session
from app import models, schemas

# CREATE
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        email=user.email,
        age=user.age
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# READ ALL
def get_users(db: Session):
    return db.query(models.User).all()

# READ BY ID
def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()

# UPDATE
def update_user(db: Session, user_id: str, user: schemas.UserUpdate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None

    if user.name:
        db_user.name = user.name
    if user.email:
        db_user.email = user.email
    if user.age:
        db_user.age = user.age

    db.commit()
    db.refresh(db_user)
    return db_user

# DELETE
def delete_user(db: Session, user_id: str):
    db_user = get_user(db, user_id)
    if not db_user:
        return None

    db.delete(db_user)
    db.commit()
    return db_user
