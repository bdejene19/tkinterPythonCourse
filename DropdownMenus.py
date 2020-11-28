from tkinter import *

# lesson creates a drop down menu
root = Tk()
root.title("Drop-down menus")
root.geometry("400x400")

# create tkinter variable
clicked = StringVar()
clicked.set("Monday") # setting a default item

# creating a drop-down box. clicked is a tkinter variable
# note: in this case, its not like checkboxes or radiobuttons where you use variable=, but instead just the tkinter variable itself
drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
drop.pack()

# the way the drop variable created works, but is inefficient for large lists
# a more efficient way to do the same thing: create a list, and pass it through your optionmenu widget
# e.g. create python list
optionList = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

# create dropdown variable and pass list through
# remember to make a tkinter variable
days = StringVar()

# note: you have to use pass it as '*listName'
# when setting a default value while passing a list, you just set the index as shown
days.set(optionList[0])
dropDown2 = OptionMenu(root, days, *optionList)
dropDown2.pack()

root.mainloop()
