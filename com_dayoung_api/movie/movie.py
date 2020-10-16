from com_dayoung_api.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DECIMAL, VARCHAR, LONGTEXT
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from com_dayoung_api.utils.file_helper import FileReader

class Movie(Base):
    __tablename__ = "movies"
    __table_args__ = {'mysql_collate':'utf8_general_ci'}

    id = Column(Integer, primary_key=True, index=True)
    movie_name = Column(VARCHAR(30))
    genre = Column(VARCHAR(30))
    country = Column(VARCHAR(30))
    year = Column(DECIMAL(4))
    company = Column(VARCHAR(30))
    director = Column(VARCHAR(30))
    actor = Column(VARCHAR(30))
    keyword = Column(VARCHAR(30))

    def __repr__(self):
        return f'Movie(id=\'{self.id}\',\
            movie_name=\'{self.movie_name}\',\
            genre=\'{self.genre}\',\
            country=\'{self.country}\',\
            year=\'{self.year}\',\
            company=\'{self.company}\',\
            director=\'{self.director}\',\
            actor=\'{self.actor}\',\
            keyword=\'{self.keyword}\',)'

class MovieData:
    def __init__(self):
        print(f'baseurl #### {baseurl}')
        self.reader = FileReader()

        
engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/mariadb?charset=utf8', encoding='utf8', echo=True)
# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.add(Movie(movie_name='여호',
                    genre='드라마', 
                    country='영국', 
                    year='1950', 
                    company='Vanguard,London Productions', 
                    director='마이클 파웰,에머릭 프레스버거', 
                    actor='마이클 파웰,에머릭 프레스버거',
                    keyword='짚시,여우,삼각관계'
))
query = session.query(Movie).filter((Movie.movie_name == '여호'))
print(query)
for i in query:
    print(i)
session.commit()

