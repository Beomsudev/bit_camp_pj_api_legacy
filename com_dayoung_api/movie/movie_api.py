from flask_restful import Resource
from flask import Response, jsonify
from com_dayoung_api.movie.movie_dao import MovieDao

class MovieApi(Resource):

    def __init__(self):
        self.dao = MovieDao()

    def get(self):
       movies = self.dao.select_movies()
       return jsonify(movies[0])