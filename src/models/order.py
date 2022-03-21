from src import db
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, Float
from .user import User
from .allcodes import Allcode


class Order(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    userID = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"))
    statusID = Column(String(255), ForeignKey(Allcode.keyMap, ondelete="CASCADE"))
    orderDate = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=True
    )
    totalPrice = Column(Float, nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now())
