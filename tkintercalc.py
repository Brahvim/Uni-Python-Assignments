from tkinter import *
import math  # For `eval()` expressions!

calcRoot = Tk()
calcRoot.title("Cal-key")
calcRoot.configure(bg="#222")   # Dark background,
calcRoot.resizable(False, False)  # Disallow resizing.

# region Expression box.
calcEntryExpr = Entry(
    calcRoot,

    bd=8,
    bg="#fff",
    fg="#000",
    justify="right",
    font=("Arial", 20),
)
calcEntryExpr.pack(pady=15, padx=10)


def calcExprAppend(value):
    calcEntryExpr.insert(END, value)


def calcExprClear():
    calcEntryExpr.delete(0, END)


def calcExprEval():
    try:
        calcEntryExpr.delete(0, END)
        calcEntryExpr.insert(END, eval(calcEntryExpr.get()))
    except Exception as e:
        print(e)
        calcEntryExpr.delete(0, END)
        calcEntryExpr.insert(END, "Error")
# endregion


# region Buttons.
CALC_BTN_WIDTH = 5
CALC_BTN_HEIGHT = 2
CALC_BTN_FG = "white"
CALC_BTN_COLOR = "#333"  # Dark grey.

# region Row 1.
calcRow1 = Frame(calcRoot, bg="#222")
calcRow1.pack(pady=3)
Button(
    calcRow1,

    text="7",
    fg=CALC_BTN_FG,
    bg=CALC_BTN_COLOR,
    width=CALC_BTN_WIDTH,
    height=CALC_BTN_HEIGHT,
    command=lambda: calcExprAppend("7")
) \
    .pack(side=LEFT, padx=3)
Button(
    calcRow1,

    text="8",
    fg=CALC_BTN_FG,
    bg=CALC_BTN_COLOR,
    width=CALC_BTN_WIDTH,
    height=CALC_BTN_HEIGHT,
    command=lambda: calcExprAppend("8")
) \
    .pack(side=LEFT, padx=3)
Button(
    calcRow1,

    text="9",
    fg=CALC_BTN_FG,
    bg=CALC_BTN_COLOR,
    width=CALC_BTN_WIDTH,
    height=CALC_BTN_HEIGHT,
    command=lambda: calcExprAppend("9")
) \
    .pack(side=LEFT, padx=3)
Button(
    calcRow1,

    text="+",
    fg="white",
    bg="#ff9500",
    width=CALC_BTN_WIDTH,
    height=CALC_BTN_HEIGHT,
    command=lambda: calcExprAppend("+")
) \
    .pack(side=LEFT, padx=3)
# endregion

# region Row 2.
calcRow2 = Frame(calcRoot, bg="#222")
calcRow2.pack(pady=3)
Button(
    calcRow2,

    text="4",
    fg=CALC_BTN_FG,
    bg=CALC_BTN_COLOR,
    width=CALC_BTN_WIDTH,
    height=CALC_BTN_HEIGHT,
    command=lambda: calcExprAppend("4")
) \
    .pack(side=LEFT, padx=3)
Button(
    calcRow2,

    text="5",
    fg=CALC_BTN_FG,
    bg=CALC_BTN_COLOR,
    width=CALC_BTN_WIDTH,
    height=CALC_BTN_HEIGHT,
    command=lambda: calcExprAppend("5")
) \
    .pack(side=LEFT, padx=3)
Button(
    calcRow2,

    text="6",
    fg=CALC_BTN_FG,
    bg=CALC_BTN_COLOR,
    width=CALC_BTN_WIDTH,
    height=CALC_BTN_HEIGHT,
    command=lambda: calcExprAppend("6")
) \
    .pack(side=LEFT, padx=3)
Button(
    calcRow2,

    text="-",
    fg="white",
    bg="#ff9500",
    width=CALC_BTN_WIDTH,
    height=CALC_BTN_HEIGHT,
    command=lambda: calcExprAppend("-")
) \
    .pack(side=LEFT, padx=3)
# endregion

# region Row 3.
calcRow3 = Frame(calcRoot, bg="#222")
calcRow3.pack(pady=3)
Button(
    calcRow3,

    text="1",
    fg=CALC_BTN_FG,
    bg=CALC_BTN_COLOR,
    width=CALC_BTN_WIDTH,
    height=CALC_BTN_HEIGHT,
    command=lambda: calcExprAppend("1")
) \
    .pack(side=LEFT, padx=3)
Button(
    calcRow3,

    text="2",
    fg=CALC_BTN_FG,
    bg=CALC_BTN_COLOR,
    width=CALC_BTN_WIDTH,
    height=CALC_BTN_HEIGHT,
    command=lambda: calcExprAppend("2")
) \
    .pack(side=LEFT, padx=3)
Button(
    calcRow3,

    text="3",
    fg=CALC_BTN_FG,
    bg=CALC_BTN_COLOR,
    width=CALC_BTN_WIDTH,
    height=CALC_BTN_HEIGHT,
    command=lambda: calcExprAppend("3")
) \
    .pack(side=LEFT, padx=3)
Button(
    calcRow3,

    text="*",
    fg="white",
    bg="#ff9500",
    width=CALC_BTN_WIDTH,
    height=CALC_BTN_HEIGHT,
    command=lambda: calcExprAppend("*")
) \
    .pack(side=LEFT, padx=3)
# endregion

# region Row 4.
calcRow4 = Frame(calcRoot, bg="#222")
calcRow4.pack(pady=3)
Button(
    calcRow4,

    text="C",
    fg="white",
    bg="#d9534f",
    width=CALC_BTN_WIDTH,
    command=calcExprClear,
    height=CALC_BTN_HEIGHT,
) \
    .pack(side=LEFT, padx=3)
Button(
    calcRow4,

    text="0",
    fg=CALC_BTN_FG,
    bg=CALC_BTN_COLOR,
    width=CALC_BTN_WIDTH,
    height=CALC_BTN_HEIGHT,
    command=lambda: calcExprAppend("0")
) \
    .pack(side=LEFT, padx=3)
Button(
    calcRow4,

    text="=",
    fg="white",
    bg="#5cb85c",
    command=calcExprEval,
    width=CALC_BTN_WIDTH,
    height=CALC_BTN_HEIGHT,
) \
    .pack(side=LEFT, padx=3)
Button(
    calcRow4,

    text="/",
    fg="white",
    bg="#ff9500",
    width=CALC_BTN_WIDTH,
    height=CALC_BTN_HEIGHT,
    command=lambda: calcExprAppend("/")
) \
    .pack(side=LEFT, padx=3)
# endregion
# endregion

calcEntryExpr.bind("<Enter>", lambda x: calcExprEval())
calcRoot.mainloop()
