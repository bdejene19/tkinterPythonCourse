
# code creates photo gallery GUI application
# imports images and puts them onto a canvas, can scroll through them with left and right clicker in window, also has exit button


# import necessary packages
from tkinter import *
from PIL import ImageTk, Image

# create canvas with title
root = Tk()
root.title("MyGallery")

# opening images to make them accessible
img1 = ImageTk.PhotoImage(Image.open("cupcakes.jpg"))
img2 = ImageTk.PhotoImage(Image.open("buddha man.jpg"))
img3 = ImageTk.PhotoImage(Image.open("electric man.jpg"))
img4 = ImageTk.PhotoImage(Image.open("birthdayboy.jpg"))
img5 = ImageTk.PhotoImage(Image.open("parents.jpg"))

# now have list of images and length
img_list = [img1, img2, img3, img4, img5]
list_length = len(img_list)

# have a global index to know which picture in gallery you're looking at as you scroll through
global index
index = 0
# is used further on, places first image on screen
global img_label
img_label = Label(root, image=img1, width=600, height=540)
img_label.grid(row=0, column=1, columnspan=3)

# function for forward button
# increaes index by one, deletes current label, then places the image label of the next index
# note: forward and back buttons were created to maintain their command when a forward button is clicked
# e.g. back button initially disabled, but when you go forward, override back button to be enabled again
def forward():
    global index
    index += 1

    global img_label
    img_label.grid_forget()
    img_label = Label(root, image=img_list[index], width=700, height=640)
    forward_button = Button(root, text=">>", command=forward)
    back_button = Button(root, text="<<", command=backward) # is now enabled

    # disable forward button when reached end of image list
    if index == list_length-1:
        forward_button = Button(root, text=">>", command=forward, state=DISABLED)

    # place label and buttons on canvas
    img_label.grid(row=0, column=1, columnspan=3)
    forward_button.grid(row=4, column=5)
    back_button.grid(row=4, column=0)
    exit.grid(row=4, column=2)

# lowers index by one
# deletes current label to show previous image label

def backward():
    global index
    index -= 1

    global img_label
    img_label.grid_forget()
    img_label = Label(root, image=img_list[index], width=700, height=640)

    forward_button = Button(root, text=">>", command=forward)

    if index == 0:
        back_button = Button(root, text="<<", command=backward, state=DISABLED)

    else:
        back_button = Button(root, text="<<", command=backward)

    img_label.grid(row=0, column=1)

    back_button.grid(row=4, column=0)
    forward_button.grid(row=4, column=5)
    exit.grid(row=4, column=1)

back_button = Button(root, text="<<", command=backward, state=DISABLED)
forward_button = Button(root, text=">>", command=forward)
exit = Button(root, text="exit", command=root.quit)

forward_button.grid(row=4, column=5)
back_button.grid(row=4, column=0)
exit.grid(row=4, column=2)



root.mainloop()
