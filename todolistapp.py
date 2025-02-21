import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def clear_tasks():
    task_list.delete(0, tk.END)

# Main App Window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")
root.config(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="To-Do List", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Task Entry Field
task_entry = tk.Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", font=("Arial", 12), command=add_task)
add_button.grid(row=0, column=0, padx=5)

remove_button = tk.Button(button_frame, text="Remove Task", font=("Arial", 12), command=remove_task)
remove_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear All", font=("Arial", 12), command=clear_tasks)
clear_button.grid(row=0, column=2, padx=5)

# Task Listbox
task_list = tk.Listbox(root, font=("Arial", 14), width=40, height=15)
task_list.pack(pady=10)

# Run the app
root.mainloop()
