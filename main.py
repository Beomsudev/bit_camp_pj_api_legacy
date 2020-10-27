from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from com_dayoung_api.ext.db import url, db
from com_dayoung_api.ext.routes import initialize_routes
from com_dayoung_api.resources.user import UserDao
from com_dayoung_api.resources.movie import MovieDao


print('========== 1 ==========')
app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()
with app.app_context():
    print('데이터 DB 삽입')
    count_user = UserDao.count()
    count_movie = MovieDao.count()
    print(f'Users Total Count is {count_user}')
    print(f'Movies Total Count is {count_movie}')

    if count_user == 0:
        UserDao.insert_many()
    elif count_movie == 0:
        MovieDao.insert_many()


# @app.before_first_request
# def create_tables():
#     db.create_all()

initialize_routes(api)