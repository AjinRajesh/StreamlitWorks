import mysql.connector

class VehicleListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.con=mysql.connector.connect(user="root",password="ajin",host="localhost",database="Vehicle_db")
        self.c=self.con.cursor()
        print("Connection established successfully")

    def list(self):
        query='''select * from vehicle;'''
        self.c.execute(query)
        rec=self.c.fetchall()
        if rec:
            for row in rec:
                print(row)
        else:
            print("Record not found!")

    def create(self):
        query='''insert into vehicle(brand,model,type,price,year) values (%s,%s,%s,%s,%s);'''

        brand = input("Brand of vehicle: ")
        model = input("Model of vehicle: ")
        t = input("Enter the type of vehicle: ")
        price = int(input("Enter price of the vehicle: "))
        yr = int(input("Enter the year of making: "))

        data=(brand,model,t,price,yr)
        self.c.execute(query,data)
        self.con.commit()
        print("Data Inserted Successfully")

    def retrieve(self,id):
        query = '''select * from vehicle where id=%s;'''
        data=(id,)
        self.c.execute(query,data)
        rec = self.c.fetchone()
        if rec:
                print(rec)
        else:
            print("Record not found!")

    def delete(self,id):
        query='''delete from vehicle where id=%s;'''
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            print(f"Data deleted successfully at id = {id}")
        else:
            print("No record Found!")

    def update(self,id):
        query='''update vehicle set brand=%s,model=%s,type=%s,price=%s,year=%s where id=%s;'''
        brand = input("Brand of updated vehicle: ")
        model = input("Model of updated vehicle: ")
        t = input("Enter the type of updated vehicle: ")
        price = int(input("Enter price of the updated vehicle: "))
        yr = int(input("Enter the year of making for the updated vehicle: "))

        data=(brand,model,t,price,yr,id)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            print("Data updated Successfully")
        else:
            print("No record found")


obj=VehicleListCreateRetrieveUpdateDelete()
while True:
    print()
    ch=int(input("1.list\n2.create\n3.retrieve\n4.update\n5.delete\n6.exit\nEnter choice: "))
    if ch==1:
        obj.list()
    elif ch==2:
        obj.create()
    elif ch==3:
        obj.retrieve(int(input("Enter id of vehicle to retrieve detail: ")))
    elif ch==4:
        obj.update(int(input("Enter id of vehicle to update row: ")))
    elif ch==5:
        obj.delete(int(input("Enter id of vehicle to delete row: ")))
    elif ch==6:
        obj.c.close()
        obj.con.close()
        break