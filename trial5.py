from tkinter import *
import tkinter.ttk as ttk
import csv

root = Tk()
root.title("STAFF LIST")
root.geometry('500x500')

TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
tree = ttk.Treeview(TableMargin, columns=("ID","name", "post", "salary"), height=400, selectmode="extended")
tree.heading('ID', text="W_ID", anchor=W)
tree.heading('name', text="name", anchor=W)
tree.heading('post', text="post", anchor=W)
tree.heading('salary', text="salary", anchor=W)
tree.column('#0',width=0)
tree.column('#1',width=100)
tree.column('#2',width=100)
tree.column('#3',width=100)
tree.column('#4',width=100)
tree.pack()

with open('workers.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        ID= row['WORKER_ID']
        name = row['NAME']
        post = row['POST']
        salary = row['SALARY']
        tree.insert("", 0, values=(ID,name,post,salary))
root.mainloop()