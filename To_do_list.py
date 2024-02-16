from tkinter import *
from tkinter import messagebox
import pickle
root = Tk()
root.geometry("500x500")
root.config(bg="light sky blue")
root.title("To-Do List")
root.resizable(False, False)

Title = Label(root, text=" THE TO-DO LIST", bg="sky blue", fg="black", font=("Brush script MT", 15, "bold"))
Title.pack(anchor="center", pady="20px")
global entry
def add_task():
    task = entry.get()
    if task != "" :
       listbox.insert(END, task) 
       entry.delete(0, END)
    else:
        messagebox.showwarning(title="Warning!", message="You must enter a task.") 
          
def delete_task():
    try:
        value = listbox.curselection()
        listbox.delete(value[0])
    except:
        messagebox.showwarning(title="Warning!", message="You must select a task.")

def save_tasks():
    tasks = listbox.get(0, listbox.size())
    pickle.dump(tasks, open("task.dat", "wb"))
def edit_tasks():
    try:
        tasks = pickle.edit(open("task.dat", "rb"))
        listbox.delete(0, END)
        for task in tasks:
            listbox.insert(END, task)
    except:
        messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")    

frame = Frame(root)
frame.pack()

listbox = Listbox(frame, height=10, width=50)
listbox.pack(side=LEFT)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = Entry(root, width=50)
entry.pack(pady="10px")

add = Button(root, text="Add task",bg="sky blue", fg="black", font=("ubuntu", 10), cursor="hand2",width=20,  command=add_task)
add.pack(anchor="center",pady="10px")

delete = Button(root, text="Delete ",bg="sky blue", fg="black", font=("ubuntu", 10), cursor="hand2",  width=20, command=delete_task)
delete.pack(anchor="center")

edit= Button(root, text="Edit ",bg="sky blue", fg="black", font=("ubuntu", 10), cursor="hand2", width=20, command=edit_tasks)
edit.pack(pady="10px")

save = Button(root, text="Save ",bg="sky blue", fg="black", font=("ubuntu", 10), cursor="hand2", width=20, command=save_tasks)
save.pack(anchor="center")
root.mainloop()