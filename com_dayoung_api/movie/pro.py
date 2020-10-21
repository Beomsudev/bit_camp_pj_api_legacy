import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from com_dayoung_api.utils.file_helper import FileReader
"""
title:영화제목
genre:장르
country:제작국가
year:제작년도
company:제작회사
director:감독
actor:배우
date:개봉일
running_time:상영시간
keyword:키워드
plot:줄거리
"""
class MoviePro:
    def __init__(self):
        print(f'baseurl #### {baseurl}')
        self.reader = FileReader()

    def hook(self):
        data = self.get_data()
        

    def get_data(self):
        reader = self.reader
        reader.context = os.path.join(baseurl,'data')
        reader.fname = 'kmdb_csv_modify4.csv'
        reader.new_file()
        data = reader.csv_to_dframe_euc_kr()
        print(data)
        return data

if __name__ == "__main__":
    pro = MoviePro()
    pro.hook()