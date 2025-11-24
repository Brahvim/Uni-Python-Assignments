# (Yes, this code is HIGHLY AI-generated, but it is what the teacher gave us.)

# Label Widget - Display text or images
import tkinter as tk

root = tk.Tk()
root.geometry("500x400")
root.title("Label Widget Demo")

# Creating different types of labels

# Simple label
label1 = tk.Label(root, text="Hello, Students!")

# Label with styling
label2 = tk.Label(
    root,
    text="Arial:20:bold,white,navy,+20x10",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="navy",
    padx=20,
    pady=10
)

# Label with border
label3 = tk.Label(
    root,
    text="Courier:14,ridge,3",
    font=("Courier", 14),
    relief="ridge",  # Border style: flat, raised, sunken, groove, ridge, solid
    borderwidth=3
)

# MVVM-style text container w/ callbacks:
dynamic_text = tk.StringVar()
dynamic_text.set("This text can change!")
label4 = tk.Label(root, textvariable=dynamic_text, font=("Arial", 12))

for i in [label1, label2, label3, label4]:
    i.pack(pady=10)

label1.pack(pady=(root.winfo_height() / 2))
for i in [label2, label3, label4]:
    i.pack(pady=10)

root.mainloop()

"""
LABEL PROPERTIES:
- text: Text to display
- font: (family, size, style)
- fg: Foreground (text) color
- bg: Background color
- padx/pady: Padding around text
- relief: Border style
- borderwidth: Border thickness
- textvariable: Variable for dynamic text
"""
