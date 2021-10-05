import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import tkcalendar
import sqlite3

blood_val = 30


# dimensions, name and colour for the login main page
n = 1920
m = 1080
mainWindow = tkinter.Tk()
mainWindow.title("Login Page")
mainWindow.geometry("1920x1080+-5+-1")
mainWindow.configure(background="white")

#  to find the logo in files
photos = [ImageTk.PhotoImage(Image.open("login_photo.jpg")), ImageTk.PhotoImage(Image.open("Password.jpg")),
          ImageTk.PhotoImage(Image.open("Logo2.jpg"))]

#  to place the logo on the login page
background = tkinter.Label(mainWindow, image=photos[2]).pack(fill="y")

# The following are functions for buttons (functions as in commands)
# register command when register button is pressed


def register():

    # to make another window that contains registration details
    register_window = Toplevel()
    register_window.title("Register")
    register_window.geometry("1920x1080+-5+-1")
    register_window.configure(background="red4")

    # to make labels and entries such as username, email ,DOB in this page
    register_frame = tkinter.LabelFrame(register_window, bd=15, relief="groove", bg="dark blue")
    register_frame.place(x=600, y=50, width=650, height=800)
    label1 = tkinter.Label(register_frame, text="Sign Up", font=("caliber", 30, "bold"), fg="gold", bg="dark blue")
    label1.place(x=180, y=10)
    username_label = tkinter.Label(register_frame, text="Username", font=("caliber", 25, "bold"), bg="dark blue",
                                   fg="white")
    username_label.place(x=10, y=110)
    password_label = tkinter.Label(register_frame, text="Password", font=("caliber", 25, "bold"), bg="dark blue",
                                   fg="white")
    password_label.place(x=10, y=200)
    email_label = tkinter.Label(register_frame, text="Email ", font=("caliber", 25, "bold"), bg="dark blue",
                                fg="white")
    email_label.place(x=10, y=290)
    gender_label = tkinter.Label(register_frame, text="Gender", font=("caliber", 25, "bold"), bg="dark blue",
                                 fg="white")
    gender_label.place(x=10, y=380)
    contact_label = tkinter.Label(register_frame, text="Contact", font=("caliber", 25, "bold"), bg="dark blue",
                                  fg="white")
    contact_label.place(x=10, y=470)
    dob_label = tkinter.Label(register_frame, text="D.O.B", font=("caliber", 25, "bold"), bg="dark blue",
                              fg="white")
    dob_label.place(x=10, y=560)
    username_entry = tkinter.Entry(register_frame, font="large_font", relief="groove")
    username_entry.place(x=230, y=120)
    password_entry = tkinter.Entry(register_frame, font="large_font", relief="groove")
    password_entry.place(x=230, y=210)
    email_entry = tkinter.Entry(register_frame, font="large_font", relief="groove")
    email_entry.place(x=230, y=300)
    contact_entry = tkinter.Entry(register_frame, font="large_font")
    contact_entry.place(x=230, y=480)
    gender_entry = ttk.Combobox(register_frame, width=20, state="readonly", font="large_font")
    gender_entry['values'] = ("Male", "Female", "Other")
    gender_entry.place(x=230, y=390)
    dob_entry = tkcalendar.DateEntry(register_frame, font=("large_font", 16, "italic"))
    dob_entry.place(x=230, y=570)

    # when sigh_up is pressed after registration details are filled
    def on_signup():
        if len(str(username_entry.get())) >= 2:
            if len(password_entry.get()) == 4:
                if email_entry.get()[-4:] == ".com":
                    if len(contact_entry.get()) == 10:
                        print("Check ok!")
                        print(dob_entry.get_date())
                    else:
                        messagebox.showerror("Error", "Contact not valid!!", parent=register_window)
                else:
                    messagebox.showerror("Error", "Invalid Email Address!!", parent=register_window)
            else:
                messagebox.showerror("Error", "Password should be a number with 4 digits!!", parent=register_window)
        else:
            messagebox.showerror("Error", "Invalid Username!!", parent=register_window)

    # button frame
    button_frame = Frame(register_frame, bd=5, relief="ridge", bg="dark blue")
    button_frame.place(x=10, y=660, width=600, height=110)

    # Sign up button
    signup_button = tkinter.Button(button_frame, text="    Sign Up   ", bg="green", fg="white",
                                   font=("caliber", 18, "italic"), relief="raised", command=on_signup)
    signup_button.place(x=20, y=23)

    back_button = tkinter.Button(button_frame, text="    Back   ", bg="green", fg="white",
                                 font=("caliber", 18, "italic"), relief="raised", command=register_window.destroy)
    back_button.place(x=230, y=23)

    # when quit is pressed
    def on_quit():
        register_window.destroy()
        mainWindow.destroy()

    clear_button = tkinter.Button(button_frame, text="    Exit   ", bg="green", fg="white",
                                  font=("caliber", 18, "italic"), relief="raised", command=on_quit)
    clear_button.place(x=430, y=23)

    register_window.mainloop()


