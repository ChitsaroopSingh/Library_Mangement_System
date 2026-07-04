import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",password="ENTER YOUR MYSQL PASSWORD HERE")
cur=con.cursor()
cur=con.cursor(buffered=True)
#----------------BACK-END---------------------#
cur.execute("create database if not exists Library")
cur.execute("use Library")
cur.execute("create table if not exists Students"
            "("
            "Addm int(5) primary key,"
            "Name varchar(35),"
            "Class varchar(3));")
cur.execute("create table if not exists Books"
            "("
            "BookCode int(5) primary key,"
            "BookName varchar(35),"
            "BookAvailability varchar(3));")
cur.execute("create table if not exists IssuedBooks"
            "("
            "BookCode int(5) primary key,"
            "StudentName varchar(35),"
            "BookName varchar(35));")
#----------------FUNCTIONS---------------------#

#adding data to the table students
def add1():
    i=int(input("Enter Student's Addmission Number'"))
    n=input("Enter Student name")
    c=input("Enter students class")
    cur.execute("insert into Students (Addm, Name,Class) values(%s,%s,%s)",(i,n,c))
    con.commit()
    print(".....Data Saved Successfully.....")

#adding data to the table books
def add2():
    i=int(input("Enter book ID: "))
    n=input("Enter book name: ")
    a=input("Tell whether the book is issued or not,Yes if issued No if not")
    cur.execute("insert into Books (Code, BookName,BookAvailability) values(%s,%s,%s)",(i,n,a))
    con.commit()
    print(".....Data Saved Successfully.....")

#adding data to the table issued books
def add3():
    i=int(input("Enter Book Code "))
    n=input("Enter Student name ")
    c=input("Enter book name ")
    cur.execute("insert into IssuedBooks (BookCode, StudentName,BookName) values(%s,%s,%s)",(i,n,c))
    con.commit()
    print(".....Data Saved Successfully.....")

#showing data from the table students
def show1():
    print("Your details are as follows ")
    cur.execute("select * from Students ")
    d=cur.fetchall()
    for i in d:
        print("Student ID",i[0],end="\t\t")
        print("Student Name",i[1])

#showing data from the table books
def show2():
    print("Your details are as follows")
    cur.execute("select * from Books")
    d=cur.fetchall()
    for i in d:
        print("Code",i[0],end="\t\t")
        print("Book Name",i[1],end="\t\t")
        print("Book Availibility",i[2])
#showing available books from the table books
def show4():
    cur.execute("select Code,BookName from books where BookAvailability='Yes'")
    d=cur.fetchall()
    for i in d:
        print("Code",i[0],end="\t\t")
        print("Book Name",i[1],end="\t\t")

#showing unavailable books from the table books
def show3():
    cur.execute("select Code,BookName from books where BookAvailability='No'")
    d=cur.fetchall()
    for i in d:
        print("Code",i[0],end="\t\t")
        print("Book Name",i[1],end="\t\t")       

#deleting data from the table students
def dels():
    cur.execute("select * from Students")
    d=cur.fetchall()
    for i in d:
        print("Student ID",i[0],end="\t\t")
        print("Student Name",i[1])
    dc=int(input("Enter student ID: "))
    print("Your details are as follows")
    cur.execute("select * from students where addm=(%s)",(dc,))
    d=cur.fetchall()
    for i in d:
        print("Student ID",i[0],end="\t")
        print("Student Name",i[1])
    chh=input("Do you want to delete Y/N")
    if chh=="Y":
        cur.execute("delete from students where addm=(%s)",(dc,))
        con.commit()
        print("Deletion successful.")
    
#deleting data from the table books
def dels2():
    cur.execute("select * from books")
    d=cur.fetchall()
    for i in d:
        print("Book ID", i[0], end="\t\t")
        print("Book Name", i[1],end="\t\t")
        print("Book availability",i[2])
    dc = int(input("Enter book ID: "))
    print("Your details are as follows ")
    cur.execute("select * from books where code=(%s)", (dc,))
    d = cur.fetchall()
    for i in d:
        print("Book ID", i[0], end="\t\t")
        print("Book Name", i[1],end="\t\t")
        print("Book availability",i[2])
    chh = input("Do you want to delete Y/N")
    if chh == "Y":
        cur.execute("delete from books where code=(%s)", (dc,))
        con.commit()
        print("Deletion successful.")

#----------------------------------------------#

#----------------FRONT-END---------------------#
print("L   I   B   R   A   R   Y")
print("     M   A   N   A   G   E   M   E   N   T")
print("           S   Y   S   T   E   M")
print("")
print("SHOW DATA FROM")
print("1-Student Details\n2-Book Details\n3-Books Issued Details\n4-  available Books")
print("")
print("ADD DATA TO")
print("5-Students\n6-Books\n7-Issued Books")
print("")
print("DELETE DATA FROM")
print("8-Students\n9-Books")
ch=int(input("Enter Your choice"))
if ch==1:
    show1()
elif ch==2:
    show2()
elif ch==3:
    show3()
elif ch==4:
    show4()
elif ch==5:
    add1()
elif ch==6:
    add2()
elif ch==7:
    add3()
elif ch==8:
    dels()
elif ch==9:
    dels2()
else:
    print("Not a valid option")
