
import sqlite3

con=sqlite3.Connection("dbi.db")
cursor=con.cursor()
cursor.execute("create table CUSTOMER(cust_id,cust_name,address,phone_no,city)")
print("enter 3 cust_id:")
cust_id=[int(input()) for i in range(3)]
print("enter 3 cust_name:")
name=[input() for i in range(3)]
print("enter 3 address for customer:")
address=[input() for i in range(3)]
print("enter 3 phone_no for customer:")
phone_no=[int(input()) for i in range(3)]
print("enter 3 city for customer:")
city=[input() for i in range(3)]
n=len(name)
for i in range(n):
    cursor.execute("insert into CUSTOMER values(?,?,?,?,?)",(id[i],name[i],address[i],phone_no[i],city[i]))
cursor.execute("select*from CUSTOMER")
data=cursor.fetchall()
con.close()
    
