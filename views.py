import peewee
import models
import datetime

#def init(self):
#    cursor = self.cursor()
    
def select_point(self,rownum,col):
    cursor = self.cursor()
    return cursor.execute('SELECT ' + col +' FROM point WHERE id = ' + str(rownum)).fetchall()
    self.close()
    
def select_user(self,rownum,col):
    cursor = self.cursor()
    return cursor.execute('SELECT ' + col +' FROM user WHERE id = ' + str(rownum)).fetchall()
    self.close()

#def close(self):
#    self.close()

def add_user(self,name,sc):
    cursor = self.cursor()
    #print(sc)
    models.User.create(username = name,join_date = datetime.date.today(),score = sc)
    self.close()


