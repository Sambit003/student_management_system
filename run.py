# Student Management System (SMS) - Python Project using Tkinter GUI
# Importing Modules
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Connecting to the database
connectDB = sqlite3.connect('student.db')
crDB = connectDB.cursor()
crDB.execute('create table if not exists student (roll_no text, name text, age text, gender text, address text, phone text)')
connectDB.commit()

# Creating instance of TK
root = Tk()

# Defining the variables
roll_no = StringVar(root)
name = StringVar(root)
age = StringVar(root)
gender = StringVar(root)
address = StringVar(root)
phone = StringVar(root)


# GUI Rendering code-block
root.title("Student Management System")
root.geometry("1350x700+0+0")


# Frames
Manage_Frame = Frame(root, bd=4, relief=RIDGE, bg="crimson")
Manage_Frame.place(x=20, y=30, width=450, height=580)

Detail_Frame = Frame(root, bd=4, relief=RIDGE, bg="crimson")
Detail_Frame.place(x=500, y=30, width=750, height=580)


# MANAGE FRAME (WRITE ONLY FRAME)
# Labels
lbl_title = Label(Manage_Frame, text="Manage Students", bg="crimson", fg="white", font=("times new roman", 30, "bold"))
lbl_title.grid(row=0, columnspan=2, pady=20)
lbl_title.place(x=50, y=30)

lbl_roll = Label(Manage_Frame, text="Roll No.", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lbl_roll.place(x=50, y=100)

lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lbl_name.place(x=50, y=150)

lbl_age = Label(Manage_Frame, text="Age", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lbl_age.place(x=50, y=200)

lb1_gender = Label(Manage_Frame, text="Gender", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lb1_gender.place(x=50, y=250)

lbl_address = Label(Manage_Frame, text="Address", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lbl_address.place(x=50, y=300,height=50)

lbl_phone = Label(Manage_Frame, text="Phone", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lbl_phone.place(x=50, y=350)


# Entry
txt_roll = Entry(Manage_Frame, textvariable=roll_no, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
txt_roll.place(x=180, y=100)

txt_name = Entry(Manage_Frame, textvariable=name, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
txt_name.place(x=180, y=150)

txt_age = Entry(Manage_Frame, textvariable=age, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
txt_age.place(x=180, y=200)

txt_gender = Entry(Manage_Frame, textvariable=gender, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
txt_gender.place(x=180, y=250)

txt_address = Entry(Manage_Frame, textvariable=address, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
txt_address.place(x=180, y=300)

txt_phone = Entry(Manage_Frame, textvariable=phone, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
txt_phone.place(x=180, y=350)


# Button Functions
def btn_add():
    try:
        crDB.execute('insert into student values(?, ?, ?, ?, ?, ?)', (roll_no.get(), name.get(), age.get(), gender.get(), address.get(), phone.get()))
        connectDB.commit()
        messagebox.showinfo("Success", "Record has been inserted")
    except:
        messagebox.showerror("Error", "Record not inserted")

def btn_update():
    # SQL query to update the record
    try:
        crDB.execute('update student set name = ?, age = ?, gender = ?, address = ?, phone = ? where roll_no = ?', (name.get(), age.get(), gender.get(), address.get(), phone.get(), roll_no.get()))
        connectDB.commit()
        messagebox.showinfo("Success", "Record has been updated")
    except:
        messagebox.showerror("Error", "Record not updated")

def btn_delete():
    try: 
        crDB.execute('delete from student where roll_no = ?', (roll_no.get(),))
        connectDB.commit()
        messagebox.showinfo("Success", "Record has been deleted")
    except:
        messagebox.showerror("Error", "Record not found")

def btn_clear():
    roll_no.set('')
    name.set('')
    age.set('')
    gender.set('')
    address.set('')
    phone.set('')

def display_records():
   tree.delete(*tree.get_children())
   curr = crDB.execute('SELECT * FROM student')
   data = curr.fetchall()
   for records in data:
       tree.insert('', END, values=records)


# Buttons
btn_add = Button(Manage_Frame, text="Add", width=10, font=("times new roman", 14, "bold"), bg="blue", fg="white", command = btn_add)
btn_add.place(x=80, y=430)

btn_update = Button(Manage_Frame, text="Update", width=10, font=("times new roman", 14, "bold"), bg="blue", fg="white", command = btn_update)
btn_update.place(x=230, y=430)

btn_delete = Button(Manage_Frame, text="Delete", width=10, font=("times new roman", 14, "bold"), bg="blue", fg="white", command = btn_delete)
btn_delete.place(x=80, y=480)

btn_clear = Button(Manage_Frame, text="Clear", width=10, font=("times new roman", 14, "bold"), bg="blue", fg="white", command = btn_clear)
btn_clear.place(x=230, y=480)


# DETAIL FRAME (VIEW ONLY FRAME)
Label(Detail_Frame, text='Students Records', font=("times new roman", 24, "bold"), bg='red', fg='LightCyan').pack(side=TOP, fill=X)
tree = ttk.Treeview(Detail_Frame, height=100, selectmode=BROWSE,
                   columns=("Roll", "Name", "Age", "Gender", "Address", "Phone"))
X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
tree.heading('Roll', text='Roll No.', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Age', text='Age', anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
tree.heading('Address', text='Address', anchor=CENTER)
tree.heading('Phone', text='Phone', anchor=CENTER)
tree.column('#0', width=90, stretch=NO)
tree.column('#1', width=90, stretch=NO)
tree.column('#2', width=90, stretch=NO)
tree.column('#3', width=90, stretch=NO)
tree.column('#4', width=90, stretch=NO)
tree.column('#5', width=90, stretch=NO)

tree.place(y=50, relwidth=1, relheight=0.9, relx=0)
display_records()

root.update()
root.mainloop()