# Create a Python class to perform database operations on the donor table.
# The class should contain methods to:
# Add a new donor
# Retrieve all donors
# Retrieve a donor using ID
# Update donor details
# Delete a donor using ID

import mysql.connector

class DonorAddRetrieveUpdateDelete:

    def __init__(self):
        self.con=mysql.connector.connect(user="root",password="ajin",host="localhost",database="blooddb")
        self.c=self.con.cursor()
        print("Connection Successful")

    def add(self,name,bloodgroup,phone,city,last_donation):
        query='''insert into donor(name,bloodgroup,phone,city,last_donation) values(%s,%s,%s,%s,%s);'''
        data=(name,bloodgroup,phone,city,last_donation)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            return True
        else:
            return False

    def readall(self):
        query='''select * from donor;'''
        self.c.execute(query)
        rec=self.c.fetchall()
        if rec:
            return rec
        else:
            return False

    def retrieve(self,id):
        query = '''select * from donor where id=%s;'''
        data=(id,)
        self.c.execute(query,data)
        rec = self.c.fetchone()
        if rec:
            return rec
        else:
            return False

    def update(self,name,bloodgroup,phone,city,last_donation,id):
        query='''update donor set name=%s,bloodgroup=%s,phone=%s,city=%s,last_donation=%s where id=%s;'''
        data=(name,bloodgroup,phone,city,last_donation,id)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            return True
        else:
            return False

    def delete(self,id):
        query='''delete from donor where id=%s'''
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            return True
        else:
            return False