def login():

    def on_clear():
        name_entry.delete(0, 'end')
        mail_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')
        requirement_entry.delete(0, 'end')
        blood_entry.delete(0, 'end')

    def on_del():
        def in_del():
            db = sqlite3.connect("request.sqlite")
            cursor = db.cursor()
            cursor.execute("SELECT * FROM donation")
            print(cursor.fetchall())
            name2 = delete_label_entry.get()
            cursor.execute("DELETE FROM donation WHERE (name = ?)", [name2])
            db.commit()
            messagebox.showinfo("Deleted", "Data Deleted Successfully!!", parent=delete_page)
            cursor.execute("SELECT * FROM donation")
            print(cursor.fetchall())
            cursor.close()
            db.close()
            delete_page.destroy()

            # to destroy 30 once donated
            a_positive_entry.destroy()
            a_negative_entry.destroy()
            b_positive_entry.destroy()
            b_negative_entry.destroy()
            ab_positive_entry.destroy()
            ab_negative_entry.destroy()
            b_negative_entry.destroy()
            o_positive_entry.destroy()
            o_negative_entry.destroy()

            # to display the new quantity of the set blood
            a_pos_entry = tkinter.Entry(values, textvariable=a_pos_str, state="disabled",
                                        font=("large_font", 15, "bold"))
            a_pos_entry.place(x=100, y=15, width=40)
            a_neg_entry = tkinter.Entry(values, textvariable=a_neg_str, state="disabled",
                                        font=("large_font", 15, "bold"))
            a_neg_entry.place(x=100, y=50, width=40)
            b_pos_entry = tkinter.Entry(values, textvariable=b_pos_str, state="disabled",
                                        font=("large_font", 15, "bold"))
            b_pos_entry.place(x=100, y=85, width=40)
            b_neg_entry = tkinter.Entry(values, textvariable=b_neg_str, state="disabled",
                                        font=("large_font", 15, "bold"))
            b_neg_entry.place(x=100, y=120, width=40)
            ab_pos_entry = tkinter.Entry(values, textvariable=ab_pos_str, state="disabled",
                                         font=("large_font", 15, "bold"))
            ab_pos_entry.place(x=100, y=155, width=40)
            ab_neg_entry = tkinter.Entry(values, textvariable=ab_neg_str, state="disabled",
                                         font=("large_font", 15, "bold"))
            ab_neg_entry.place(x=100, y=190, width=40)
            o_pos_entry = tkinter.Entry(values, textvariable=o_pos_str, state="disabled",
                                        font=("large_font", 15, "bold"))
            o_pos_entry.place(x=100, y=225, width=40)
            o_neg_entry = tkinter.Entry(values, textvariable=o_neg_str, state="disabled",
                                        font=("large_font", 15, "bold"))
            o_neg_entry.place(x=100, y=260, width=40)

        delete_page = Toplevel()
        delete_page.title("Delete Entry")
        delete_page.geometry("480x270")
        delete_page.configure(bg="maroon")
        delete_page.wm_attributes("-alpha", 0.95)
        delete_label = tkinter.Label(delete_page, font=("caliber", 15, "bold"), text="Enter Name", fg="gold",
                                     bg="dark blue")
        delete_label.place(x=30, y=30)
        delete_label_entry = tkinter.Entry(delete_page, font="large_font", bg="white")
        delete_label_entry.place(x=180, y=33)
        delete_button = tkinter.Button(delete_page, text="Delete Data", font="large_font", bg="dark blue", fg="gold",
                                       command=in_del)
        delete_button.place(x=150, y=120)

    def on_add():
        if username_entry_user.get() == name_entry.get():
            if mail_entry.get()[-4:] == ".com":
                if len(phone_entry.get()) == 10:
                    if 0 < int(requirement_entry.get()) < 6:
                        db = sqlite3.connect("request.sqlite")
                        db.execute("CREATE TABLE IF NOT EXISTS donation(name TEXT, email TEXT, phone INTEGER,"
                                   " requirement TEXT, blood TEXT)")
                        db.execute("INSERT INTO donation(name, email, phone, requirement, blood) VALUES(?, ?, ?, ?, ?)",
                                   (name_entry.get(), mail_entry.get(), phone_entry.get(),   requirement_entry.get(),
                                    blood_entry.get()))
                        cursor = db.cursor()
                        cursor.execute("SELECT * FROM donation")
                        print(cursor.fetchall())
                        db.commit()
                        cursor.close()
                        db.close()

                        # to destroy 30 once donated
                        a_positive_entry.destroy()
                        a_negative_entry.destroy()
                        b_positive_entry.destroy()
                        b_negative_entry.destroy()
                        ab_positive_entry.destroy()
                        ab_negative_entry.destroy()
                        b_negative_entry.destroy()
                        o_positive_entry.destroy()
                        o_negative_entry.destroy()

                        if blood_entry.get() == "B+":
                            b_pos_str.set(int(b_pos_str.get()) - int(requirement_entry.get()))
                        elif blood_entry.get() == "B-":
                            b_neg_str.set(int(b_neg_str.get()) - int(requirement_entry.get()))
                        elif blood_entry.get() == "A+":
                            a_pos_str.set(int(a_pos_str.get()) - int(requirement_entry.get()))
                        elif blood_entry.get() == "A-":
                            a_neg_str.set(int(a_neg_str.get()) - int(requirement_entry.get()))
                        elif blood_entry.get() == "AB+":
                            ab_pos_str.set(int(ab_pos_str.get()) - int(requirement_entry.get()))
                        elif blood_entry.get() == "AB-":
                            ab_neg_str.set(int(ab_neg_str.get()) - int(requirement_entry.get()))
                        elif blood_entry.get() == "O+":
                            o_pos_str.set(int(o_pos_str.get()) - int(requirement_entry.get()))
                        elif blood_entry.get() == "O-":
                            o_neg_str.set(int(o_neg_str.get()) - int(requirement_entry.get()))

                        # to display the new quantity of the set blood
                        a_pos_entry = tkinter.Entry(values, textvariable=a_pos_str, state="disabled",
                                                    font=("large_font", 15, "bold"))
                        a_pos_entry.place(x=100, y=15, width=40)
                        a_neg_entry = tkinter.Entry(values, textvariable=a_neg_str, state="disabled",
                                                    font=("large_font", 15, "bold"))
                        a_neg_entry.place(x=100, y=50, width=40)
                        b_pos_entry = tkinter.Entry(values, textvariable=b_pos_str, state="disabled",
                                                    font=("large_font", 15, "bold"))
                        b_pos_entry.place(x=100, y=85, width=40)
                        b_neg_entry = tkinter.Entry(values, textvariable=b_neg_str, state="disabled",
                                                    font=("large_font", 15, "bold"))
                        b_neg_entry.place(x=100, y=120, width=40)
                        ab_pos_entry = tkinter.Entry(values, textvariable=ab_pos_str, state="disabled",
                                                     font=("large_font", 15, "bold"))
                        ab_pos_entry.place(x=100, y=155, width=40)
                        ab_neg_entry = tkinter.Entry(values, textvariable=ab_neg_str, state="disabled",
                                                     font=("large_font", 15, "bold"))
                        ab_neg_entry.place(x=100, y=190, width=40)
                        o_pos_entry = tkinter.Entry(values, textvariable=o_pos_str, state="disabled",
                                                    font=("large_font", 15, "bold"))
                        o_pos_entry.place(x=100, y=225, width=40)
                        o_neg_entry = tkinter.Entry(values, textvariable=o_neg_str, state="disabled",
                                                    font=("large_font", 15, "bold"))
                        o_neg_entry.place(x=100, y=260, width=40)

                        name_entry.delete(0, 'end')
                        mail_entry.delete(0, 'end')
                        phone_entry.delete(0, 'end')
                        requirement_entry.delete(0, 'end')
                        blood_entry.delete(0, 'end')
                    else:
                        messagebox.showerror("Error", "Requirement should be between 0 and 6", parent=login_window)
                else:
                    messagebox.showerror("Error", "Invalid Contact!!", parent=login_window)

            else:
                messagebox.showerror("Error", "Invalid Email!!", parent=login_window)

        else:
            messagebox.showerror("Error", "Your name should match with username", parent=login_window)

    # when login button is pressed on login page
    login_window = Toplevel()
    login_window.title("Login")
    login_window.geometry("1920x1080+-5+-1")
    login_window.configure(background="grey92")
    # for text label Welcome BAck on the login page
    labeled1 = tkinter.LabelFrame(login_window, bd=10, relief="groove", fg="gold", bg="dark blue")
    labeled1.place(x=0, y=0, relwidth=1, height=120)
    text1_label = tkinter.Label(labeled1, text="\t\t\t\t                    Welcome", bg="dark blue", fg="gold",
                                font=("times new roman", 30, "bold"))
    text1_label.grid(row=0, column=0, padx=20, pady=20)
    # for requesting half
    request_label = tkinter.LabelFrame(login_window, bd=10, relief="groove", fg="gold", bg="dark blue")
    request_label.place(x=0, y=120, relwidth=0.5, height=100)
    request_label_text = tkinter.Label(request_label, text="\t\tRequest Blood", bg="dark blue", fg="gold",
                                       font=("times new roman", 30, "bold"))
    request_label_text.grid(row=0, column=0, padx=20, pady=20)
    # for data in requesting half
    info_box = tkinter.Label(login_window, bd=10, relief="groove", bg="maroon")
    info_box.place(x=0, y=220, relwidth=0.5, height=860)
    name = tkinter.Label(info_box, text="Name", bg="maroon", fg="white", font=("times new roman", 22, "italic"))
    name.place(x=10, y=10)
    email = tkinter.Label(info_box, text="Email", bg="maroon", fg="white", font=("times new roman", 22, "italic"))
    email.place(x=10, y=70)
    phone = tkinter.Label(info_box, text="Contact", bg="maroon", fg="white", font=("times new roman", 22, "italic"))
    phone.place(x=10, y=130)
    blood = tkinter.Label(info_box, text="Blood Type", bg="maroon", fg="white", font=("times new roman", 22, "italic"))
    blood.place(x=10, y=190)
    requirement = tkinter.Label(info_box, text="Requirement\t\t1 unit = 350ml", bg="maroon", fg="white",
                                font=("times new roman", 22, "italic"))
    requirement.place(x=6, y=250)
    name_entry = tkinter.Entry(info_box, relief="sunken", font=("large_font", 15, "normal"))
    name_entry.place(x=200, y=15)
    mail_entry = tkinter.Entry(info_box, relief="sunken", font=("large_font", 15, "normal"))
    mail_entry.place(x=200, y=75)
    phone_entry = tkinter.Entry(info_box, relief="sunken", font=("large_font", 15, "normal"))
    phone_entry.place(x=200, y=135)
    blood_entry = ttk.Combobox(info_box, font=("large_font", 15, "normal"), width=10)
    blood_entry['values'] = ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')
    blood_entry.place(x=200, y=195)
    requirement_entry = Spinbox(info_box, from_=1, to=5, font=("large_font", 15, "normal"), width=10)
    requirement_entry.place(x=200, y=255)

    # button frame
    button_frame1 = Frame(info_box, bd=5, relief="ridge", bg="maroon")
    button_frame1.place(x=80, y=300, width=680, height=100)
    # buttons in button frame

    add_entry = tkinter.Button(button_frame1, text="Add Request", bg="dark blue", fg="white", relief="raised",
                               font=("large_font", 15, "bold"), command=on_add)
    add_entry.place(x=40, y=22)
    delete_entry = tkinter.Button(button_frame1, text="Delete Request", bg="dark blue", fg="white", relief="raised",
                                  font=("large_font", 15, "bold"), command=on_del)
    delete_entry.place(x=250, y=22)
    clear_entry = tkinter.Button(button_frame1, text="Clear Request", bg="dark blue", fg="white", relief="raised",
                                 font=("large_font", 15, "bold"), command=on_clear)
    clear_entry.place(x=480, y=22)

    # to show the quantity available of blood
    values = tkinter.LabelFrame(info_box, text="Available blood in Bank", bg="maroon", fg="gold",
                                font=("large_font", 15, "bold"), relief="groove", bd=10)
    values.place(x=300, y=450, width=300, height=350)
    a_positive = tkinter.Label(values, text="  A +", bg="maroon", fg="gold", font="large_font")
    a_positive.place(x=10, y=10)
    a_negative = tkinter.Label(values, text="  A -", bg="maroon", fg="gold", font="large_font")
    a_negative.place(x=10, y=45)
    b_positive = tkinter.Label(values, text="  B +", bg="maroon", fg="gold", font="large_font")
    b_positive.place(x=10, y=80)
    b_negative = tkinter.Label(values, text="  B -", bg="maroon", fg="gold", font="large_font")
    b_negative.place(x=10, y=115)
    ab_positive = tkinter.Label(values, text="AB +", bg="maroon", fg="gold", font="large_font")
    ab_positive.place(x=10, y=150)
    ab_negative = tkinter.Label(values, text="AB -", bg="maroon", fg="gold", font="large_font")
    ab_negative.place(x=10, y=185)
    o_positive = tkinter.Label(values, text="  O +", bg="maroon", fg="gold", font="large_font")
    o_positive.place(x=10, y=220)
    o_negative = tkinter.Label(values, text="  O -", bg="maroon", fg="gold", font="large_font")
    o_negative.place(x=10, y=255)

    a_positive_entry = tkinter.Entry(values, textvariable=a_pos_str, state="disabled", font=("large_font", 15, "bold"))
    a_positive_entry.place(x=100, y=15, width=40)
    a_negative_entry = tkinter.Entry(values, textvariable=a_neg_str, state="disabled", font=("large_font", 15, "bold"))
    a_negative_entry.place(x=100, y=50, width=40)
    b_positive_entry = tkinter.Entry(values, textvariable=b_pos_str, state="disabled", font=("large_font", 15, "bold"))
    b_positive_entry.place(x=100, y=85, width=40)
    b_negative_entry = tkinter.Entry(values, textvariable=b_neg_str, state="disabled", font=("large_font", 15, "bold"))
    b_negative_entry.place(x=100, y=120, width=40)
    ab_positive_entry = tkinter.Entry(values, textvariable=ab_pos_str, state="disabled",
                                      font=("large_font", 15, "bold"))
    ab_positive_entry.place(x=100, y=155, width=40)
    ab_negative_entry = tkinter.Entry(values, textvariable=ab_neg_str, state="disabled",
                                      font=("large_font", 15, "bold"))
    ab_negative_entry.place(x=100, y=190, width=40)
    o_positive_entry = tkinter.Entry(values, textvariable=o_pos_str, state="disabled", font=("large_font", 15, "bold"))
    o_positive_entry.place(x=100, y=225, width=40)
    o_negative_entry = tkinter.Entry(values, textvariable=o_neg_str, state="disabled", font=("large_font", 15, "bold"))
    o_negative_entry.place(x=100, y=260, width=40)

    # for donating half
    donate_label = tkinter.LabelFrame(login_window, bd=10, relief="groove", bg="dark blue")
    donate_label.place(x=(1920/2), y=120, relwidth=0.5, height=100)
    donate_label_text = tkinter.Label(donate_label, text="\t\tDonate Blood", bg="dark blue", fg="gold",
                                      font=("times new roman", 30, "bold"))
    donate_label_text.place(x=80, y=20)

    # for making a label frame inside Donation half
    info_box2 = tkinter.Label(login_window, bd=10, relief="groove", bg="maroon")
    info_box2.place(x=(1920/2), y=220, relwidth=0.5, height=860)


