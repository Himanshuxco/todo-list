import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("300x400")
        
        # List to store tasks
        self.tasks = []
        
        # Title Label
        self.title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        
        # Task Entry
        self.task_entry = tk.Entry(root, width=20, font=("Helvetica", 14))
        self.task_entry.pack(pady=10)
        
        # Add Task Button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        # Task Listbox
        self.task_listbox = tk.Listbox(root, width=25, height=10, font=("Helvetica", 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)
        
        # Delete Task Button
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

# Create main window and run app
root = tk.Tk()
app = TodoApp(root)
root.mainloop()
