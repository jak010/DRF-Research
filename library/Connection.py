
from django.db import connection


class dbCursor:
    def __init__(self,sql):
        self.cursor = connection.cursor()
        self.connection = connection
        self.sql = sql

    def get(self):
        try:
            if self.cursor.execute(self.sql):
                return [x[1:6] for x in self.cursor.fetchall()]
            self.cursor.commit()

        finally:
            self.connection.close()