a_pos_str = StringVar()
a_pos_str.set(blood_val)
a_neg_str = StringVar()
a_neg_str.set(blood_val)
b_pos_str = StringVar()
b_pos_str.set(blood_val)
b_neg_str = StringVar()
b_neg_str.set(blood_val)
ab_pos_str = StringVar()
ab_pos_str.set(blood_val)
ab_neg_str = StringVar()
ab_neg_str.set(blood_val)
o_pos_str = StringVar()
o_pos_str.set(blood_val)
o_neg_str = StringVar()
o_neg_str.set(blood_val)

# to make top title frame
labeled = tkinter.LabelFrame(bd=10, relief="groove", fg="gold", bg="red2")
labeled.place(x=0, y=0, relwidth=1, height=120)
text_label = tkinter.Label(labeled, text="\t\t\t\t     Online Blood Bank Management", bg="red2", fg="gold",
                           font=("times new roman", 30, "bold"))

text_label.grid(row=0, column=0, padx=20, pady=20)


# to make login frame for user and hospital
login_frame_user = tkinter.LabelFrame(bd=10, relief="groove", text="Login as User",
                                      font=("times new roman", 20, "bold"), fg="gold", bg="dark blue")
login_frame_user.place(x=400, y=300, width=470, height=350)

login_frame_hospital = tkinter.LabelFrame(bd=10, relief="groove", text="Login as Hospital Staff",
                                          font=("times new roman", 20, "bold"), fg="gold", bg="dark blue")
