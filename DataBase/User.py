from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, Date, ForeignKey
from DataBase.Base import Base
import datetime


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(String(32), unique=False, nullable=True)
    family = Column(Boolean, default=False)
    friend = Column(Boolean, default=False)
    reg_date = Column(Date, default=datetime.date.today)
    upd_date = Column(Date, onupdate=datetime.date.today)

    ratings = relationship("Rating", back_populates="user")


class Rating(Base):
    __tablename__ = 'rating'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    rating_value = Column(Integer, nullable=False)
    rated_at = Column(Date, default=datetime.date.today())

    user = relationship("User", back_populates="ratings")
