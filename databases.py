from tkinter import *
import sqlite3

root = Tk()
root.title("Drop-down menus")
root.geometry("400x400")

# adding a database to anytype of program vastly improves the power of that program --> imported sqlite3
# first thing we need to do is create a data base or connect to one
# to do that, we need to create a connection to the database, therefore, need to create a variable
conn = sqlite3.connect("address_book.db") # .connect() is how we connect to the database we want


# now need to create a cursor
# cursor: executes commands that allows to send things off and return things from the database
cursor = conn.cursor()

# need to come create a table to hold values and entries
cursor.execute("""CREATE TABLE addresses (
first_name, text,
""")

# commit changes to database
conn.commit()

# then always close your database
conn.close()


root.mainloop()
