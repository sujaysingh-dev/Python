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
t7=f.getvalue("t7")
t8=f.getvalue("t8")
b=f.getvalue("b")
try:
  if(b=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['employees']
   a=0
   for x in collection.find({}):
     if(x['emp_id']==t1):
       a=1
       break
   if(a==1):
     print("<script>alert('Customer id already exist....')</script>")
     print("<script>window.open('Customers.html','_self')</script>")
   else:
    insert1={'emp_id':t1,'first_nm':t2,'last_nm':t3,'email_id':t4,'phone_no':t5,'hire_date':t6,'mng_id':t7,'join_date':t8}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")

  if(b=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['employees']
   collection.update_many({'emp_id':t1},{'$set':{'first_nm':t2,'last_nm':t3,'email_id':t4,'phone_no':t5,'hire_date':t6,'mng_id':t7,'join_date':t8}})
   print("<script>alert('Record Update....')</script>")

  if(b=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['employees']
   delete1={'emp_id':t1}
   collection.delete_many(delete1)
   print("<script>alert('Record Deleted...')</script>")


  if(b=="AllSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['employees']
   print("<body bgcolor=pink><center><table border=2 bgcolor=grey><tr><th>Employee Id</th><th>First Name</th><th>Last Name</th><th>Email Id</th><th>Phone Number</th><th>Hire Date</th><th>Maneger Id</th><th>Join Date</th></tr><center>")
   for x in collection.find({}):
    print("<tr><th>",x["emp_id"],"</th>","<th>",x["first_nm"],"</th>","<th>",x["last_nm"],"</th>","<th>",x["email_id"],"</th>","<th>",x["phone_no"],"</th><th>",x["hire_date"],"</th>","<th>",x["mng_id"],"</th>","<th>",x["join_date"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")


  if(b=="PSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['employees']
   print("<body bgcolor=pink><center><table border=2 bgcolor=grey><tr><th>Employee Id</th><th>First Name</th><th>Last Name</th><th>Email Id</th><th>Phone Number</th><th>Hire Date</th><th>Maneger Id</th><th>Join Date</th></tr><center>")
   for x in collection.find({'emp_id':t1}):
    print("<tr><th>",x["emp_id"],"</th>","<th>",x["first_nm"],"</th>","<th>",x["last_nm"],"</th>","<th>",x["email_id"],"</th>","<th>",x["phone_no"],"</th><th>",x["hire_date"],"</th>","<th>",x["mng_id"],"</th>","<th>",x["join_date"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")

except Exception:
        traceback.print_exc()

