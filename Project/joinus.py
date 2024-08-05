#!C:/Users/T.YADAV/AppData/Local/Programs/Python/Python311/python
print("Content-Type:text/html")
print()
from abc import update_abstractmethods
import cgi
import traceback
from turtle import update
from pymongo import MongoClient
import pymongo
f=cgi.FieldStorage()
t1=f.getvalue("t1")
t2=f.getvalue("t2")
t3=f.getvalue("t3")
b1=f.getvalue("b")
try:
     if(b1=="Submit"):
          client=pymongo.MongoClient("mongodb://localhost:27017/")
          db=client['inventory']
          collection=db['joinus']
          insert1={'fullname':t1,'gender':t2,'dateofbirth':t3}
          collection.insert_one(insert1)
          print("<script>alert('Send Request Successfully ....')</script>")
          print("<script>window.open('Project.html')</script>")
          
except Exception:
        traceback.print_exc()

