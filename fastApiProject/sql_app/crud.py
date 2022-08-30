from sqlalchemy.orm import Session
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import os, time, random

from . import models, schemas

executor = ThreadPoolExecutor(max_workers=3)


def task(n):
    print('%s is runing' % os.getpid())
    time.sleep(random.randint(1, 3))
    return n ** 2


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):




    # return db.query(models.User).offset(skip).limit(limit).all()

    # for i in range(11):
    #     future=executor.submit(task,i)

    res = executor.map(task, range(1, 12))  # map取代了for+submit
    executor.shutdown()
    for r in res:
        print(r)
    # dd = result.to_json()


    return res
    # return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item