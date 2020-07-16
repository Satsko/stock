import sqlite3


class views:
    def __init1__(self, database1):
        self.connection = sqlite3.connect(database1)
        self.cursor = self.connection.cursor()

    def select_single1(self, rownum):
        with self.connection:
            return self.cursor.execute('SELECT * FROM kvest_user WHERE id = ?', (rownum,)).fetchall()[0]
          

    def close1(self):
        self.connection.close()


    def __init2__(self, database2):
        self.connection = sqlite3.connect(database2)
        self.cursor = self.connection.cursor()

    def select_single2(self, rownum):
        with self.connection:
            return self.cursor.execute('SELECT * FROM kvest_point WHERE id = ?', (rownum,)).fetchall()[0]

    def count_rows2(self):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM kvest_point').fetchall()
            return len(result)

    def close2(self):
        self.connection.close()
