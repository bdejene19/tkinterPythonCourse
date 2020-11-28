from tkinter import *

# radio buttons are buttons thats you would see similar to filling out a survey
root = Tk()
root.title("Radio Button Example")

# using variable= attributes lets you know when someone clicks one of your radio buttons
# stores this value that can be used in future use


# variable x is a tkinter variable, works differently when you are creating it
# Note: since value= is an integer, tkinter variable x also needs to be an integer

def clicked(click_val):
    click_label = Label(root, text=click_val)
    click_label.pack()

'''
x = IntVar() # if you were passing a string as value, would use x=StringVar()

rdButton1 = Radiobutton(root, text="option 1", command=lambda: clicked(x.get()), variable=x, value=1).pack()
rdButton2 = Radiobutton(root, text="option 2", command=lambda: clicked(x.get()), variable=x, value=2).pack()

myLabel = Label(root, text=x.get()).pack()
'''
# however, sometimes you may have a lot of radio buttons, therefore, can use a loop using tuples
# tuple would function as (text, value)

# note: for some reason, doesn't work when values are the same
pizza_prices = [
    (5, "Pepperoni"),
    (4, "Cheese"),
    (6, "Vegeterian"),
    (7, "MeatLovers")
]
pizza_type = StringVar()
pizza_type.set("Pepperoni")

for cost,flavour in pizza_prices:
    Radiobutton(root, text=flavour, value=cost, variable=pizza_type, command=lambda:clicked(pizza_type.get())).pack(anchor=W)
root.mainloop()
