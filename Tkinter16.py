
from tkinter import *
window = Tk()
window.title("Welcome")
window.geometry('350x200')
spin = Spinbox(window, from_=0, to=9000, width=2)
spin.grid(column=0,row=0)
window.mainloop()

