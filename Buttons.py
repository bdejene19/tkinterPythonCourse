from tkinter import *

root = Tk()

# button created, however, want it to do something
# can create a function to be executed when a button is clicked

def myClick():
    label1 = Label(root, text="Enter info")
    label1.pack()

# to execute function when clicked, use command=functionName without brackets
# can also control the colour of text using fg=, and control background colour with bg=
# can also change size of the button using padx= and pady=
button = Button(root, text="Sign up", command=myClick, fg="red", bg="red", padx=50, pady=50)
button.pack() # remember to place your GUI

root.mainloop()
