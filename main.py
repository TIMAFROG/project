from flask import Flask
from data.users import User
from data.donations import Donations
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():

    db_session.global_init("db/db_proekt.db")

    # app.run()


if __name__ == '__main__':
    main()
