from src import db
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, Text

from .allcodes import Allcodes
from .product import Product


class DetailProduct(db.Model):
    __tablename__ = "DetailProducts"

    # Define column
    id = Column(Integer, primary_key=True, autoincrement=True)
    contentHTML = Column(Text, nullable=True)
    contentMarkdown = Column(Text, nullable=True)
    simSlots = Column(Integer, nullable=False, default=1)
    osID = Column(String(255), ForeignKey(Allcodes.keyMap))
    batteryText = Column(String(255), nullable=False)
    batteryID = Column(String(255), ForeignKey(Allcodes.keyMap))
    screenText = Column(String(255), nullable=False)
    screenID = Column(String(255), ForeignKey(Allcodes.keyMap))
    brandID = Column(String(255), ForeignKey(Allcodes.keyMap))
    featureID = Column(String(255), ForeignKey(Allcodes.keyMap))

    productID = Column(Integer, ForeignKey(Product.id))

    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now())

    # Constructor
    def __init__(self):
        pass
