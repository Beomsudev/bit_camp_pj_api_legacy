from com_dayoung_api.ext.db import db
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from com_dayoung_api.movie.service import MovieService

from com_dayoung_api.utils.file_helper import FileReader

config = {
    'user' : 'root',
    'password' : 'root',
    'host': '127.0.0.1',
    'port' : '3306',
    'database' : 'dayoungdb'
}
charset = {'utf8':'utf8'}
url = f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}?charset=utf8"
engine = create_engine(url)

class MovieDto(db.Model):
    
    __tablename__ = 'movies'
    __table_args__= {'mysql_collate':'utf8_general_ci'}

    id : str = db.Column(db.String(30), primary_key = True, index = True)
    title : str = db.Column(db.String(30))
    genre : str = db.Column(db.String(30))
    country : str = db.Column(db.String(30))
    year : str = db.Column(db.String(4))
    company : str = db.Column(db.String(30))
    director : str = db.Column(db.String(30))
    actor : str = db.Column(db.String(30))
    date : str = db.Column(db.String(30))
    running_time : str = db.Column(db.String(30))
    keyword : str = db.Column(db.String(30))
    plot : str = db.Column(db.String(30))

    def __init__(self, id, title, genre, country, year, compacompanyny, director, actor, date, running_time, keyword, plot):
        self.id = id
        self.title = title
        self.genre = genre
        self.country = country
        self.year = year
        self.company = company
        self.director = director
        self.actor = actor
        self.date = date
        self.running_time = running_time
        self.keyword = keyword
        self.plot = plot


    def __repr__(self):
        return f'Movie(id=\'{self.id}\',\
            title=\'{self.title}\',\
            genre=\'{self.genre}\',\
            country=\'{self.country}\',\
            year=\'{self.year}\',\
            company=\'{self.company}\',\
            director=\'{self.director}\',\
            actor=\'{self.actor}\',\
            date=\'{self.date}\',\
            running_time=\'{self.running_time}\',\
            keyword=\'{self.keyword}\',\
            plot=\'{self.plot}\',)'

    @property
    def json(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'genre' : self.genre,
            'country' : self.country,
            'year' : self.year,
            'company' : self.company,
            'director' : self.director,
            'actor' : self.actor,
            'date' : self.date,
            'running_time' : self.running_time,
            'keyword' : self.keyword,
            'plot' : self.plot
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

service = MovieService()
Session = sessionmaker(bind=engine)
s = Session()
df = service.hook()
print(df.head())
s.bulk_insert_mappings(MovieDto, df.to_dict(orient="records"))
s.commit()
s.close()
