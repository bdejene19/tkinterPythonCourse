from tkinter import *

# create a scroll index for your window in this program
# to do that, you use the scale widget --> is like all other widgets (e.g. Buttons, Radiobuttons, Entrys, and Labels)
root = Tk()
root.title("ScrollingSlider Test")
root.geometry("460x460")

# only other parameter it takes in than the window its put in, is the distance you want it to span --> note: vertical is the default
# done using 'from_=" and 'to='
vertical = Scale(root, from_=0, to=200)

# for sliders, you don't want to create them and also pack them in the same line
vertical.pack()


# horizontal slider
horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

# function allows to get value of slider after clicking button
def slider():
    lbl = Label(root, text=horizontal.get())
    lbl.pack()

indicator = Button(root, text="slider indicator", command=slider)
indicator.pack()

# however, what if you wanted to have the value of your slider change as you moved the slider?
# pass in a command to slider scale widget

root.mainloop()
