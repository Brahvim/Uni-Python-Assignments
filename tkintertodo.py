from tkinter import messagebox
import tkinter

tdRoot = tkinter.Tk()
tdRoot.title("Todos App")
tdRoot.geometry("450x500")
tdRoot.config(bg="lightgreen")

# region Tasklist functions.


def tdTaskAdd():
    task = tdEntryTask.get()
    if task == "":
        messagebox.showwarning("Empty", "Please enter a task!")
    else:
        tdListboxTasks.insert(tkinter.END, task)
        tdEntryTask.delete(0, tkinter.END)
        messagebox.showinfo("Added", "Task added successfully!")


def tdTaskPop():
    try:
        selected = tdListboxTasks.curselection()[0]
        tdListboxTasks.delete(selected)
        messagebox.showinfo("Deleted", "Task deleted!")
    except:
        messagebox.showwarning(
            "No Selection", "Please select a task to delete!")


def tdTaskClearAll():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        tdListboxTasks.delete(0, tkinter.END)
# endregion


tkinter.Label(
    tdRoot,

    bg="green",
    fg="white",
    text="📝 My To-Do List",
    font=("Arial", 20, "bold"),
) \
    .pack(fill="x", pady=10)

tdFrameTask = tkinter.Frame(tdRoot, bg="lightgreen")
tdFrameTask.pack(pady=10)

tkinter.Label(
    tdFrameTask,
    bg="lightgreen",
    text="Enter Task:",
    font=("Arial", 12),
) \
    .pack(side="left", padx=5)

tdEntryTask = tkinter.Entry(
    tdFrameTask,

    width=25,
    font=("Arial", 12),
)
tdEntryTask.pack(side="left", padx=5)

tdButtonAdd = tkinter.Button(
    tdFrameTask,

    bg="blue",
    fg="white",
    text="Add",
    font=("Arial", 11),
    command=tdTaskAdd,
)
tdButtonAdd.pack(side="left", padx=5)

# `tk.Listbox::delete(item)`            removes `item`,
# `tk.Listbox::curselection()`          gets selection,
# `tk.Listbox::insert(tk.END, item)`    appends `item`.
tdListboxTasks = tkinter.Listbox(
    tdRoot,

    width=40,
    height=12,
    font=("Arial", 12),
    selectmode=tkinter.SINGLE,
)
tdListboxTasks.pack(pady=10)

tdFrameBottomBar = tkinter.Frame(tdRoot, bg="lightgreen")
tdFrameBottomBar.pack(pady=10)

tdButtonPop = tkinter.Button(
    tdFrameBottomBar,

    width=12,
    bg="red",
    fg="white",
    command=tdTaskPop,
    text="Delete Task",
    font=("Arial", 11),
)
tdButtonPop.pack(side="left", padx=5)

tdButtonClear = tkinter.Button(
    tdFrameBottomBar,

    width=12,
    fg="white",
    bg="orange",
    text="Clear All",
    font=("Arial", 11),
    command=tdTaskClearAll,
)
tdButtonClear.pack(side="left", padx=5)

tdRoot.mainloop()
