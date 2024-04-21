from sqlalchemy import orm
import sqlalchemy
from .db_session import SqlAlchemyBase


class Donations(SqlAlchemyBase):
    __tablename__ = 'donations'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    info = sqlalchemy.Column(sqlalchemy.String, unique=True)

    money = sqlalchemy.Column(sqlalchemy.Integer, index=True)

    donate = sqlalchemy.Column(sqlalchemy.String, nullable=False, default='Игрок')
    d = orm.relationship("User", back_populates='donate_donations')
    
