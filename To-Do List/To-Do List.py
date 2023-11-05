import tkinter as tk

def add_task():
    description = task_description.get()
    due_date = task_due_date.get()
    priority = task_priority.get()
    task = f"Description: {description} | Due Date: {due_date} | Priority: {priority}"
    task_list.insert(tk.END, task)

def complete_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        completed_tasks.insert(tk.END, task_list.get(selected_task_index))
        task_list.delete(selected_task_index)

def update_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        description = task_description.get()
        due_date = task_due_date.get()
        priority = task_priority.get()
        updated_task = f"Description: {description} | Due Date: {due_date} | Priority: {priority}"
        task_list.delete(selected_task_index)
        task_list.insert(selected_task_index, updated_task)

def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)

# Create the main window
root = tk.Tk()
root.title("To-Do List App")

# Task Entry
tk.Label(root, text="Description:").pack()
task_description = tk.Entry(root)
task_description.pack()

tk.Label(root, text="Due Date:").pack()
task_due_date = tk.Entry(root)
task_due_date.pack()

tk.Label(root, text="Priority:").pack()
task_priority = tk.Entry(root)
task_priority.pack()

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack()

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Task List Display
tk.Label(root, text="Task List:").pack()
task_list = tk.Listbox(root)
task_list.pack()

# Completed Tasks List Display
tk.Label(root, text="Completed Tasks:").pack()
completed_tasks = tk.Listbox(root)
completed_tasks.pack()

root.mainloop()
