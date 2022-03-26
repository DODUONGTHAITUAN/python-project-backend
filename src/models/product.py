from src import db
from sqlalchemy import Integer, String, DateTime, func, Column, LargeBinary, Text


class Product(db.Model):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    productName = Column(Text, nullable=False)
    image = Column(LargeBinary, nullable=False)
    cpu = Column(String(255), nullable=False)
    gpu = Column(String(255), nullable=False)
    productDate = Column(String(255), nullable=False)
    origin = Column(String(255), nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now())

    # Constructor:
    def __init__(self):
        pass

    def __repr__(self):
        return f"<Product {self.productName}>"
