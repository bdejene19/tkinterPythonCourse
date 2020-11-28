
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("first window")



# where new window is created
def new_window():
    global  img
    top = Toplevel()
    top.title("second window")
    img = ImageTk.PhotoImage(Image.open("img2.png"))
    # note: immage doesnt show up though in second window since it doesn't have access to img
    # to solve, turn img variable into a global one
    lbl = Label(top, image=img)
    lbl.pack()

    # can easily close second window using destroy method on top window (2nd window)
    btn2 = Button(top, text="exit window", command=top.destroy)
    btn2.pack()

myframe = LabelFrame(root, text="frame window")
myframe.pack(padx=100, pady=100)

Button(myframe, text="click here to move to new window", command=new_window).pack(padx=50, pady=50)

root.mainloop()
