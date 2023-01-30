from tkinter import *
import tkinter.ttk as ttk
import csv

root = Tk()
root.title("PATIENTS LIST")
root.geometry('500x500')


TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
tree = ttk.Treeview(TableMargin, columns=("ID","name","age","disease"), height=400, selectmode="extended")
tree.heading('ID', text="P_ID", anchor=W)
tree.heading('name', text="name", anchor=W)
tree.heading('age', text="age", anchor=W)
tree.heading('disease', text="disease", anchor=W)
tree.column('#0',width=0)
tree.column('#1',width=100)
tree.column('#2',width=100)
tree.column('#3',width=100)
tree.column('#4',width=100)
tree.pack()

with open('patient.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        ID= row['P_ID']
        name = row['P_NAME']
        age = row['P_AGE']
        disease = row['P_DISEASE']
        tree.insert("", 0, values=(ID,name,age,disease))
root.mainloop()
