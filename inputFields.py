from tkinter import *

root = Tk()

# creating an input field, can change size and colour of input field
# can also change borderwidth if you want
myEntry = Entry(root, width=50, bg="blue", fg="red", borderwidth=5)
myEntry.pack()

# can have text already inside your input field using .insert() method
myEntry.insert(0, "Enter name: ")

def clicker():
    textBox = Label(root, text= "hello " +myEntry.get())
    textBox.pack()

button = Button(root, text="Sign up", command=clicker, bg="black", fg='red')
button.pack()
root.mainloop()
