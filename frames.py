from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("frame example")

myFrame = LabelFrame(root, text="this is my kingdom frame")
#you can use padx and pady on labelFrames, but it doesnt increase size. Instead pads frame from outside window border
myFrame.pack(padx=10, pady=10)

# instead of putting button in the root, you place it in your frame
b1 = Button(myFrame, text="click me if you dare..")

# same thing applies to the button, but relative to the frame it is contained in
# note, you can actually pack multiple things into frame window (eg. multiple buttons)
b1.pack(padx=100, pady=100)

root.mainloop()
