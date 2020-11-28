
from tkinter import *
from PIL import ImageTk, Image

#PIL = python imaging library, required to import images


# to put in an icon for an application (e.g. google chrome, safari icon), use iconbitmap
# syntax: root.iconbitmap(location of icon saved)
root = Tk()
root.title("Icon, Images and Exit Buttons")

# importing an image is a little trickier
my_image = ImageTk.PhotoImage(Image.open("thirsty bitch.jpg"))
bottle_image = Label(image=my_image, padx= 10, pady=20)
bottle_image.pack()










# quiting a progrgam is pretty easy too
exit_button = Button(root, text="exit button", command=root.quit)
exit_button.pack()

root.mainloop()
G
