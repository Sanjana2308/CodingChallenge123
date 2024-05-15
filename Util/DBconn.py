import pyodbc
from Util.DBUtil import PropertyUtil


# When new object -> new connection
class DBConnection:
    def __init__(self):
        conn_str = PropertyUtil.get_DBconn()
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()


# con1 = DBConnection() # new connection
# con2 = DBConnection() # new connection