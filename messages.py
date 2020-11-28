from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("messages")

# make popup function, where message box is used
# multiple different ytpes of message boxes you can use
# show info, takes in 2 parameters: the first being the title bar that popup, then the second is the message that popups up in the windo
# most common message boxes: showinfo(), showwarning, showerror, askquestion, askyesno, askokcancel
def popup():
    response = messagebox.askokcancel("This is a popup", "first message box")
    # depending on the message box used, you can create if/else statements based on the response
    # for message boxes that ask things, yesno and okcancel return 1 (yes/ok) and 0 (ok/cancel). Alternatively, askquestion gives yesno response
    # the show messagebox types return ok

    if response == 1:
        Label(root, text="you hit yes").pack()

    else:
        Label(root, text="you hit cancel").pack()



# create a simple button with a command function called popup
Button(root, text="click here", command=popup).pack()

root.mainloop()
