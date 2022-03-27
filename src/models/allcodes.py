from src import db
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


class Allcodes(db.Model):
    __tablename__ = "Allcodes"
    # Define column
    id = Column(Integer, nullable=False, unique=True, autoincrement=True)
    keyMap = Column(String(255), primary_key=True)
    type = Column(String(255), nullable=False)
    value = Column(String(255), nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now())

    # gender_allcodes = relationship(
    #     "User", foreign_keys="[User.genderID]", back_populates="gender_user"
    # )
    # role_allcodes = relationship(
    #     "User", foreign_keys="[User.roleID]", back_populates="role_user"
    # )

    # Add Relationship
    #  users = relationship("User", backref="roleData")

    # Constuctor
    def __init__(self):
        pass

    def __repr__(self):
        return f"<Allcodes {self.fullName}>"
