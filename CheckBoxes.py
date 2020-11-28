from tkinter import *

root = Tk()
root.title("CheckBoxes")
root.geometry("400x400")

# looked at radio buttons previously, checkboxes are similar
# need to create a tkinter variable which is a little different
# need to create the variable to be passed through a checkbox widget
var = IntVar()

# now build a checkbox
# can also store default values for when the boxes are either checked or unchecked
# this is done by using onvalue=, and offvalue=
# note: if you change the type of your default variable from 0/1 to something else, you need to change your tkinter variable being passed

cb = Checkbutton(root, text="Check this box or else...", variable=var, onvalue=10, offvalue=20)

# can use the .deselect()/.select() method to make sure the checkbuttons initial state is checked or unchecked
cb.deselect()
cb.pack()

# for checkbuttons --> they show 0 if the box is unchecked, is 1 if box is checked
# simple button to check between on and off

def check():
    Label(root, text=var.get()).pack()

b = Button(root, text="see state of checkbox", command=check).pack()

root.mainloop()
