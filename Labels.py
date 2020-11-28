
# always need to import tkinter when creating GUIs
from tkinter import *

# always create a root at the beginning of your GUI using Tk()
myRoot = Tk()

# to create a GUI, you need to create the type, then place it in your root
# creating GUI type - label. When creating a label, requires 2 parameters:
# 1) where your placing it (e.g. myRoot) and  2) its text
myLabel = Label(myRoot, text="Hello world")
myLabel2 = Label(myRoot, text="Hello world")


# GUI created, now we place it using either .pack() - quick but clumsy, or .grid(row=x, column=y)
myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
# to allow GUI to continuously run, always need to put '.mainloop()' after your root
myRoot.mainloop()
