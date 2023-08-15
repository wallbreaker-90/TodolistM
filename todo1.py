import tkinter as tk
from tkinter import messagebox


file_path = "C:\\Users\\MANAS\\Documents\\text.txt"

def add_task():
    Serial_no=task_entry3.get().strip()
    priority=task_entry1.get().strip()
    content=task_entry.get("1.0", tk.END).strip()
    task = content
    main_task = (Serial_no+"   \t    \t                               "+ priority+ ""+"        \t                "  + content+"\n").strip()
    if len(priority)  == 0 and len(task)==0:
        messagebox.showwarning("Warning", "Enter Task")
    else:
            if len(priority) == 0:
                messagebox.showwarning("Warning", "Enter Priority")
            else:
            
                if len(task) == 0:
                    messagebox.showwarning("Warning", "Enter something")
                else:
                    listbox.insert(tk.END, main_task)
                    task_entry.delete("1.0", tk.END)
                    with open(file_path, "a") as file:  
                        for task in listbox.get(0, tk.END):
                            file.write(task + "\n")
                    close_add_window()



def load_tasks():
    listbox.delete(0, tk.END)
    with open(file_path, "r") as file:
        for line in file:
            listbox.insert(tk.END, line.strip())    
            
def close_add_window():
    w2.destroy()
    window.deiconify()  

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        deleted_index = selected_task_index[0]
        tasks = list(listbox.get(0, tk.END))
        tasks.pop(deleted_index)  
        
        listbox.delete(deleted_index)  
        
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(task + "\n")  

            

def exit_app():
    window.destroy()

def open_add_window():
    window.withdraw()  
    global w2
    w2 = tk.Toplevel()
    w2.title("Add Task")
    w2.geometry("600x700")
    w2.configure(bg="yellow")

    welcome = tk.Label(w2, text="Welcome", font=("Arial", 30))
    welcome.place(x=200, y=40)

    global task_entry,task_entry1,task_entry3


    l1=tk.Label(w2,text="Serial no.:",font=("Arial", 20))
    l1.place(x=100, y=100)
    l2=tk.Label(w2,text=" Priority",font=("Arial", 20))
    l2.place(x=100, y=150)
    l3=tk.Label(w2,text=" Content",font=("Arial", 20))
    l3.place(x=100, y=200)
    task_entry3 = tk.Entry(w2, font=("Arial", 20))
    task_entry3.place(x=250, y=100)
    task_entry1 = tk.Entry(w2, font=("Arial", 20))
    task_entry1.place(x=250, y=150)
    task_entry = tk.Text(w2, height=12, width=20, font=("Arial", 20))
    task_entry.place(x=250, y=200)



    save_button = tk.Button(w2, text="Save", cursor='hand2', font=("Arial", 15),command=add_task)
    save_button.place(x=200, y=600)
    back_button = tk.Button(w2, text="Back", cursor='hand2', font=("Arial", 15),command=close_add_window)
    back_button.place(x=300, y=600)
    

window = tk.Tk()
window.title("ToDo List")
window.geometry("1360x800")
window.configure(bg="orange")

title_label = tk.Label(width=20, text="ToDo List", font=("Arial", 30))
title_label.place(x=400, y=50)

add_button = tk.Button(window, text="ADD", cursor='hand2', font=("Arial", 20), border=0, relief=tk.SUNKEN, command=open_add_window)
add_button.place(x=300, y=625)

delete_button = tk.Button(window, text="Delete",font=("Arial", 20), command=delete_task)
delete_button.place(x=700,y=625)

l=tk.Label(window,text="Sr No. \t              |    Priority \t        |       Content                                                                         ",font=("Arial", 20))
l.place(x=30, y=110)

listbox = tk.Listbox(window)
listbox.configure(font=('Arial 22'))



listbox.pack(padx=30,pady=150,fill="both",expand=True)


exit_button = tk.Button(window, text="Exit",font=("Arial", 20), command=exit_app)
exit_button.place(x=1000,y=625)
load_tasks()
window.mainloop()
