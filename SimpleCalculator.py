from tkinter import *

root = Tk()
root.title("SimpleCalculator")
entry = Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3)


# create function for command when button is clicked

def button_click(number):
    entry.insert(END, number) # inserts number into input field bar

def button_clear():
    entry.delete(0, END)

def math_function(sign):
    num1 = entry.get()
    global first_num

    global math_sign
    if sign == "+":
        math_sign = "+"

    elif sign == "-":
        math_sign = "-"

    elif sign == "/":
        math_sign = "/"

    elif sign == "*":
        math_sign = "*"

    first_num = float(num1)
    entry.delete(0, END)

def equal():
    num2 = entry.get()
    global second_num
    second_num = float(num2)
    entry.delete(0, END)

    if math_sign == "+":
        entry.insert(0, first_num + second_num)

    elif math_sign == "-":
        entry.insert(0, first_num - second_num)

    elif math_sign == "/":
        entry.insert(0, first_num/second_num)

    else:
        entry.insert(0, first_num * second_num)


# since function takes in a parameter, need to use lambda function in command
# syntax --> command=lambda: function(param)
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))


equal = Button(root, text="=", padx=40, pady=20, command=equal)
clear = Button(root, text="clear", padx=30, pady=20, command=button_clear)
add = Button(root, text="+", padx=40, pady=20, command=lambda: math_function("+"))
subtract = Button(root, text="-", padx=40, pady=20, command=lambda: math_function("-"))
divide = Button(root, text="/", padx=40, pady=20, command=lambda: math_function("/"))
multiply = Button(root, text="*", padx=40, pady=20, command=lambda: math_function("*"))


button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)


add.grid(row=1, column=3)
subtract.grid(row=2, column=3)
divide.grid(row=3, column=3)
multiply.grid(row=4, column=3)
equal.grid(row=4, column=1)
clear.grid(row=4, column=2)

root.mainloop()
