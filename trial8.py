from tkinter import *
import tkinter.simpledialog
import csv

def store():
    with  open ('doctor.csv','a+',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([id.get(),name.get(),age.get(),dept.get(),pno.get()])
    csvfile.close()    
    import trial7
   
 
root=Tk()
root.geometry("500x500")
id=StringVar()
name=StringVar()
age=StringVar()
dept=StringVar()
pno=StringVar()

title=Label(root,text="NEW PATIENT").grid(row=0,column=0,columnspan=4,ipadx=20,ipady=10)

lid=Label(root,text="ID:").grid(row=1,column=1)
eid=Entry(root,textvariable=id,width=10).grid(row=1,column=2)

lname=Label(root,text="NAME:").grid(row=2,column=1)
ename=Entry(root,textvariable=name,width=10).grid(row=2,column=2)

lage=Label(root,text="AGE:").grid(row=3,column=1)
eage=Entry(root,textvariable=age,width=10).grid(row=3,column=2)

ldept=Label(root,text="DEPT:").grid(row=4,column=1)
edept=Entry(root,textvariable=dept,width=10).grid(row=4,column=2)

lpno=Label(root,text="PNO:").grid(row=5,column=1)
epno=Entry(root,textvariable=pno,width=10).grid(row=5,column=2)

b1=Button(root,text="store",command=store).grid(row=6,column=1)

root.mainloop()






