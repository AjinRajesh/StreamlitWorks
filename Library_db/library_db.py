import mysql.connector

class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user="root",password="ajin",host="localhost",database="library_db")
        self.c=self.con.cursor()
        print("Successfully Connected")

    def list(self):
        #reading all records from db table
        query='''select * from book;'''
        self.c.execute(query)

        rec=self.c.fetchall()
        if rec:
            # for row in rec:
            #     # print(row)
            return rec
        else:
            # print("No records found!")
            return 0


    def create(self,title,author,price,lang,pages):
        query='''insert into book(title,author,price,language,pages) values(%s,%s,%s,%s,%s);'''

        data=(title,author,price,lang,pages)

        self.c.execute(query,data)
        self.con.commit()
        # print("Data inserted successfully!!")

    def retrieve(self,id):
        query='''select * from book where id=%s'''
        data=(id,)
        self.c.execute(query,data)
        rec=self.c.fetchone()
        if rec:
                # print(rec)
                return rec
        else:
            # print("No record Found")
            return 0

    def update(self,title,author,price,lang,pages,id):
        query='''update book set title=%s,author=%s,price=%s,language=%s,pages=%s where id=%s'''

        data=(title,author,price,lang,pages,id)

        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            # print("Data updated")
            return self.c.rowcount
        else:
            # print("No record Found!")
            return 0


    def delete(self,id):
        query='''delete from book where id=%s;'''
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            # print("Row deleted successfully!")
            return self.c.rowcount
        else:
            # print("No records found")
            return 0

# book_instance=BookListCreateRetrieveUpdateDelete()
# while True:
    # print()
    # ch=int(input("1.list\n2.create\n3.retrieve\n4.update\n5.delete\n6.exit\nEnter choice: "))
    # if ch==1:
    #     book_instance.list()
    # elif ch==2:
    #     book_instance.create()
    # elif ch==3:
    #     book_instance.retrieve(int(input("Enter id of book to retrieve detail: ")))
    # elif ch==4:
    #     book_instance.update(int(input("Enter id to update row: ")))
    # elif ch==5:
    #     book_instance.delete(int(input("Enter id of row to delete: ")))
    # elif ch==6:
    #     book_instance.c.close()
    #     book_instance.con.close()
    #     break