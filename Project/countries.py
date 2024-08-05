#!C:/Users/T.YADAV/AppData/Local/Programs/Python/Python311/python
print("Content-Type:text/html")
print()
import cgi
import traceback
from turtle import update
from pymongo import MongoClient
import pymongo
f=cgi.FieldStorage()
t1=f.getvalue("t1")
t2=f.getvalue("t2")
t3=f.getvalue("t3")
b=f.getvalue("b")
try:
  if(b=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['coutries']
   a=0
   for x in collection.find({}):
     if(x['cnt_id']==t1):
       a=1
       break
   if(a==1):
     print("<script>alert('Customer id already exist....')</script>")
     print("<script>window.open('Customers.html','_self')</script>")
   else:
    insert1={'cnt_id':t1,'cnt_nm':t2,'rgn_id':t3}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")

  if(b=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['coutries']
   collection.update_many({'cnt_id':t1},{'$set':{'cnt_nm':t2,'rgn_id':t3}})
   print("<script>alert('Record Update....')</script>")

  if(b=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['coutries']
   delete1={'cnt_id':t1}
   collection.delete_many(delete1)
   print("<script>alert('Record Deleted...')</script>")


  if(b=="AllSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['coutries']
   print("<body bgcolor=pink><center><table border=2 bgcolor=grey><tr><th>Country Id</th><th>Country Name</th><th>Region ID</th></tr><center>")
   for x in collection.find({}):
    print("<tr><th>",x["cnt_id"],"</th>","<th>",x["cnt_nm"],"</th>","<th>",x["rgn_id"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")


  if(b=="PSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['coutries']
   print("<body bgcolor=pink><center><table border=2 bgcolor=grey><tr><th>Country Id</th><th>Country Name</th><th>Region ID</th></tr><center>")
   for x in collection.find({'cnt_id':t1}):
    print("<tr><th>",x["cnt_id"],"</th>","<th>",x["cnt_nm"],"</th>","<th>",x["rgn_id"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")

except Exception:
        traceback.print_exc()

