from tkinter import *

def click(event):
    global val
    val += event.widget.cget("text")
    text.set(val)

def clear():
    global val
    val = ""
    text.set("")

def equal():
    global val
    try:
        result = str(eval(val))
        text.set(result)
        val = result
    except Exception as e:
        text.set("Error")
        val = ""

val = ""
root = Tk()
root.title("Simple Calculator")
text = StringVar()

entry = Entry(root, textvar=text, font="Arial 20")
entry.pack(fill=BOTH, ipadx=8, pady=10, padx=10)

btns = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for row in btns:
    frame = Frame(root)
    frame.pack()
    for btn in row:
        b = Button(frame, text=btn, font="Arial 15", width=5, height=2)
        b.pack(side=LEFT, padx=5, pady=5)
        if btn == "=":
            b.bind("<Button-1>", lambda e: equal())
        else:
            b.bind("<Button-1>", click)

clear_btn = Button(root, text="C", font="Arial 15", command=clear)
clear_btn.pack(pady=5)

root.mainloop()
