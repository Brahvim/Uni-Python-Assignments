# All of this comes thanks to [ http://stackoverflow.com/questions/15246523/ ]!
from tkinter.messagebox import showerror
import tkinter as tk


def cbckBtn():
    raise Exception("I'm Bad!")


# Override this method here GLOBALLY *but* only for the very next app, or in a `tk.Tk` subclass:
tk.Tk.report_callback_exception = lambda p_errorType, p_error, p_stacktrace: showerror(
    icon="error", message=str(p_stacktrace))

w = tk.Tk()
tk.Button(master=w, text="Raise an exception!", command=cbckBtn).pack()
w.mainloop()
