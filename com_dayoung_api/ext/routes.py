from com_dayoung_api.movie.movie_api import MovieApi
def initialize_routes(api):
    api.add_resource(MovieApi, '/api/movies')