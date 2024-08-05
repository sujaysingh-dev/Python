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
t4=f.getvalue("t4")
t5=f.getvalue("t5")
t6=f.getvalue("t6")
t7=f.getvalue("t7")
t8=f.getvalue("t8")
t9=f.getvalue("t9")
t10=f.getvalue("t10")
t11=f.getvalue("t11")
t12=f.getvalue("t12")
t13=f.getvalue("t13")
t14=f.getvalue("t14")
t15=f.getvalue("t15")
b1=f.getvalue("b")
b2=f.getvalue("b1")
b3=f.getvalue("b2")
b4=f.getvalue("b3")
try:
     if(b1=="Login"):
          client=pymongo.MongoClient("mongodb://localhost:27017/")
          db=client['inventory']
          collection=db['adminlogin']
          a=0
          for x in collection.find({}):
               if(x['loginid']==t1 and x['password']==t2):
                    a=1
                    break
          if(a==1):
               print("<script>window.open('Menu.html','_self')</script>")
          else:
               print("<script>alert('Please Check Your UserId Or Password.....')</script>")
               print("<script>window.open('AdminLogin.html','_self')</script>")
       
     if(b2=="Next"):
          client=pymongo.MongoClient("mongodb://localhost:27017/")
          db=client['inventory']
          collection=db['adminlogin']
          a=0
          for x in collection.find({}):
               if(x['loginid']==t14 and x['password']==t15):
                    a=1
                    break
          if(a==1):
               print("<script>alert('Request Accepted You Can Create User.....')</script>")
               print("<script>window.open('AdminLogin.html#Create1','_self')</script>")
          else:
               print("<script>alert('Access Denied.....')</script>")
               print("<script>window.open('AdminLogin.html#Create','_self')</script>")

     if(b3=="Create"):
          client=pymongo.MongoClient("mongodb://localhost:27017/")
          db=client['inventory']
          collection=db['adminlogin']
          a=0
          for x in collection.find({}):
               if(x['loginid']==t7):
                    a=1
                    break
          if(a==1):
               print("<script>alert('This Login Id Already Exist....')</script>")
               print("<script>window.open('adminlogin.html','_self')</script>")
          else:
               if(t8==t9):
                    insert1={'fullname':t3,'gender':t4,'dateofbirth':t5,'mobile':t6,'loginid':t7,'password':t8,'cpassword':t9}
                    collection.insert_one(insert1)
                    print("<script>alert('New User Created Successfully ....')</script>")
                    print("<script>window.open('AdminLogin.html','_self')</script>")
               else:
                    print("<script>alert('Please Check Your Password........')</script>")
                    print("<script>window.open('AdminLogin.html#Create1','_self')</script>")

     if(b4=="Submit"):
          client=pymongo.MongoClient("mongodb://localhost:27017/")
          db=client['inventory']
          collection=db['adminlogin']
          a=0
          for x in collection.find({}):
               if(x['dateofbirth']==t10 and x['mobile']==t11):
                    if(t12==t13):
                         collection.update_many({'dateofbirth':t10,'mobile':t11},{'$set':{'password':t12,'cpassword':t13}})
                         print("<script>alert('Password Change Successfully....')</script>")
                         print("<script>window.open('AdminLogin.html','_self')</script>")
                    print("<script>alert('Check Your Password....')</script>")
                    print("<script>window.open('AdminLogin.html#Forget','_self')</script>")
               print("<script>alert('Your Detail Not Matched....')</script>")
               print("<script>window.open('AdminLogin.html#Forget','_self')</script>")

except Exception:
        traceback.print_exc()

