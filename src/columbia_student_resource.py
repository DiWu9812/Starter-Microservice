import pymysql

# import os


class ColumbiaStudentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        # usr = os.environ.get("diwu")
        # pw = os.environ.get("dw3013")
        # h = os.environ.get("localhost")
        usr = 'admin'
        pw = '20176098wd'
        h = 'hw1-dw3013.c4gryhcdew19.us-east-1.rds.amazonaws.com'
        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM f22_databases.columbia_students where guid=%s";
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

