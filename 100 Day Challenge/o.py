import tkinter
from tkinter import *

# --- setup ---
root = Tk()
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

# expression string
expression = ""

# --- callback functions ---
def btn_click(item):
    global expression
    expression += str(item)
    label_result.config(text=expression)

def btn_clear():
    global expression
    expression = ""
    label_result.config(text=expression)

def btn_equal():
    global expression
    try:
        # evaluate the expression and update display
        result = str(eval(expression))
        label_result.config(text=result)
        expression = result
    except Exception:
        label_result.config(text="Error")
        expression = ""

# --- display ---
label_result = Label(root, width=28, height=2, text="", font=("arial", 30), bg="#17161b", fg="#fff")
label_result.pack(pady=(20,0))

# --- buttons ---
btn_specs = [
    ("C", 10, 100, btn_clear, "#3697f5"),
    ("/", 150, 100, lambda: btn_click("/"), "#2a2d36"),
    ("%", 290, 100, lambda: btn_click("%"), "#2a2d36"),
    ("*", 430, 100, lambda: btn_click("*"), "#2a2d36"),

    ("7", 10, 200, lambda: btn_click(7), "#2a2d36"),
    ("8", 150, 200, lambda: btn_click(8), "#2a2d36"),
    ("9", 290, 200, lambda: btn_click(9), "#2a2d36"),
    ("-", 430, 200, lambda: btn_click("-"), "#2a2d36"),

    ("4", 10, 300, lambda: btn_click(4), "#2a2d36"),
    ("5", 150, 300, lambda: btn_click(5), "#2a2d36"),
    ("6", 290, 300, lambda: btn_click(6), "#2a2d36"),
    ("+", 430, 300, lambda: btn_click("+"), "#2a2d36"),

    ("3", 10, 400, lambda: btn_click(3), "#2a2d36"),
    ("2", 150, 400, lambda: btn_click(2), "#2a2d36"),
    ("1", 290, 400, lambda: btn_click(1), "#2a2d36"),
    ("=", 430, 400, btn_equal,        "#fe9037", 2, 1),  # rowspan=2

    ("0", 10, 500, lambda: btn_click(0), "#2a2d36", 11),
    (".", 290, 500, lambda: btn_click("."), "#2a2d36"),
]

for spec in btn_specs:
    text, x, y, cmd, color = spec[0], spec[1], spec[2], spec[3], spec[4]
    width = spec[5] if len(spec) > 5 else 5
    rowspan = spec[6] if len(spec) > 6 else 1
    Button(
        root, text=text, width=width, height=1 if rowspan==1 else 3,
        font=("arial", 30, "bold"), bd=1, fg="#fff", bg=color,
        command=cmd
    ).place(x=x, y=y)

# --- run ---
root.mainloop()
