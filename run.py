# Student Management System (SMS) - Python Project using Tkinter GUI

# Importing Modules
from tkinter import *
import sqlite3

# Connecting to the database
connectDB = sqlite3.connect('student.db')
crDB = connectDB.cursor()
crDB.execute('create table if not exists student (roll_no integer primary key, name text, age integer, gender text, address text, phone integer)')
connectDB.commit()

# Creating instance of TK
root = Tk()

# Defining the variables
roll_no = IntVar()
name = StringVar()
age = IntVar()
gender = StringVar()
address = StringVar()
phone = IntVar()

# GUI Rendering code-block
root.title("Student Management System")
root.geometry("1350x700+0+0")

# Frames
Manage_Frame = Frame(root, bd=4, relief=RIDGE, bg="crimson")
Manage_Frame.place(x=20, y=100, width=450, height=580)

Detail_Frame = Frame(root, bd=4, relief=RIDGE, bg="crimson")
Detail_Frame.place(x=500, y=100, width=800, height=580)

# Labels
lbl_title = Label(Manage_Frame, text="Manage Students", bg="crimson", fg="white", font=("times new roman", 30, "bold"))
lbl_title.grid(row=0, columnspan=2, pady=20)
lbl_title.place(x=50, y=50)

lbl_roll = Label(Manage_Frame, text="Roll No.", bg="crimson", fg="white", font=("times new roman", 20, "bold"))



root.mainloop()



'''
# Student Management System (SMS) - Python Project using Tkinter GUI

# Importing Required Modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os

# Creating Database and Students Table
if not os.path.exists('Student.db'):
    # Create a new database if not exists
    conn = sqlite3.connect('Student.db')
    # Create a cursor to execute SQL commands
    c = conn.cursor()
    # Create table - Students
    c.execute("""CREATE TABLE students ( 
            student_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            """    )
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()

# Creating Window
class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        # Variables
        self.var_student_id = StringVar()
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_email = StringVar()

        # Title

        
        # Manage Frame
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=580)


        # Manage Frame Details
        m_title = Label(Manage_Frame, text="Manage Students", bg="crimson", fg="white", font=("times new roman", 30, "bold"))



        # First Name
        



conn.mainloop()
'''