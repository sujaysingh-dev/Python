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
t4=f.getvalue("t4")
t5=f.getvalue("t5")
t6=f.getvalue("t6")
b=f.getvalue("b")
try:
  if(b=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['product']
   a=0
   for x in collection.find({}):
     if(x['prd_id']==t1):
       a=1
       break
   if(a==1):
     print("<script>alert('Customer id already exist....')</script>")
     print("<script>window.open('Customers.html','_self')</script>")
   else:
    insert1={'prd_id':t1,'prd_nm':t2,'diss':t3,'stn_cost':t4,'list_price':t5,'cat_id':t6}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")

  if(b=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['product']
   collection.update_many({'prd_id':t1},{'$set':{'prd_nm':t2,'diss':t3,'stn_cost':t4,'list_price':t5,'cat_id':t6}})
   print("<script>alert('Record Update....')</script>")

  if(b=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['product']
   delete1={'prd_id':t1}
   collection.delete_many(delete1)
   print("<script>alert('Record Deleted...')</script>")


  if(b=="AllSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['product']
   print("<body bgcolor=pink><center><table border=2 bgcolor=grey><tr><th>product Id</th><th>product Name</th><th>Discription</th><th>Standard Cost</th><th>List Price</th><th>Category_Id</th></tr><center>")
   for x in collection.find({}):
    print("<tr><th>",x["prd_id"],"</th>","<th>",x["prd_nm"],"</th>","<th>",x["diss"],"</th>","<th>",x["stn_cost"],"</th>","<th>",x["list_price"],"</th>","<th>",x["cat_id"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")


  if(b=="PSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['product']
   print("<body bgcolor=pink><center><table border=2 bgcolor=grey><tr><th>product Id</th><th>product Name</th><th>Discription</th><th>Standard Cost</th><th>List Price</th><th>Category_Id</th></tr><center>")
   for x in collection.find({'prd_id':t1}):
    print("<tr><th>",x["prd_id"],"</th>","<th>",x["prd_nm"],"</th>","<th>",x["diss"],"</th>","<th>",x["stn_cost"],"</th>","<th>",x["list_price"],"</th>","<th>",x["cat_id"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")

except Exception:
        traceback.print_exc()

