from src import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    ForeignKey,
    LargeBinary,
)

from .product import Product
from .allcodes import Allcodes


class Option(db.Model):
    __tablename__ = "Option"
    id = Column(Integer, primary_key=True, autoincrement=True)
    productID = Column(Integer, ForeignKey(Product.id))
    ram = Column(String(255), nullable=False)
    rom = Column(String(255), nullable=False)
    price = Column(String(255), nullable=False)
    image = Column(LargeBinary, nullable=True)
    colorID = Column(String(255), ForeignKey(Allcodes.keyMap))
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self):
        pass
