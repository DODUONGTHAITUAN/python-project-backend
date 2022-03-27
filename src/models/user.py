from src import db
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from .allcodes import Allcodes


class User(db.Model):

    __tablename__ = "User"
    # Define column
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullName = Column(String(255), nullable=False)
    genderID = Column(String(255), ForeignKey(Allcodes.keyMap))
    address = Column(String(255), nullable=False)
    phonenumber = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    roleID = Column(String(255), ForeignKey(Allcodes.keyMap))
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now())

    """Cái relationship này quan trọng, bảng User tham  chiếu tới bảng Allcodes nên hai dòng dưới chỉ có ở bảng User, bảng Allcodes sẽ không ghi gì cả"""
    genderData = relationship(Allcodes, foreign_keys=[genderID])
    roleData = relationship(Allcodes, foreign_keys=[roleID])

    # gender_user = relationship(
    #     Allcodes, foreign_keys=[genderID], back_populates="gender_allcodes"
    # )
    # role_user = relationship(
    #     Allcodes, foreign_keys=[roleID], back_populates="role_allcodes"
    # )
    # # Define relationship
    # orders = relationship("Order", backref="orderData")

    # Constuctor
    def __init__(
        self, fullName, genderID, address, phonenumber, email, password, roleID
    ):
        self.fullName = fullName
        self.genderID = genderID
        self.address = address
        self.phonenumber = phonenumber
        self.email = email
        self.password = password
        self.roleID = roleID

    """Display info of instance"""

    def __repr__(self):
        return f"<User {self.fullName}>"
