from tkinter import *
from tkinter import scrolledtext
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="school"
)
mycursor = mydb.cursor()  # '''CREATE TABLE customer (name varchar(20), address varchar(255))''')

def getdata():
    try:
        r = roll.get()
        n = name.get()
        m = marks.get()
        if (r and n and m):
            mycursor.execute("create table if not exists student(roll int(2) primary key,name varchar(10),marks int(2))")
            mycursor.execute("insert into student(roll,name,marks) values('" + str(r) + "','" + n + "','" + str(m) + "')")
            mydb.commit()
            # lbl2.config(text="Success")
            erase()  # calling erase function
            # mydb.close()
        else:
            print("Enter Details")

    except:
        print("Duplicate Roll No Not Allowed")

def updatename():
    ur = uroll.get()
    un = uname.get()
    if (ur and un):
        mycursor.execute("update student set name ='%s'" % (un) + "where roll ='%s'" % (ur))
        mydb.commit()
    # we use direct string for update or we convert it into int value by using int() functiom
        uroll.delete(0, END)
        uname.delete(0, END)

    else:
        print("Enter The Roll and Name")

def updatemarks():
    ur = uroll.get()
    um = umarks.get()

    if (ur and um):

        mycursor.execute("update student set marks ='%s'" % (um) + "where roll = '%s'" % (ur))
        mydb.commit()

        uroll.delete(0, END)
        umarks.delete(0, END)
    else:
        print("Enter The Roll and marks")

def showdata():
    cleardata()
    try:
        mycursor.execute("select * from student")
        data =mycursor.fetchall()

        for y in data:
            st.insert(INSERT,y)
            st.insert(INSERT,"\n")

    except:
        st.insert(INSERT,'Error..Table Not exist')

def cleardata():
    st.delete(1.0, END)

def erase():
    roll.delete(0, END)
    name.delete(0, END)
    marks.delete(0, END)

def deleterecordsroll():
    try:
        dr = int(droll.get())
        if (dr):
            mycursor.execute("select roll from student where roll like '%d'" % (dr))
            fr = mycursor.fetchone()
            if (fr):

                mycursor.execute("delete from student where roll ='%d'" % (dr))
                mydb.commit()
                lbl12.config(text="deleted")
                print("Deleted")
            else:
                droll.delete(0, END)
                print("Record Not exist")
    except:
        print("Please Enter Integer Value")

def deleterecordsname():
    dn = str(dname.get())
    if (dn):
        mycursor.execute("select name from student where name like '%s'" % (dn))
        fn = mycursor.fetchone()
        if (fn):
            mycursor.execute("delete from student where name ='%s'" % (fn))
            mydb.commit()
            lbl14.config(text="deleted")
            print("deleted")
        else:
            dname.delete(0, END)
            print("Record Not exist")
    else:
        print("Please Enter The Name")

def searchroll():
    try:
        sr = int(sroll.get())
        mycursor.execute("select roll,name,marks from student where roll like '%d'" % (sr))
        dt = mycursor.fetchone()
        if (dt):
            print(dt)
            lbl17.config(text="found")
        else:
            sroll.delete(0,END)
            print("Not Found")
            # print("In The Search Roll Function")
            lbl17.config(text="not found")
    except:
        print("Please Enter The Integer Value")

def searchname():
    sn = sname.get()
    if (sn):

        mycursor.execute("select roll,name,marks from student where name like '%s'" % (sn))
        dt = mycursor.fetchone()
        if (dt):

            print(dt)
            lbl19.config(text="found")
        else:
            sname.delete(0, END)
            print("Not Found")
            # print("In The Search Name Function")
            lbl19.config(text="not found")

    else:
        print("Enter The Input")

root = Tk()
root.title("Student Database V 1.0")
root.geometry("500x365")
root.minsize(500,365)
root.maxsize(500,365)


