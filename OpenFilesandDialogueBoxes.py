from tkinter import *
from tkinter import filedialog # is needed to open files anywhere on your computer

root = Tk()
root.title("Dialogue box")

# come back to this lesson --> @2:47:00
#initialdir allows us to get file from anywhere on computer --> note: still trying to figure it out
root.filename = filedialog.askopenfilename(initialdir="Bemnet/PycharmProjects/GUIs/images")


root.mainloop()
