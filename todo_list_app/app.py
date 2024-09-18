import tkinter
from tkinter import *

root = Tk()

root.title("To Do List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []


def addTask():
    task = tast_entry.get()
    tast_entry.delete(0, END)
    
    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
            
        task_list.append(task)
        list_box.insert(END, task)

def openTaskFile():
    try:
        global task_list 
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        
        for task in tasks:
            if task !='\n':
                task_list.append(task)
                list_box.insert( END, task)
                
    except:
        file = open('tasklist.txt', 'w')
        file.close()
        
def deleteTask():
    global task_list
    task = str(list_box.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        
        list_box.delete( ANCHOR)    

# icon

icon_img = PhotoImage(file="images/task.png")
root.iconphoto(False, icon_img)

# top
top_image = PhotoImage(file="images/topbar.png")
Label(root, image=top_image).pack()


dock_img = PhotoImage(file="images/dock.png")
Label(root, image=dock_img, bg="#32405b").place(x=30, y=25)

note_img = PhotoImage(file="images/task.png")
Label(root, image=note_img, bg= "#32405b").place(x=30, y=25)

heading = Label(root, text = "All Task", font = "arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# main
frame = Frame(root, width = 400, height=50, bg="white")
frame.place(x=0, y=180)


task = StringVar()
tast_entry = Entry(frame, width=18, font="arial 20", bd=0)
tast_entry.place(x=10, y=7)


button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)

# listbox
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160,0))

list_box = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b", fg="#fff", cursor="hand2", selectbackground="#5a95ff")
list_box.pack(side=LEFT, fill=BOTH, padx=2)
scrollBar = Scrollbar(frame1)
scrollBar.pack(side=RIGHT, fill=BOTH)

list_box.config(yscrollcommand=scrollBar.set)
scrollBar.config(command=list_box.yview)

openTaskFile()

# delete
delete_icon = PhotoImage(file="images/delete.png")
Button(root, image=delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

root.mainloop()