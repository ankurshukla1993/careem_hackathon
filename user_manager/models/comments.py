from sqlalchemy import Column, Integer, ForeignKey, String

from user_manager.main import Base


class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user_info.id"))
    ride_id = Column(Integer)
    comment = Column(String)
