import pymysql.cursors
#from . import connector

def category(categoryID):
    query = "SELECT category FROM categories WHERE categoryID = %s"

