from sqlalchemy import Column, Integer, String, Boolean, Float

from user_manager.main import Base


class User(Base):
    __tablename__ = 'user_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    country = Column(String)
    phone_number = Column(String)
    email_address = Column(String)
    password = Column(String)
    type = Column(String)
    rating = Column(Float)