from peewee import *

db1 = SqliteDatabase('kvest_user.db')
db2 = SqliteDatabase('kvest_point.db')

class User(Model):
    username = CharField()
    join_date = DateField()
    score = int

    class Meta:
        database = db1
        

class Point(Model):
    score = int
    question = CharField()
    right_answer = CharField()
    wrong_answer = CharField()

    class Meta:
        database = db2