lbl1 = Label(root, text="Insert Records ", font="bold 10")
lbl1.grid(row=0, column=1)
lbl2 = Label(root, text="Roll No")
lbl2.grid(row=1, column=0)
lbl3 = Label(root, text="Name")
lbl3.grid(row=2, column=0)
lbl4 = Label(root, text="Marks")
lbl4.grid(row=3, column=0)

roll = Entry(root, width=15)
roll.grid(row=1, column=1)
name = Entry(root, width=15)
name.grid(row=2,
          column=1)  # bad option "-spanx": must be -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky
marks = Entry(root, width=15)
marks.grid(row=3, column=1)

btn1 = Button(root, text="Submit", command=getdata)
btn1.grid(row=4, column=1, ipadx=5)
# btn2 = Button(root,text ="showdata",command=showdata)
# btn2.grid(row =5,column =1)

lbl5 = Label(root, text="", width=10, )
lbl5.grid(row=4, column=2)

# **********GUI For Updating data

lbl6 = Label(root, text="roll")
lbl6.grid(row=1, column=2)
lbl7 = Label(root, text="name")
lbl7.grid(row=2, column=2)
lbl8 = Label(root, text="marks")
lbl8.grid(row=3, column=2)
lbl9 = Label(root, text="Update Records ", font="bold 10")
lbl9.grid(row=0, column=3)

uroll = Entry(root, width=15)
uroll.grid(row=1, column=3)
uname = Entry(root, width=15)
uname.grid(row=2, column=3)
umarks = Entry(root, width=15)
umarks.grid(row=3, column=3)

btn3 = Button(root, text="update", command=updatename)
btn3.grid(row=2, column=4)
btn4 = Button(root, text="update", command=updatemarks)
btn4.grid(row=3, column=4)

# ************GUI For DeleteRecords
# ******delete records by roll no

lbl10 = Label(root, text="Delete Records")
lbl10.grid(row=6, column=0,sticky='w')
lbl11 = Label(root, text="By Roll No")
lbl11.grid(row=7, column=0)
lbl12 = Label(root, text="")
lbl12.grid(row=7, column=3)
droll = Entry(root, width=10)
droll.grid(row=7, column=1)
btn5 = Button(root, text="delete", command=deleterecordsroll)
btn5.grid(row=7, column=2)

# **********delete records by name

lbl13 = Label(root, text="By Name  ")
lbl13.grid(row=8, column=0)
dname = Entry(root, width=10)
dname.grid(row=8, column=1)
lbl14 = Label(root, text="")
lbl14.grid(row=8, column=3)
btn6 = Button(root, text="delete", command=deleterecordsname)
btn6.grid(row=8, column=2)

# ***********GUI For search Records

# *********Search By Roll No

lbl15 = Label(root, text="Search Records", font="bold 10")
lbl15.grid(row=9, column=0)

lbl16 = Label(root, text="By Roll No")
lbl16.grid(row=10, column=0)

sroll = Entry(root, width=10)
sroll.grid(row=10, column=1)

btn7 = Button(root, text="search", command=searchroll)
btn7.grid(row=10, column=2)

lbl17 = Label(root, text="")
lbl17.grid(row=10, column=3)

# ********Search By Name

lbl18 = Label(root, text="By Name  ")
lbl18.grid(row=11, column=0)

sname = Entry(root, width=10)
sname.grid(row=11, column=1)

btn8 = Button(root, text="search", command=searchname)
btn8.grid(row=11, column=2)

lbl19 = Label(root, text="")
lbl19.grid(row=11, column=3)

#***************GUI For Showing data

lbl20 =Label(root,text ="Show Data",font="bold 10")
lbl20.grid(row=12 ,column =0,sticky='w')
st=scrolledtext.ScrolledText(root,width=16,height=4)
st.grid(row=13,column=1)

btn9 =Button(root,text ="show",command = showdata)
btn9.grid(row = 13,column= 2,sticky='n')

btn10 =Button(root,text ="clear",command=cleardata)
btn10.grid(row=13 ,column= 2,sticky ='s')

root.mainloop()
