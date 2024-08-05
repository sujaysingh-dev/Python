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
   collection=db['inventories']
   a=0
   for x in collection.find({}):
     if(x['prd_id']==t1):
       a=1
       break
   if(a==1):
     print("<script>alert('Customer id already exist....')</script>")
     print("<script>window.open('Customers.html','_self')</script>")
   else:
    insert1={'prd_id':t1,'wareh':t2,'qnt':t3}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")

  if(b=="Update"):
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    db=client['inventory']
    collection=db['inventories']
    collection.update_many({'prd_id':t1},{'$set':{'wareh':t2,'qnt':t3}})
    print("<script>alert('Record Update....')</script>")

  if(b=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['inventories']
   delete1={'prd_id':t1}
   collection.delete_many(delete1)
   print("<script>alert('Record Deleted...')</script>")


  if(b=="AllSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['inventories']
   print("<body bgcolor=pink><center><table border=2 bgcolor=grey><tr><th>Product Id</th><th>Warehouse Id</th><th>Quntity</th></tr><center>")
   for x in collection.find({}):
    print("<tr><th>",x["prd_id"],"</th>","<th>",x["wareh"],"</th>","<th>",x["qnt"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")


  if(b=="PSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['inventories']
   print("<body bgcolor=pink><center><table border=2 bgcolor=grey><tr><th>Product Id</th><th>Warehouse Id</th><th>Quntity</th></tr><center>")
   for x in collection.find({'prd_id':t1}):
    print("<tr><th>",x["prd_id"],"</th>","<th>",x["wareh"],"</th>","<th>",x["qnt"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")

except Exception:
        traceback.print_exc()

