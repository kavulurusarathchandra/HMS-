from tkinter import *
import tkinter.ttk as ttk
import csv

root1 = Tk()
root1.title("DOCTORS LIST")
root1.geometry('500x500')

TableMargin = Frame(root1, width=500)
TableMargin.pack(side=TOP)
tree = ttk.Treeview(TableMargin, columns=("ID","name","dept","no"), height=400, selectmode="extended")
tree.heading('ID', text="P_ID", anchor=W)
tree.heading('name', text="name", anchor=W)
tree.heading('dept', text="dept", anchor=W)
tree.heading('no', text="phone", anchor=W)
tree.column('#0',width=0)
tree.column('#1',width=100)
tree.column('#2',width=120)
tree.column('#3',width=120)
tree.column('#4',width=100)
tree.pack()

with open('doctor.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        ID= row['D_ID']
        name = row['D_NAME']
        dept = row['DEPARTMENT']
        no = row['D_PHONE']
        tree.insert("", 0, values=(ID,name,dept,no))
root1.mainloop()