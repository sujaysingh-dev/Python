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
   collection=db['orderitem']
   a=0
   for x in collection.find({}):
     if(x['ord_id']==t1):
       a=1
       break
   if(a==1):
     print("<script>alert('Customer id already exist....')</script>")
     print("<script>window.open('Customers.html','_self')</script>")
   else:
    insert1={'ord_id':t1,'itm_id':t2,'prd_id':t3,'qnt':t4,'unt_price':t5}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")

  if(b=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['orderitem']
   collection.update_many({'ord_id':t1},{'$set':{'itm_id':t2,'prd_id':t3,'qnt':t4,'unt_price':t5}})
   print("<script>alert('Record Update....')</script>")

  if(b=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['orderitem']
   delete1={'ord_id':t1}
   collection.delete_many(delete1)
   print("<script>alert('Record Deleted...')</script>")


  if(b=="AllSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['orderitem']
   print("<body bgcolor=pink><center><table border=2 bgcolor=grey><tr><th>Order Id</th><th>Item Id</th><th>Product Id</th><th>Quntity</th><th>Unit Price</th></tr><center>")
   for x in collection.find({}):
    print("<tr><th>",x["ord_id"],"</th>","<th>",x["itm_id"],"</th>","<th>",x["prd_id"],"</th>","<th>",x["qnt"],"</th>","<th>",x["unt_price"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")


  if(b=="PSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['orderitem']
   print("<body bgcolor=pink><center><table border=2 bgcolor=grey><tr><th>Order Id</th><th>Item Id</th><th>Product Id</th><th>Quntity</th><th>Unit Price</th></tr><center>")
   for x in collection.find({'ord_id':t1}):
    print("<tr><th>",x["ord_id"],"</th>","<th>",x["itm_id"],"</th>","<th>",x["prd_id"],"</th>","<th>",x["qnt"],"</th>","<th>",x["unt_price"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")

except Exception:
        traceback.print_exc()

