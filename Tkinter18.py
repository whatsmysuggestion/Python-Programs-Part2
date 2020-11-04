from tkinter import *
counter = 1
def counter_label(label):
    counter = 1

    def count():
        global counter
        counter += 1# count =count+2
        label.config(text=str(counter))
        label.after(10, count)

    count()

root =Tk()
root.title("Counting Seconds")
label = Label(root, fg="dark red")
label.pack()
counter_label(label)
button = Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()