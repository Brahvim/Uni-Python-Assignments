import tkinter

ctCounter = 0
ctRoot = tkinter.Tk()
ctRoot.geometry("400x300")
ctRoot.title("Counter App")

# region Counter functions.
# Function to increase counter


def ctUp():
    ctCounter = ctCounter + 1
    ctLabelCount.config(text=str(ctCounter))


# Function to decrease counter
def ctDn():
    ctCounter -= 1
    ctLabelCount.config(text=str(ctCounter))


# Function to reset counter
def ctRst():
    # global ctCounter # Use this in lambdas I guess?
    ctCounter = 0
    ctLabelCount.config(text=str(ctCounter))
# endregion


ctLabelTitle = tkinter.Label(
    ctRoot,
    text="Counter App",
    font=("Arial", 20, "bold")
) \
    .pack(pady=20)

ctLabelCount = tkinter.Label(
    ctRoot,
    text="0",
    fg="blue",
    font=("Arial", 40, "bold"),
) \
    .pack(pady=20)

# region Buttons
ctButtonUp = tkinter.Button(
    ctRoot,

    fg="white",
    bg="green",
    command=ctUp,
    text="Increase",
    font=("Arial", 12)
) \
    .pack(pady=5)

ctButtonDn = tkinter.Button(
    ctRoot,

    bg="red",
    fg="white",
    command=ctDn,
    text="Decrease",
    font=("Arial", 12)
) \
    .pack(pady=5)

ctButtonRst = tkinter.Button(
    ctRoot,

    fg="white",
    bg="orange",
    text="Reset",
    command=ctRst,
    font=("Arial", 12)
) \
    .pack(pady=5)
# endregion

ctRoot.mainloop()

# label.config(text=...) = change the label text
