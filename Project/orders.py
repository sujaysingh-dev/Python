#!C:/Users/T.YADAV/AppData/Local/Programs/Python/Python311/python
print("Content-Type:text/html")
print()
import cgi
import traceback
from pymongo import MongoClient
import pymongo
f=cgi.FieldStorage()
t1=f.getvalue("t1")
t2=f.getvalue("t2")
t3=f.getvalue("t3")
t4=f.getvalue("t4")
t5=f.getvalue("t5")
b1=f.getvalue("b")
try:
 if(b1=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['orders']
   a=0
   for x in collection.find({}):
     if(x['ord_id']==t1):
       a=1
       break
   if(a==1):
     print("<script>alert('Customer id already exist....')</script>")
     print("<script>window.open('Customers.html','_self')</script>")
   else:
    insert1={'ord_id':t1,'cus_id':t2,'status':t3,'salesman_id':t4,'ord_date':t5}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")

 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['orders']
   collection.update_many({'ord_id':t1},{'$set':{'cus_id':t2,'status':t3,'sa;esman_id':t4,'ord_date':t5}})
   print("<script>alert('Record Update....')</script>")

   
 if(b1=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['orders']
   delete1={'ord_id':t1}
   collection.delete_many(delete1)
   print("<script>alert('Record Deleted...')</script>")


 if(b1=="AllSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['orders']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Order Id</th><th>Customer id</th><th>Status</th><th>Salesman ID</th><th>Order Date</th></tr>")
   for x in collection.find({}):
    print("<tr><th>",x["ord_id"],"</th>","<th>",x["cus_id"],"</th>","<th>",x["status"],"</th>","<th>",x["salesman_id"],"</th>","<th>",x["ord_date"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")


 if(b1=="PSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['orders']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Order Id</th><th>Customer id</th><th>Status</th><th>Salesman ID</th><th>Order Date</th></tr>")
   for x in collection.find({'ord_id':t1}):
    print("<tr><th>",x["ord_id"],"</th>","<th>",x["cus_id"],"</th>","<th>",x["status"],"</th>","<th>",x["salesman_id"],"</th>","<th>",x["ord_date"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")

except Exception:
        traceback.print_exc()
