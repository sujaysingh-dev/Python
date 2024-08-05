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
b=f.getvalue("b")
try:
  if(b=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['customers']
   a=0
   for x in collection.find({}):
     if(x['cus_id']==t1):
       a=1
       break
   if(a==1):
     print("<script>alert('Customer id already exist....')</script>")
     print("<script>window.open('Customers.html','_self')</script>")
   else:
     insert1={'cus_id':t1,'cus_nm':t2,'cadd':t3,'cweb':t4,'climit':t5}
     collection.insert_one(insert1)
     print("<script>alert('Record Saved...')</script>")
     print("<script>window.open('Customers.html','_self')</script>")

  if(b=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['customers']
   collection.update_many({'cus_id':t1},{'$set':{'cus_nm':t2,'cadd':t3,'cweb':t4,'climit':t5}})
   print("<script>alert('Record Update....')</script>")

  if(b=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['customers']
   delete1={'cus_id':t1}
   collection.delete_many(delete1)
   print("<script>alert('Record Deleted...')</script>")


  if(b=="AllSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['customers']
   print("<body bgcolor=pink><center><table border=2 bgcolor=grey><tr><th>Customer Id</th><th>Customer Name</th><th>Customer Address</th><th>Customer Web</th><th>Credit Limit</th></tr><center>")
   for x in collection.find({}):
    print("<tr><th>",x["cus_id"],"</th>","<th>",x["cus_nm"],"</th>","<th>",x["cadd"],"</th>","<th>",x["cweb"],"</th>","<th>",x["climit"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")


  if(b=="PSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['customers']
   print("<body bgcolor=pink><center><table border=2 bgcolor=grey><tr><th>Customer Id</th><th>Customer Name</th><th>Customer Address</th><th>Customer Web</th><th>Credit Limit</th></tr></center>")
   for x in collection.find({'cus_id':t1}):
    print("<tr><th>",x["cus_id"],"</th>","<th>",x["cus_nm"],"</th>","<th>",x["cadd"],"</th>","<th>",x["cweb"],"</th>","<th>",x["climit"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")

except Exception:
        traceback.print_exc()

