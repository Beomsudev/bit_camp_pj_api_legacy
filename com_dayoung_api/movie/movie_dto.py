from com_dayoung_api.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DECIMAL, VARCHAR, LONGTEXT

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from com_dayoung_api.utils.file_helper import FileReader

class MovieDto:
    def __init__(self):
        ...

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

    # def __init__(self):
    #     print(f'baseurl #### {baseurl}')
    #     self.reader = FileReader()

    # def hook(self):
    #     data = self.get_data()
    #     self.data_to_list(data)
        
    # def get_data(self):
    #     reader = self.reader
    #     reader.context = os.path.join(baseurl,'data')
    #     reader.fname = 'kmdb_csv.csv'
    #     reader.new_file()
    #     data = reader.csv_to_dframe_euc_kr()
    #     print(data)
    #     return data

    # def data_to_list(self, data):
    #     sess = {}
    #     feature = ['movie_name', 'genre', 'country', 'year', 'company', 'director', 'actor', 'keyword']
    #     mylist1 = []
    #     mylist2 = []
    #     mylist3 = []

    #     for i in data['movie_name']:
    #         mylist1.append((feature[0], i))
    #     for i in data['genre']:
    #         mylist2.append((feature[1], i))
    #     for i in data['country']:
    #         mylist3.append((feature[2], i))

    #     print('*'*30)
    #     print(mylist1)
    #     print(mylist2)
    #     print(mylist3)

    #     return mylist1, mylist2, mylist3

    # def __repr__(self):
    #     return f'Movie(id=\'{self.id}\',\
    #         movie_name=\'{self.movie_name}\',\
    #         genre=\'{self.genre}\',\
    #         country=\'{self.country}\',\
    #         year=\'{self.year}\',\
    #         company=\'{self.company}\',\
    #         director=\'{self.director}\',\
    #         actor=\'{self.actor}\',\
    #         keyword=\'{self.keyword}\',)'

engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/dayoungdb?charset=utf8', encoding='utf8', echo=True)
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

# if __name__ == "__main__":
#     movie = Movie()
#     # movie.hook()

