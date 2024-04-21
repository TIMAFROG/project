from sqlalchemy import orm
import sqlalchemy
from .db_session import SqlAlchemyBase


class Data(SqlAlchemyBase):
    __tablename__ = 'data'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    password = sqlalchemy.Column(sqlalchemy.String, unique=True)

    email = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    telephone = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    name = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.name"))
    name_user = orm.relationship('User')
