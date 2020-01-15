import pymysql


class MysqlUtil(object):
    def __init__(self):
        self.__conn = None
        self.__cursor = None


    def __enter__(self):
        config = {
            'host': 'db',
            'user': 'root',
            'password': 'root',
            'port': 3306,
            'database': 'general',
            'cursorclass':pymysql.cursors.DictCursor
        }
        self.__conn = pymysql.connect(**config)
        self.__cursor = self.__conn.cursor()

        return self


    def __exit__(self, exc_type, exc_value, traceback):
        """ closes connection and rollback on exceptions """
        self.__cursor.close()
        if isinstance(exc_value, Exception):
            self.__conn.rollback()
        else:
            self.__conn.commit()
        self.__conn.close()


    def fetchone(self, sql, params=None):
        self.__cursor.execute(sql, params)
        return self.__cursor.fetchone()


    def fetch(self, sql, params=None):
        self.__cursor.execute(sql, params)
        return self.__cursor.fetchall()


    def execute_statements(self, sps):
        """ execute several statements in array, return results 
            sps: [[sql1, params1], [sql1]]
        """
        for sp in sps:
            sql = sp[0]
            params = sp[1] if len(sp) > 1 else None
            self.__cursor.execute(sql, params)

        return self.__cursor.fetchall()
    

    def execute(self, sql, params=None):
        self.__cursor.execute(sql, params)
        return