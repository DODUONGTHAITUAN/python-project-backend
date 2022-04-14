from black import supports_feature
from sqlalchemy import Integer, String, DateTime, func, Column, Text, ForeignKey
from sqlalchemy.orm import relationship

from src import db
from src.models.allcodes import Allcodes


class Product(db.Model):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    productName = Column(Text, nullable=False)
    image = Column(Text, nullable=False)
    cpu = Column(String(255), nullable=False)
    gpu = Column(String(255), nullable=False)
    productDate = Column(String(255), nullable=False)
    origin = Column(String(255), nullable=False)
    brandID = Column(String(255), ForeignKey(Allcodes.keyMap), nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now())

    """ Define relatioship """
    # brandData = relationship(Allcodes, foreign_keys=[brandID])
    # Constructor:
    def __init__(self, productName, image, cpu, gpu, productDate, origin, brandID):
        self.productName = productName
        self.image = image
        self.cpu = cpu
        self.gpu = gpu
        self.productDate = productDate
        self.origin = origin
        self.brandID = brandID

    def __repr__(self):
        return f"<Product {self.productName}>"
