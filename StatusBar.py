
# adding staus bar o gallery viewer

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
img_label = Label(root, image=img1, width=400, height=500)
img_label.grid(row=0, column=1, columnspan=3)

# to give status bar border and sunken look, us bd= (border) and relief= for sunken
global status
status = Label(root, text=f'Image {index + 1} of ' + str(list_length), bd=1, relief=SUNKEN)

# while using the grid system, can use sticky to spread distance of status to go entire length of window
# works in a compass manner, using N, W, S, E
# can also anchor your statusbar to a specific location, e.g. E
status.grid(row=3, column=4, columnspan=2, sticky=W+E)



# function for forward button
# increaes index by one, deletes current label, then places the image label of the next index
# note: forward and back buttons were created to maintain their command when a forward button is clicked
# e.g. back button initially disabled, but when you go forward, override back button to be enabled again
def forward():
    global index
    index += 1

    global img_label
    img_label.grid_forget()
    img_label = Label(root, image=img_list[index], width=400, height=500)
    back_button = Button(root, text="<<", command=backward, padx=40, pady=10)
    forward_button = Button(root, text=">>", command=forward, padx=40, pady=10)
    exit = Button(root, text="exit", command=root.quit, padx=40, pady=10) # is now enabled

    status = Label(root, text=f'Image {index + 1} of ' + str(list_length), bd=1, relief=SUNKEN)
    status.grid(row=3, column=4, columnspan=2, sticky=W + E)

    # disable forward button when reached end of image list
    if index == list_length-1:
        forward_button = Button(root, text=">>", command=forward, state=DISABLED, padx=40, pady=10)

    # place label and buttons on canvas
    img_label.grid(row=0, column=1, columnspan=5)
    forward_button.grid(row=4, column=6, padx=50, pady=25)
    back_button.grid(row=4, column=0, padx=50, pady=25)
    exit.grid(row=4, column=3, padx=3, pady=5)

# lowers index by one
# deletes current label to show previous image label

def backward():
    global index
    index -= 1

    global img_label
    img_label.grid_forget()
    img_label = Label(root, image=img_list[index], width=400, height=500)

    forward_button = Button(root, text=">>", command=forward, padx=40, pady=10)
    if index == 0:
        back_button = Button(root, text="<<", command=backward, state=DISABLED, padx=40, pady=10)

    else:
        back_button = Button(root, text="<<", command=backward, padx=40, pady=10)

    status = Label(root, text=f'Image {index + 1} of ' + str(list_length), bd=1, relief=SUNKEN)
    status.grid(row=3, column=4, columnspan=2, sticky=W + E)

    img_label.grid(row=0, column=1)
    img_label.grid(row=0, column=1, columnspan=5)
    forward_button.grid(row=4, column=6)
    back_button.grid(row=4, column=0)
    exit.grid(row=4, column=3)

back_button = Button(root, text="<<", command=backward, state=DISABLED, padx=40, pady=10)
forward_button = Button(root, text=">>", command=forward, padx=40, pady=10)
exit = Button(root, text="exit", command=root.quit, padx=40, pady=10)
status = Label(root, text=f'Image {index + 1} of ' + str(list_length), bd=1, relief=SUNKEN)

status.grid(row=3, column=4, columnspan=2, sticky=W+E)
img_label.grid(row=0, column=1, columnspan=5)
forward_button.grid(row=4, column=6)
back_button.grid(row=4, column=0)
exit.grid(row=4, column=3, padx=4)



root.mainloop()

