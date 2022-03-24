from src import db
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


class Allcode(db.Model):
    __tablename__ = "Allcodes"
    # Define column
    id = Column(Integer, nullable=False, unique=True, autoincrement=True)
    keyMap = Column(String(255), primary_key=True)
    type = Column(String(255), nullable=False)
    value = Column(String(255), nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now())

    # Add Relationship
    users = relationship("User", backref="roleData")

    # Constuctor
    def __init__(self):
        pass

    def __repr__(self):
        return f"<User {self.fullName}>"
