from peewee import *

db = SqliteDatabase('kvest.db')

class BaseModel(Model):
    class Meta:
        databases = db


class User(Model):
    username = CharField()
    join_date = DateField()
    score = int

    class Meta:
        database = db
        table_name = 'User'
        

class Point(Model):
    score = int
    question = CharField()
    right_answer = CharField()
    wrong_answer = CharField()

    class Meta:
        database = db
