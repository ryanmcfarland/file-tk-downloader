from tkinter import *
from tkinter.messagebox import *

def show_answer():
    blank.delete(0, END)
    Ans = int(num1.get()) + int(num2.get())
    blank.insert(0, Ans)


main = Tk()
Label(main, text = "Enter Num 1:").grid(row=0)
Label(main, text = "Enter Num 2:").grid(row=1)
Label(main, text = "The Sum is:").grid(row=2)


num1 = Entry(main)
num2 = Entry(main)
blank = Entry(main)


num1.grid(row=0, column=1)
num2.grid(row=1, column=1)
blank.grid(row=2, column=1)


Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W, pady=4)
Button(main, text='Show', command=show_answer).grid(row=4, column=1, sticky=W, pady=4)

mainloop()