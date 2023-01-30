import csv
from tkinter import *
file=open("hbill.csv")
Reader = csv.reader(file)
Data=list(Reader)

loi=[]
for x in list(range(0,51)):
    loi.append(Data[x][1])
root=Tk()
root.title("BILL")
root.geometry('300x310')
listbox1=Listbox(root)
for x,y in enumerate(loi):
    listbox1.insert(x,y)
listbox1.grid(row=0,column=0)

def update():
    index=listbox1.curselection()
    a=index[0]
    IDlabel2.config(text=Data[a][0])
    ID1label2.config(text=Data[a][1])
    ID2label2.config(text=Data[a][2])
    ID3label2.config(text=Data[a][3])
    ID4label2.config(text=Data[a][4])
    ID5label2.config(text=Data[a][5])
    return NONE

button1=Button(root,text="DISPLAY",command=update)
button1.grid(row=7,column=0)


IDlabel=Label(root,text="ID:").grid(row=1,column=0,sticky="w")
ID1label=Label(root,text="NAME:").grid(row=2,column=0,sticky="w")
ID2label=Label(root,text="AGE:").grid(row=3,column=0,sticky="w")
ID3label=Label(root,text="Dr FEE:").grid(row=4,column=0,sticky="w")
ID4label=Label(root,text="medicnes bill:").grid(row=5,column=0,sticky="w")
ID5label=Label(root,text="ROOM Charges:").grid(row=6,column=0,sticky="w")

IDlabel2=Label(root,text="")
IDlabel2.grid(row=1,column=1,sticky="w")
ID1label2=Label(root,text="")
ID1label2.grid(row=2,column=1,sticky="w")
ID2label2=Label(root,text="")
ID2label2.grid(row=3,column=1,sticky="w")
ID3label2=Label(root,text="")
ID3label2.grid(row=4,column=1,sticky="w")
ID4label2=Label(root,text="")
ID4label2.grid(row=5,column=1,sticky="w")
ID5label2=Label(root,text="")
ID5label2.grid(row=6,column=1,sticky="w")
root.mainloop()
