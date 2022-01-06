from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import mysql.connector
mydb=mysql.connector.connect(host="localhost",port="3306",database="python",user="root",password="")
mycursor=mydb.cursor()

top=Tk()
l1=Label(top,text="First Name")
l1.grid(row=0,column=0)
t1=Entry(top,bd=5) 
t1.grid(row=0,column=1)
l2=Label(top,text="Last Name")
l2.grid(row=1,column=0)
t2=Entry(top,bd=5) 
t2.grid(row=1,column=1)
l3=Label(top,text="Contact Number")
l3.grid(row=2,column=0)
t3=Entry(top,bd=5) 
t3.grid(row=2,column=1)
l4=Label(top,text="Gender")
l4.grid(row=3,column=0)
var=IntVar()
r1=Radiobutton(top,text="Male",variable=var,value=1)
r2=Radiobutton(top,text="Female",variable=var,value=2)
r1.grid(row=3,column=1)
r2.grid(row=3,column=2)
def Register(): 
    sql="insert into teacher (fn,ln,contact,gender) values(%s,%s,%s,%s)" 
    fn=t1.get()
    ln=t2.get() 
    contact=t3.get() 
    if(var.get()==1): 
        gender="Male" 
    else: 
        gender="Female" 
    values=(fn,ln,contact,gender)
    mycursor.execute(sql,values) 
    mydb.commit() 
    messagebox.askokcancel("Information","Record Inserted Successfully")
def Delete():
    fn=t1.get()
    sql="delete from teacher where fn='%s'"%fn
    mycursor.execute(sql) 
    mydb.commit()
    messagebox.askokcancel("Information","Record Deketed Successfully")
def Update():   
    
    fn=t1.get()
    ln=t2.get() 
    contact=t3.get() 
    if(var.get()==1): 
        gender="Male" 
    else: 
        gender="Female"
    sql="update teacher set ln='%s',contact='%s',gender='%s' where fn='%s'"%(ln,contact,gender,fn)
    mycursor.execute(sql) 
    mydb.commit() 
    messagebox.askokcancel("Information","Record Updated Successfully")

def ShowAll(): 
    class A(Frame): 
        
        def __init__ (self,parent): 
            Frame.__init__(self,parent) 
            self.createUI()
            self.LoadTable()
            self.grid(sticky=(N,S,W,E)) 
            parent.grid_rowconfigure(0,weight=1) 
            parent.grid_columnconfigure(0,weight=1) 
        
        def createUI(self): 
            tv=Treeview(self) 
            tv['columns']=('id','firstname','lastname','contact','gender') 
            tv.heading('#0',text='id',anchor='center') 
            tv.column('#0',anchor='center') 
            tv.heading('#1',text='firstname',anchor='center') 
            tv.column('#1',anchor='center') 
            tv.heading('#2',text='lastname',anchor='center') 
            tv.column('#2',anchor='center') 
            tv.heading('#3',text='contact',anchor='center') 
            tv.column('#3',anchor='center') 
            tv.heading('#4',text='gender',anchor='center')
            tv.column('#4',anchor='center') 
            tv.grid(sticky=(N,S,W,E))
            self.treeview=tv
            self.grid_rowconfigure(0,weight=1) 
            self.grid_columnconfigure(0,weight=1) 
        
        def LoadTable(self): 
            sql="select * from teacher" 
            mycursor.execute(sql) 
            result=mycursor.fetchall() 
            for i in result: 
                id=i[0]
                firstname=i[1] 
                lastname=i[2] 
                contact=i[3] 
                gender=i[4] 
                self.treeview.insert("",'end',text=id,values=(firstname,lastname,contact,gender)) 
    root=Tk()
    root.title("All Data")
    A(root) 

b1=Button(top,text="Register",command=Register)
b1.grid(row=4,column=0)
b2=Button(top,text="Delete",command=Delete)
b2.grid(row=4,column=1)
b3=Button(top,text="Update",command=Update)
b3.grid(row=5,column=0)
b4=Button(top,text="Show All",command=ShowAll)
b4.grid(row=5,column=1)
top.geometry('500x500')
