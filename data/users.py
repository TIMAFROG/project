from sqlalchemy import orm
import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    name = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=True, unique=True)
    n = orm.relationship("Data", back_populates='name_user')

    donate = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("donations.donate"))
    donate_donations = orm.relationship('Donations')

    count_money = sqlalchemy.Column(sqlalchemy.Integer, index=True, nullable=True)
