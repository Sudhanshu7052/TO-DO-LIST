# Step 0: Import necessary modules
import tkinter as tk
from tkinter import messagebox, filedialog
import json

# Step 0.1: Initialize task list and edit index
tasks = []
edit_index = None

# Step 1: Add or Update Task
def add_task():
    global edit_index
    task_text = entry.get()
    if not task_text:
        messagebox.showwarning("Input Error", "Please enter a task.")
        return

    if edit_index is None:
        # Add new task
        tasks.append({"text": task_text, "done": False})
    else:
        # Update existing task
        tasks[edit_index]["text"] = task_text
        messagebox.showinfo("Updated", "Task updated successfully.")
        edit_index = None
        add_btn.config(text="1️⃣ Add Task")

    entry.delete(0, tk.END)
    update_listbox()

# Step 2: Edit Task
def edit_task():
    global edit_index
    try:
        index = listbox.curselection()[0]
        entry.delete(0, tk.END)
        entry.insert(0, tasks[index]["text"])
        edit_index = index
        add_btn.config(text="✏️ Update Task")
    except:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

# Step 3: Delete Task
def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        update_listbox()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Step 4: Mark Task as Done
def mark_done():
    try:
        index = listbox.curselection()[0]
        tasks[index]["done"] = True
        update_listbox()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

# Step 5: Clear All Tasks
def clear_all():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        tasks.clear()
        update_listbox()

# Step 6: Update Listbox UI
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        display = f"{'✔️' if task['done'] else '❌'} {task['text']}"
        listbox.insert(tk.END, display)

# Step 7: Save Tasks to JSON File
def save_tasks():
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if file_path:
        with open(file_path, "w") as f:
            json.dump(tasks, f)
        messagebox.showinfo("Saved", "Tasks saved successfully!")

# Step 8: Load Tasks from JSON File
def load_tasks():
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file_path:
        try:
            with open(file_path, "r") as f:
                global tasks
                tasks = json.load(f)
            update_listbox()
        except:
            messagebox.showerror("Error", "Failed to load tasks.")

# Step 9: GUI Setup
window = tk.Tk()
window.title("Serial To-Do List")
window.geometry("460x560")
window.resizable(False, False)

# Step 9.1: Title
title = tk.Label(window, text="📝 Serial To-Do List", font=("Helvetica", 16))
title.pack(pady=10)

# Step 9.2: Entry for task input
entry = tk.Entry(window, width=40, font=("Helvetica", 14))
entry.pack(pady=5)

# Step 9.3: Buttons for each function
add_btn = tk.Button(window, text="1️⃣ Add Task", width=20, command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(window, width=50, height=12, font=("Helvetica", 12))
listbox.pack(pady=10)

edit_btn = tk.Button(window, text="2️⃣ ✏️ Edit Task", width=20, command=edit_task)
edit_btn.pack(pady=5)

done_btn = tk.Button(window, text="3️⃣ ✔️ Mark as Done", width=20, command=mark_done)
done_btn.pack(pady=5)

delete_btn = tk.Button(window, text="4️⃣ ❌ Delete Task", width=20, command=delete_task)
delete_btn.pack(pady=5)

clear_btn = tk.Button(window, text="5️⃣ 🧹 Clear All Tasks", width=20, command=clear_all)
clear_btn.pack(pady=5)

save_btn = tk.Button(window, text="6️⃣ 💾 Save Tasks", width=20, command=save_tasks)
save_btn.pack(pady=5)

load_btn = tk.Button(window, text="7️⃣ 📂 Load Tasks", width=20, command=load_tasks)
load_btn.pack(pady=5)

# Step 10: Run the application
window.mainloop()

