from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


# class ModalTodict(Base):
#     def to_dict(self):
#         model_dict = dict(self.__dict__)
#         return model_dict



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

    def to_dict(self):
        model_dict = dict(self.__dict__)
        return model_dict

    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")