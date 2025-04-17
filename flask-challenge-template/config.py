import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'b3be5f02a4ca515eadd92d7fd8da1382f5934131a153403d86b0a34cdd4c1861'