login_frame_hospital.place(x=1090, y=300, width=470, height=350)


# to make username and password entries for user and hospital
var = StringVar()
var.set(" ")
username_user = tkinter.Label(login_frame_user, image=photos[0], bd=5)
username_user.grid(row=0, column=0, pady=30, padx=20)
username_entry_user = tkinter.Entry(login_frame_user, textvariable=str, relief="groove", font=("large_font",
                                                                                               15, "normal"))
username_entry_user.place(x=130, y=50)
username_password_user = tkinter.Label(login_frame_user, image=photos[1], bd=5)
username_password_user.grid(row=3, column=0)
username_entry_password_user = tkinter.Entry(login_frame_user, relief="groove", font=("large_font", 15,
                                                                                      "normal"), show="*")\
    .grid(row=3, column=1, padx=30)
print(username_entry_user.get())

username_hospital = tkinter.Label(login_frame_hospital, image=photos[0], bd=5)
username_hospital.grid(row=0, column=0, pady=30, padx=20)
username_entry_hospital = tkinter.Entry(login_frame_hospital, relief="groove", font="large_font").grid(row=0, column=1,
                                                                                                       padx=30)
username_password_hospital = tkinter.Label(login_frame_hospital, image=photos[1], bd=5)
username_password_hospital.grid(row=3, column=0)
username_entry_password_hospital = tkinter.Entry(login_frame_hospital, relief="groove", font="large_font", show="*").\
    grid(row=3, column=1)


# login buttons
user_login = tkinter.Button(login_frame_user, text="Login", bg="Green", fg="white", font=("caliber", 15, "italic bold"),
                            padx=40, relief="raised", command=login)
user_login.grid(row=4, column=1, pady=10)

hospital_login = tkinter.Button(login_frame_hospital, text="Login", bg="Green", fg="white",
                                font=("caliber", 15, "italic bold"), padx=40, relief="raised")
hospital_login.grid(row=4, column=1, pady=10)
user_signup = tkinter.Button(login_frame_user, text="Sign Up!!", bg="red2", fg="white",
                             font=("caliber", 15, "italic bold"), padx=40, relief="raised", command=register)
user_signup.grid(row=5, column=1, pady=10)
mainWindow.mainloop()
