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
Manage_Frame.place(x=20, y=100, width=450, height=580)

Detail_Frame = Frame(root, bd=4, relief=RIDGE, bg="crimson")
Detail_Frame.place(x=500, y=100, width=800, height=580)

# MANAGE FRAME (WRITE ONLY FRAME)
# Labels
lbl_title = Label(Manage_Frame, text="Manage Students", bg="crimson", fg="white", font=("times new roman", 30, "bold"))
lbl_title.grid(row=0, columnspan=2, pady=20)
lbl_title.place(x=50, y=50)

lbl_roll = Label(Manage_Frame, text="Roll No.", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lbl_roll.place(x=50, y=100)

lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lbl_name.place(x=50, y=150)

lbl_age = Label(Manage_Frame, text="Age", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lbl_age.place(x=50, y=200)

lb1_gender = Label(Manage_Frame, text="Gender", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lb1_gender.place(x=50, y=250)

lbl_address = Label(Manage_Frame, text="Address", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lbl_address.place(x=50, y=300, height=50)

lbl_phone = Label(Manage_Frame, text="Phone", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lbl_phone.place(x=50, y=350)


# Entry
txt_roll = Entry(Manage_Frame, textvariable=roll_no, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
txt_roll.place(x=200, y=100)

txt_name = Entry(Manage_Frame, textvariable=name, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
txt_name.place(x=200, y=150)

txt_age = Entry(Manage_Frame, textvariable=age, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
txt_age.place(x=200, y=200)

txt_gender = Entry(Manage_Frame, textvariable=gender, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
txt_gender.place(x=200, y=250)

txt_address = Entry(Manage_Frame, textvariable=address, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
txt_address.place(x=200, y=300, height=50)

txt_phone = Entry(Manage_Frame, textvariable=phone, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
txt_phone.place(x=200, y=350)

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

# Buttons
btn_add = Button(Manage_Frame, text="Add", width=10, font=("times new roman", 14, "bold"), bg="blue", fg="white", command = btn_add)
btn_add.place(x=50, y=450)

btn_update = Button(Manage_Frame, text="Update", width=10, font=("times new roman", 14, "bold"), bg="blue", fg="white", command = btn_update)
btn_update.place(x=150, y=450)

btn_delete = Button(Manage_Frame, text="Delete", width=10, font=("times new roman", 14, "bold"), bg="blue", fg="white", command = btn_delete)
btn_delete.place(x=250, y=450)

btn_clear = Button(Manage_Frame, text="Clear", width=10, font=("times new roman", 14, "bold"), bg="blue", fg="white", command = btn_clear)
btn_clear.place(x=350, y=450)


# DETAIL FRAME (VIEW ONLY FRAME)
# Labels
lbl_title = Label(Detail_Frame, text="Student Details", bg="crimson", fg="white", font=("times new roman", 30, "bold"))
lbl_title.grid(row=0, columnspan=2, pady=20)
lbl_title.place(x=250, y=50)

lbl_roll = Label(Detail_Frame, text="Roll No.", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lbl_roll.place(x=50, y=100)

lbl_name = Label(Detail_Frame, text="Name", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lbl_name.place(x=50, y=150)

lbl_age = Label(Detail_Frame, text="Age", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lbl_age.place(x=50, y=200)

lb1_gender = Label(Detail_Frame, text="Gender", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lb1_gender.place(x=50, y=250)

lbl_address = Label(Detail_Frame, text="Address", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lbl_address.place(x=50, y=300, height=50)

lbl_phone = Label(Detail_Frame, text="Phone", bg="crimson", fg="black", font=("times new roman", 20, "bold"))
lbl_phone.place(x=50, y=350)


# columns=("roll", "name", "age", "gender", "address", "phone")
# student_table = ttk.Treeview(root, columns=("roll", "name", "age", "gender", "address", "phone"))
# dict_student=[]

# for item in dict_student:
#     dict_student.insert('', 'end', values=item)

# def item_selected(event):
#     for selected_item in dict_student.selection():
#         piece = dict_student.item(selected_item)
#         record = piece['values']
#         # show a message
#         showinfo(title='Information', message=','.join(record))


# student_table.bind('<<TreeviewSelect>>', item_selected)

# student_table.grid(row=0, column=0, sticky='new')

Display_roll = Label(Detail_Frame, textvariable=roll_no, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
Display_roll.place(x=200, width=400, y=100)

Display_name = Label(Detail_Frame, textvariable=name, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
Display_name.place(x=200, width=400, y=100)

Display_age = Label(Detail_Frame, textvariable=age, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
Display_age.place(x=200, width=400, y=100)

Display_gender = Label(Detail_Frame, textvariable=gender, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
Display_gender.place(x=200, width=400, y=100)   

Display_address = Label(Detail_Frame, textvariable=address, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
Display_address.place(x=200, width=400, y=100)

Display_phone = Label(Detail_Frame, textvariable=phone, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
Display_phone.place(x=200, width=400, y=100)




# Scrollbar
scroll_x = Scrollbar(Detail_Frame, orient=HORIZONTAL)
scroll_y = Scrollbar(Detail_Frame, orient=VERTICAL)


'''
# Without Treeview
# Table Frame
Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="white", highlightbackground="black", highlightthickness=2)
Table_Frame.place(x=50, y=100, width=700, height=400)

# Scrollbar
scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

# Student Table

# Treeview
What is Treeview? 
Treeview is a widget which is used to display the data in a tree structure.


student_table = (ttk.Treeview(root, columns=("roll", "name", "age", "gender", "address", "phone"), height=12, selectmode="extended",show='headings'))


# define headings
# student_table.heading('name', text='Name')
# student_table.heading('roll', text='Roll')
# student_table.heading('age', text='Age')
# student_table.heading('gender', text='Gender')
# student_table.heading('address', text='Address')
# student_table.heading('phone', text='Phone')

# # generate sample data
# contacts = []
# while len(contacts) < 100:
#     contacts.append((f'Name- {n}', f'Roll- {n}',f'Age-{n}',f'Gender-{n}',f'Address-{n}',f'Phone-{n}'))
#     n += 1

# create a treeview insert function
def treeview_insert():
    for contact in contacts:
        student_table.insert('', 'end', values=contact)

# insert data into the treeview
treeview_insert()

# add data to the treeview
for student in student_table:
    student_table.insert('', Tk.after() , values=student)

def item_selected(event):
    for selected_item in student_table.selection():
        item = student_table.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


student_table.bind('<<TreeviewSelect>>', item_selected)

student_table.grid(row=0, column=0, sticky='new')

# Scrollbar
scroll_x = Scrollbar(Detail_Frame, orient=HORIZONTAL)
scroll_y = Scrollbar(Detail_Frame, orient=VERTICAL)
'''


root.mainloop()