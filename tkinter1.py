import tkinter as tk
w1 = tk.Tk()
w1.title("Adder")
w1.config(bg="lightblue")  # Used to change properties after construction.

# Can specify a `bg`, too:
l1 = tk.Label(w1, text="Please enter two numbers: ", fg="blue")
l1.config(bg="lightblue")
l1.grid(row=0, column=0)

e1 = tk.Entry(w1, width=30, borderwidth=5)
e1.config(bg="lightblue")
e1.grid(row=1, column=0)

e2 = tk.Entry(w1, width=30, borderwidth=5)
e2.config(bg="lightblue")
e2.grid(row=2, column=0)

s1 = tk.Scale(w1, to=1, from_=100)
s1.config(bg="lightblue")
s1.grid(row=3, column=1)  # Merges w/ button!


def b1Click():
    a = e1.get()
    b = e2.get()
    l1.config(text=f"{a} + {b} is {str(int(a) + int(b))}")


b1 = tk.Button(w1, text="Add (+)", command=b1Click)
b1.grid(row=3, column=0, columnspan=2)
b1.bind("<Button-1>", b1Click)
b1.config(bg="lightblue")

w1.mainloop()
