from models.task import Task_manager 
import tkinter as tk

window = tk.Tk()
window.config(background='#151F30')
window.geometry('400x600')
window.title('To Do List')

container_task_frame = tk.Frame(window, borderwidth=2, relief='solid')
container_task_frame.pack(padx=30, pady=(30, 20), fill='both', expand=True)
container_task_frame.config(background='#151F30', highlightbackground='#FFF')

add_task_frame = tk.Frame(window)
add_task_frame.config(background='#151F30')
add_task_frame.pack(padx=30, pady=(0 , 30), fill='both', expand=False)

def handle_delete(id):
    Task_manager.delete_task(id)
    create_task()

edit = False
to_be_edited_id = None

def handle_edit(id):
    if len(add_task_frame.winfo_children()) == 3:
        add_task_frame.winfo_children()[2].destroy()

    global edit , to_be_edited_id

    for t in Task_manager.get_task_list():
        if t.task_id == id:
            entry_label = tk.Label(add_task_frame, text=f'Editando a task {t.task}', background='#151F30', fg='#FFF', font=('Inter', 12))
            entry_label.pack(pady=5, side='top')

            buttons_frame.pack(after=entry_label)

            to_be_edited_id = id
            break

    edit = True

def create_task():
    task_list = Task_manager.get_task_list()
    
    for child in container_task_frame.winfo_children():
        child.destroy()
    
    for t in task_list:
        task_frame = tk.Frame(container_task_frame)
        task_frame.pack(fill='x', pady=5, padx=30, expand=False)

        edit_btn = tk.Button(task_frame, text='Edit', command= lambda task_id=t.task_id: handle_edit(task_id))
        edit_btn.pack(side='left')

        label = tk.Label(task_frame, text=t.task)
        label.place(relx=0.5, rely=0.5, anchor='center')

        delete_btn = tk.Button(task_frame, text='Delete', command= lambda task_id=t.task_id: handle_delete(task_id))
        delete_btn.pack(side='right')

task_input = tk.Entry(add_task_frame)
task_input.pack(fill='x', ipady=5 ,padx=30, expand=True)

def alert_user(msg):
    if len(add_task_frame.winfo_children()) == 3:
        add_task_frame.winfo_children()[2].destroy()

    alert_label = tk.Label(add_task_frame, text=msg, background='#151F30', fg='#FFF', font=('Inter', 12))
    alert_label.pack(pady=5, side='top')

    buttons_frame.pack(after=alert_label)

def add_task():
    if not edit:
        if task_input.get():
            task = Task_manager(task_input.get())
            msg = Task_manager.add_task(task)

            if msg:
                alert_user(msg)
            else:
                if len(add_task_frame.winfo_children()) == 3:
                    add_task_frame.winfo_children()[2].destroy()

                create_task()
    else: 
        if len(add_task_frame.winfo_children()) == 3:
            add_task_frame.winfo_children()[2].destroy()

        new_task = task_input.get()
        Task_manager.edit_task(to_be_edited_id, new_task)
        create_task()

def cancel_edit():
    global edit
    if edit:
        edit = False
        add_task_frame.winfo_children()[2].destroy()

buttons_frame = tk.Frame(add_task_frame)
buttons_frame.config(background='#151F30')
buttons_frame.pack(padx=30, pady=(0 , 30), fill='both', expand=False)

add_task_btn = tk.Button(buttons_frame, text='Add Task', command=add_task , width=16)
add_task_btn.pack(side= 'left',ipady=5 , pady=10)

add_task_btn = tk.Button(buttons_frame, text='Cancel', command=cancel_edit,  width=16)
add_task_btn.pack(side= 'right' , ipady=5, pady=10)