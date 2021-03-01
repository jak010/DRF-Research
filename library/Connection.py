
from django.db import connection


class dbCursor:
    def __init__(self,sql,_max=None):
        self.con = connection
        self.sql = sql

    def get(self, _max_list=None):

        _max_list = _max_list if _max_list is not None else 5 # defualt: 5

        with self.con.cursor() as cursor:
            cursor.execute(self.sql)
            # DB Column Name 매핑
            columns = [col[0] for col in cursor.description]
            self.con.commit()
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ][0:_max_list]
