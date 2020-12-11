import pymysql

class testdb:
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd="kgj@980219", db = 'project', charset = 'utf8')


    def select_all(self):
        cursor = self.db.cursor()
        sql = 'select * from project.movie'
        cursor.execute(sql)
        result = cursor.fetchall()
        return result