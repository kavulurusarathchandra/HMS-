from tkinter import * 
from tkinter import ttk
import csv

root=Tk()
root.geometry('1000x1000')
title=Label(root,bd=20,relief=RIDGE,text="CBIT HOSPITAL",fg="red",bg="white",font=("times new roman",50,"bold"))
title.pack(side=TOP,fill=X)
dataFrame=Frame(root,bd=10,relief=RIDGE)
dataFrame.place(x=0,y=150,width=1000,height=400)
def f1():
    import trial
def f2():
    import trial2
def f3():
    import trial3
def f4():
    import trial4
def f5():
    import trial5
def f6():
    import trial6
def f7():
    import trial7
def f8():
    import opt5
def f9():
    import opt6
def f10():
    import opt7


        
            
        
button1=Button(root,text="click here to check bill",command=f1)
button1.place(x=100,y=175,width=300,height=40)
button2=Button(root,text="click here to check staff details",command=f2)
button2.place(x=100,y=250,width=300,height=40)
button3=Button(root,text="click here to check doctor details",command=f3)
button3.place(x=100,y=325,width=300,height=40)
button4=Button(root,text="click here to check patient details",command=f4)
button4.place(x=100,y=400,width=300,height=40)
button5=Button(root,text="click here to view staff list",command=f5)
button5.place(x=100,y=475,width=300,height=40)

button6=Button(root,text="click here to view patient list",command=f6)
button6.place(x=600,y=175,width=300,height=40)
button7=Button(root,text="click here to view doctors list",command=f7)
button7.place(x=600,y=250,width=300,height=40)
button8=Button(root,text="Patient Analysis",command=f8)
button8.place(x=600,y=325,width=300,height=40)
button9=Button(root,text="line plot",command=f9)
button9.place(x=600,y=400,width=300,height=40)
button10=Button(root,text="Doctors Analysis",command=f10)
button10.place(x=600,y=475,width=300,height=40)



def store():
    with  open ('doctor.csv','a+',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([id.get(),name.get(),age.get(),dept.get(),pno.get()])
    csvfile.close()    
    #import trial7
   
 
id=StringVar()
name=StringVar()
age=StringVar()
dept=StringVar()
pno=StringVar()

title=Label(root,bd=5,relief=RIDGE,text="NEW DOCTOR",fg="red",bg="white",font=("times new roman",15,"bold")).place(x=125,y=555)
dataFrame=Frame(root,bd=10,relief=RIDGE)
dataFrame.place(x=0,y=600,width=400,height=190)

lid=Label(root,text="ID:").place(x=100,y=625)
eid=Entry(root,textvariable=id,width=15).place(x=145,y=625)

lname=Label(root,text="NAME:").place(x=100,y=650)
ename=Entry(root,textvariable=name,width=15).place(x=145,y=650)

lage=Label(root,text="AGE:").place(x=100,y=675)
eage=Entry(root,textvariable=age,width=15).place(x=145,y=675)

ldept=Label(root,text="DEPT:").place(x=100,y=700)
edept=Entry(root,textvariable=dept,width=15).place(x=145,y=700)

lpno=Label(root,text="PNO:").place(x=100,y=725)
epno=Entry(root,textvariable=pno,width=15).place(x=145,y=725)

b1=Button(root,text="store",command=store).place(x=100,y=750)



def add():
    with  open ('patient.csv','a+',newline='') as csvfile1:
        writer = csv.writer(csvfile1)
        writer.writerow([pid.get(),pname.get(),page.get(),pdisease.get(),ppno.get()])
    csvfile1.close()    
    #import trial6
   
 
pid=StringVar()
pname=StringVar()
page=StringVar()
pdisease=StringVar()
ppno=StringVar()

title=Label(root,bd=5,relief=RIDGE,text="NEW PATIENT",fg="red",bg="white",font=("times new roman",15,"bold")).place(x=650,y=555)
dataFrame=Frame(root,bd=10,relief=RIDGE)
dataFrame.place(x=550,y=600,width=400,height=190)

lid=Label(root,text="ID:").place(x=650,y=625)
eid=Entry(root,textvariable=pid,width=15).place(x=695,y=625)

lname=Label(root,text="NAME:").place(x=650,y=650)
ename=Entry(root,textvariable=pname,width=15).place(x=695,y=650)

lage=Label(root,text="AGE:").place(x=650,y=675)
eage=Entry(root,textvariable=page,width=15).place(x=695,y=675)

ldept=Label(root,text="DISEASE:").place(x=650,y=700)
edept=Entry(root,textvariable=pdisease,width=15).place(x=695,y=700)

lpno=Label(root,text="PNO:").place(x=650,y=725)
epno=Entry(root,textvariable=ppno,width=15).place(x=695,y=725)

b1=Button(root,text="store",command=add).place(x=650,y=750)
root.mainloop()
