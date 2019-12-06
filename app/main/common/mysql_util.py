import mysql.connector


class MysqlUtil(object):
    def __init__(self):
        """ Empty init """
        self.__conn = None
        self.__cursor = None


    def __enter__(self):
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db',
            'port': '3306',
            'database': 'store'
        }
        self.__conn = mysql.connector.connect(**config)
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


    def execute_query(self, sql, params=None):
        """ take in SQL, execute query and return results """
        self.__cursor.execute(sql, params)
        return self.rows_to_dict_list()


    def rows_to_dict_list(self):
        """ converts row object to list """
        columns = [i[0] for i in self.__cursor.description]
        return [dict(list(zip(columns, row))) for row in self.__cursor]
