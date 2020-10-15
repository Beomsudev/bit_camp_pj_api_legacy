from com_dayoung_api.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DECIMAL, VARCHAR, LONGTEXT

class Article(Base):
    __tablename__ = "articles"
    __table_args__ = {'mysql_collate':'utf8_eneral_ci'}

    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey("user.id"))
    movie = Column(Integer, ForeignKey("movie.id"))
    title = Column(VARCHAR(30))
    content = Column(VARCHAR(30))

    def __repr__(self):
        return f'Movie(id=\'{self.id}\',\
            user=\'{self.user}\',\
            movie=\'{self.movie}\',\
            title=\'{self.title}\',\
            content=\'{self.content}\',)'

engine = create_engine('mysql+mysqlconnector://root:1347@127.0.0.1/mariadb?charset=utf8', encoding='utf8', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
