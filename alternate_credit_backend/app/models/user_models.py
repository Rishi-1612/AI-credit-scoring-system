from sqlalchemy import Column, DateTime, Integer, String, func

from app.db import Base


class User(Base):
    """User account used by customer and manager authentication routes."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    public_user_id = Column(String(36), unique=True, nullable=False, index=True)
    name = Column(String(150), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(32), nullable=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False, default="customer")
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())
