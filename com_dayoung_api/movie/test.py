import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from com_dayoung_api.utils.file_helper import FileReader

class MovieData:
    def __init__(self):
        print(f'baseurl #### {baseurl}')
        self.reader = FileReader()

    def get_crime(self):
        reader = self.reader
        reader.context = os.path.join(baseurl,'data')
        reader.fname = 'kmdb_csv.csv'
        reader.new_file()
        crime = reader.csv_to_dframe()
        print(crime)
        return crime

aaa = MovieData()
aaa.get_crime()