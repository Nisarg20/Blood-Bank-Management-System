import tkinter
import threading
import imageio
from tkinter import ttk
from tkinter import messagebox, scrolledtext
from tkinter import *
from PIL import ImageTk, Image
import tkcalendar
import sqlite3
import datetime
import pygame
import time

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
          ImageTk.PhotoImage(Image.open("Logo2.jpg")), ImageTk.PhotoImage(Image.open("contact_us.png")),
          ImageTk.PhotoImage(Image.open("logout.jpg")), ImageTk.PhotoImage(Image.open("nav_con.png")),
          ImageTk.PhotoImage(Image.open("close.jpg")), ImageTk.PhotoImage(Image.open("faq.png")),
          ImageTk.PhotoImage(Image.open("users.png")), ImageTk.PhotoImage(Image.open("user data.png")),
          ImageTk.PhotoImage(Image.open("data.png")), ImageTk.PhotoImage(Image.open("users2.jpg")),
          ImageTk.PhotoImage(Image.open("Home.jpg")), ImageTk.PhotoImage(Image.open("user data2.jpg")),
          ImageTk.PhotoImage(Image.open("queries (1) (1).jpg")), ImageTk.PhotoImage(Image.open("Ask Queries.jpg")),
          ImageTk.PhotoImage(Image.open("Q&A background.png")), ImageTk.PhotoImage(Image.open("Send message.png")),
          ImageTk.PhotoImage(Image.open("Clear message.png")), ImageTk.PhotoImage(Image.open("Back.png")),
          ImageTk.PhotoImage(Image.open("contact_us2.jpg")), ImageTk.PhotoImage(Image.open("Sign_up_bg.jpg")),
          ImageTk.PhotoImage(Image.open("icons8-search-bar-100.png"))]

#  to place the logo on the login page
background = tkinter.Label(mainWindow, image=photos[2]).pack(fill="y")

# The following are functions for buttons (functions as in commands)
# register command when register button is pressed


def register():
    # to make another window that contains registration details
    register_window = Toplevel()
    register_window.title("Register")
    register_window.geometry("1920x1080+-5+-1")
    register_window.configure(background="red2")

    # to set the bg of the register page
    bg_label = tkinter.Label(register_window, image=photos[21])
    bg_label.place(x=-4, y=-33)

    register_frame = tkinter.LabelFrame(register_window, bd=10)
    register_frame.place(x=150, y=150, width=1620, height=750)
    label1 = tkinter.Label(register_frame, text="Sign Up", font=("caliber", 30, "bold"))
    label1.place(x=700, y=10)

    # to make labels and entries such as username, email ,DOB in this page
    username_label = tkinter.Label(register_frame, text="Username", font=("caliber", 25, "bold"))
    username_label.place(x=10, y=110)
    password_label = tkinter.Label(register_frame, text="Password", font=("caliber", 25, "bold"))
    password_label.place(x=600, y=110)
    email_label = tkinter.Label(register_frame, text="Email ", font=("caliber", 25, "bold"))
    email_label.place(x=1090, y=110)
    gender_label = tkinter.Label(register_frame, text="Gender", font=("caliber", 25, "bold"))
    gender_label.place(x=10, y=250)
    contact_label = tkinter.Label(register_frame, text="Contact", font=("caliber", 25, "bold"))
    contact_label.place(x=500, y=250)
    dob_label = tkinter.Label(register_frame, text="D.O.B", font=("caliber", 25, "bold"))
    dob_label.place(x=1000, y=250)
    address_label = tkinter.Label(register_frame, text="Address", font=("caliber", 25, "bold"))
    address_label.place(x=10, y=390)

    username_entry = tkinter.Entry(register_frame, font=("caliber", 16, "normal"), relief="groove")
    username_entry.place(x=230, y=120, width=300)
    password_entry = tkinter.Entry(register_frame, font=("caliber", 16, "normal"), relief="groove")
    password_entry.place(x=820, y=120)
    email_entry = tkinter.Entry(register_frame, font=("caliber", 16, "normal"), relief="groove")
    email_entry.place(x=1250, y=120, width=250)
    contact_entry = tkinter.Entry(register_frame, font=("caliber", 16, "normal"))
    contact_entry.place(x=700, y=260)
    gender_entry = ttk.Combobox(register_frame, width=20, state="readonly", font=("caliber", 16, "normal"))
    gender_entry['values'] = ("Male", "Female", "Other")
    gender_entry.place(x=180, y=260)
    dob_entry = tkcalendar.DateEntry(register_frame, font=("large_font", 16, "italic"), date_pattern='dd/mm/yyyy')
    dob_entry.place(x=1200, y=260)
    address_entry = tkinter.Text(register_frame, font=("caliber", 16, "normal"))
    address_entry.place(x=230, y=400, width=800, height=200)
    date2 = dob_entry.get()
    day2 = int(date2[:2])
    month2 = int(date2[3:5])
    year2 = int(date2[6:])

    # when sigh_up is pressed after registration details are filled
    def on_signup():
        date = dob_entry.get()
        day = int(date[:2])
        month = int(date[3:5])
        year = int(date[6:])
        if year2 - year == 18:
            if month2 - month >= 0:
                if day2 - day >= 0:
                    age = 18
                else:
                    age = year2 - year - 1
            else:
                age = year2 - year - 1
        else:
            age = year2 - year

        if len(str(username_entry.get())) >= 10:
            if len(password_entry.get()) >= 6:
                if email_entry.get()[-4:] == ".com":
                    if len(contact_entry.get()) == 10:
                        if age >= 18:
                            if len(address_entry.get(1.0, 'end')) >= 20:
                                messagebox.showinfo("Success", "Hurray Sign-In Successful", parent=register_window)
                                current_date_time = datetime.datetime.now()
                                date_month_year = "{0}-{1}-{2}".format(current_date_time.day, current_date_time.month,
                                                                       current_date_time.year)
                                time2 = "{0}:{1}:{2}".format(current_date_time.hour, current_date_time.minute,
                                                             current_date_time.second)
                                db = sqlite3.connect("sign_up.sqlite")
                                db.execute("CREATE TABLE IF NOT EXISTS sign_up(name TEXT, email TEXT, gender TEXT,"
                                           " password TEXT,"
                                           " phone TEXT, dob TEXT, age TEXT,"
                                           "  Address TEXT, date TEXT, time TEXT)")
                                db.execute("INSERT INTO sign_up(name, email, gender, password, phone, DOB, age, "
                                           " Address, date, time) "
                                           "                                    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                           (username_entry.get(), email_entry.get(), gender_entry.get(),
                                            password_entry.get(), contact_entry.get(),
                                            dob_entry.get(), age,  address_entry.get(1.0, 'end'), date_month_year,
                                            time2))
                                cursor = db.cursor()
                                cursor.execute("SELECT * FROM sign_up")
                                db.commit()
                                cursor.close()
                                db.close()

                                username_entry.delete(0, 'end')
                                password_entry.delete(0, 'end')
                                email_entry.delete(0, 'end')
                                contact_entry.delete(0, 'end')
                                address_entry.delete(1.0, 'end')

                            else:
                                messagebox.showerror("Error", "Please Enter your full address!!",
                                                     parent=register_window)
                        else:
                            messagebox.showerror("Error", "Please Wait for {0} year(s) more :)".format(18 - age),
                                                 parent=register_window)
                    else:
                        messagebox.showerror("Error", "Contact not valid!!", parent=register_window)
                else:
                    messagebox.showerror("Error", "Invalid Email Address!!", parent=register_window)
            else:
                messagebox.showerror("Error", "Password should be strong(equivalent to 6 or more spaces)!!",
                                     parent=register_window)
        else:
            messagebox.showerror("Error", "Please Enter your full name!!", parent=register_window)

    # button frame
    button_frame = Frame(register_frame, bd=5, relief="ridge", bg="grey")
    button_frame.place(x=500, y=610, width=600, height=110)

    # Sign up button
    signup_button = tkinter.Button(button_frame, text="    Sign Up   ", font=("caliber", 18, "italic"), relief="raised",
                                   command=on_signup, bg="green", fg="white",)
    signup_button.place(x=20, y=23)

    back_button = tkinter.Button(button_frame, text="    Back   ", font=("caliber", 18, "italic"), relief="raised",
                                 command=register_window.destroy, bg="maroon", fg="white",)
    back_button.place(x=230, y=23)

    # when quit is pressed
    def on_quit():
        register_window.destroy()
        mainWindow.destroy()

    clear_button = tkinter.Button(button_frame, text="    Exit   ", bg="red2", fg="white",
                                  font=("caliber", 18, "italic"), relief="raised", command=on_quit)
    clear_button.place(x=430, y=23)

    register_window.mainloop()


def login():
    name_list = []
    name_last = username_entry_user.get()
    pass_last = username_entry_password_user.get()
    db_last = sqlite3.connect("sign_up.sqlite")
    cursor_last = db_last.cursor()
    cursor_last.execute("SELECT * FROM sign_up WHERE (name = ?)", [name_last])
    name_list.append(cursor_last.fetchall())

    for q in name_list:
        for w in q:
            if pass_last in w:
                # to clear entry in requesting half
                def on_clear():
                    name_entry.delete(0, 'end')
                    mail_entry.delete(0, 'end')
                    phone_entry.delete(0, 'end')
                    requirement_entry.delete(0, 'end')
                    blood_entry.delete(0, 'end')

                # to clear entry in donation half
                def on_clear2():
                    info_name_entry.delete(0, 'end')
                    info_email_entry.delete(0, 'end')
                    info_phone_entry.delete(0, 'end')
                    info_requirement_entry.delete(0, 'end')
                    info_b_entry.delete(0, 'end')
                    info_last_date_entry.delete(0, 'end')

                # to delete entry in donating half
                def on_del2():
                    def in_del2():
                        record2 = []
                        j = []
                        db = sqlite3.connect("donate.sqlite")
                        cursor = db.cursor()
                        cursor.execute("SELECT * FROM donate")
                        record2.append(cursor.fetchall())
                        name3 = username_entry_user.get()
                        cursor.execute("DELETE FROM donate WHERE (name = ?)", [name3])
                        for i in record2:
                            for k in i:
                                if k[0] == name3:
                                    messagebox.showinfo("Success", "Data Deleted Successfully", parent=delete_page2)
                                    j.append(k[0])
                                    destroy()
                                    if b_type2_entry.get() == "B+":
                                        b_pos_str.set(int(b_pos_str.get()) - int(delete_req2_entry.get()))
                                    elif b_type2_entry.get() == "B-":
                                        b_neg_str.set(int(b_neg_str.get()) - int(delete_req2_entry.get()))
                                    elif b_type2_entry.get() == "A+":
                                        a_pos_str.set(int(a_pos_str.get()) - int(delete_req2_entry.get()))
                                    elif b_type2_entry.get() == "A-":
                                        a_neg_str.set(int(a_neg_str.get()) - int(delete_req2_entry.get()))
                                    elif b_type2_entry.get() == "AB+":
                                        ab_pos_str.set(int(ab_pos_str.get()) - int(delete_req2_entry.get()))
                                    elif b_type2_entry.get() == "AB-":
                                        ab_neg_str.set(int(ab_neg_str.get()) - int(delete_req2_entry.get()))
                                    elif b_type2_entry.get() == "O+":
                                        o_pos_str.set(int(o_pos_str.get()) - int(delete_req2_entry.get()))
                                    elif b_type2_entry.get() == "O-":
                                        o_neg_str.set(int(o_neg_str.get()) - int(delete_req2_entry.get()))

                        for i in range(100):
                            if name3 not in j:
                                messagebox.showerror("Error", "No such name in the database", parent=delete_page2)
                                break

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

                        db.commit()
                        cursor.execute("SELECT * FROM donate")
                        print(cursor.fetchall())
                        cursor.close()
                        db.close()
                        delete_page2.destroy()

                    delete_page2 = Toplevel()
                    delete_page2.title("Delete Entry")
                    delete_page2.geometry("550x350")
                    delete_page2.configure(bg="maroon")
                    delete_page2.wm_attributes("-alpha", 0.95)

                    delete_req2 = tkinter.Label(delete_page2, font=("caliber", 15, "bold"), text="Unit", fg="gold",
                                                bg="dark blue")
                    delete_req2.place(x=30, y=50)
                    delete_req2_entry = Spinbox(delete_page2, from_=1, to=5, font=("large_font", 15, "normal"),
                                                width=10)
                    delete_req2_entry.place(x=180, y=50)
                    b_type2 = tkinter.Label(delete_page2, font=("caliber", 15, "bold"), text="Blood Type", fg="gold",
                                            bg="dark blue")
                    b_type2.place(x=30, y=110)
                    b_type2_entry = ttk.Combobox(delete_page2, font=("large_font", 15, "normal"), width=10)
                    b_type2_entry['values'] = ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')
                    b_type2_entry.place(x=180, y=113)
                    delete2_button = tkinter.Button(delete_page2, text="Delete Data", font="large_font", bg="dark blue",
                                                    fg="gold",
                                                    command=in_del2)
                    delete2_button.place(x=150, y=220)
                    note2 = tkinter.LabelFrame(delete_page2, font="large_font", bg="dark blue")
                    note2.place(x=10, y=280, width=530, height=60)
                    note2_label = tkinter.Label(note2, text="Note: The Unit value must be same as that in data!!",
                                                bg="dark blue",
                                                fg="gold", font=("caliber", 14, "normal"))
                    note2_label.place(x=10, y=12)

                # to delete entry in requesting half
                def on_del():
                    def in_del():
                        record = []
                        j = []
                        db = sqlite3.connect("request.sqlite")
                        cursor = db.cursor()
                        cursor.execute("SELECT * FROM request")
                        record.append(cursor.fetchall())
                        name2 = username_entry_user.get()
                        cursor.execute("DELETE FROM request WHERE (name = ?)", [name2])
                        for i in record:
                            for k in i:
                                if k[0] == name2:
                                    messagebox.showinfo("Success", "Data Deleted Successfully", parent=delete_page)
                                    j.append(k[0])
                                    destroy()
                                    if b_type_entry.get() == "B+":
                                        b_pos_str.set(int(b_pos_str.get()) + int(delete_req_entry.get()))
                                    elif b_type_entry.get() == "B-":
                                        b_neg_str.set(int(b_neg_str.get()) + int(delete_req_entry.get()))
                                    elif b_type_entry.get() == "A+":
                                        a_pos_str.set(int(a_pos_str.get()) + int(delete_req_entry.get()))
                                    elif b_type_entry.get() == "A-":
                                        a_neg_str.set(int(a_neg_str.get()) + int(delete_req_entry.get()))
                                    elif b_type_entry.get() == "AB+":
                                        ab_pos_str.set(int(ab_pos_str.get()) + int(delete_req_entry.get()))
                                    elif b_type_entry.get() == "AB-":
                                        ab_neg_str.set(int(ab_neg_str.get()) + int(delete_req_entry.get()))
                                    elif b_type_entry.get() == "O+":
                                        o_pos_str.set(int(o_pos_str.get()) + int(delete_req_entry.get()))
                                    elif b_type_entry.get() == "O-":
                                        o_neg_str.set(int(o_neg_str.get()) + int(delete_req_entry.get()))

                        for i in range(100):
                            if name2 not in j:
                                messagebox.showerror("Error", "No such name in the database", parent=delete_page)
                                break

                        db.commit()
                        cursor.execute("SELECT * FROM request")
                        print(cursor.fetchall())
                        cursor.close()
                        db.close()
                        delete_page.destroy()

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
                    delete_page.geometry("550x350")
                    delete_page.configure(bg="maroon")
                    delete_page.wm_attributes("-alpha", 0.95)

                    delete_req = tkinter.Label(delete_page, font=("caliber", 15, "bold"), text="Requirement", fg="gold",
                                               bg="dark blue")
                    delete_req.place(x=30, y=50)
                    delete_req_entry = Spinbox(delete_page, from_=1, to=5, font=("large_font", 15, "normal"), width=10)
                    delete_req_entry.place(x=180, y=50)
                    b_type = tkinter.Label(delete_page, font=("caliber", 15, "bold"), text="Blood Type", fg="gold",
                                           bg="dark blue")
                    b_type.place(x=30, y=110)
                    b_type_entry = ttk.Combobox(delete_page, font=("large_font", 15, "normal"), width=10)
                    b_type_entry['values'] = ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')
                    b_type_entry.place(x=180, y=113)
                    delete_button = tkinter.Button(delete_page, text="Delete Data", font="large_font", bg="dark blue",
                                                   fg="gold",
                                                   command=in_del)
                    delete_button.place(x=150, y=220)
                    note = tkinter.LabelFrame(delete_page, font="large_font", bg="dark blue")
                    note.place(x=10, y=280, width=530, height=60)
                    note_label = tkinter.Label(note, text="Note: The Req. value must be same as that in data!!",
                                               bg="dark blue",
                                               fg="gold", font=("caliber", 14, "normal"))
                    note_label.place(x=10, y=12)

                # to destroy entries in requesting half
                def destroy():
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

                # TO SET BLOOD ENTRY VALUES IN REQUESTING HALF
                def blood_val_sub():
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

                # to add entry in donating half
                def on_donate():
                    if username_entry_user.get() == info_name_entry.get():
                        if info_email_entry.get()[-4:] == ".com":
                            if len(info_phone_entry.get()) == 10:
                                if info_requirement_entry.get() in ('1', '2', '3', '4', '5'):
                                    if len(info_b_entry.get()) > 1:
                                        if info_last_date_entry.get() == "> 3" or\
                                                info_last_date_entry.get() == "First time donation":
                                            current_date_time = datetime.datetime.now()
                                            date_month_year = "{0}-{1}-{2}".format(current_date_time.day,
                                                                                   current_date_time.month,
                                                                                   current_date_time.year)
                                            time2 = "{0}:{1}:{2}".format(current_date_time.hour,
                                                                         current_date_time.minute,
                                                                         current_date_time.second)
                                            db = sqlite3.connect("donate.sqlite")
                                            db.execute("CREATE TABLE IF NOT EXISTS donate(name TEXT, email TEXT,"
                                                       " phone INTEGER,"
                                                       " requirement TEXT, blood TEXT, date TEXT, time TEXT)")
                                            db.execute("INSERT INTO donate(name, email, phone, requirement, blood,"
                                                       " date, time) "
                                                       " VALUES(?, ?, ?, ?, ?, ?, ?)",
                                                       (info_name_entry.get(), info_email_entry.get(),
                                                        info_phone_entry.get(),
                                                        info_requirement_entry.get(), info_b_entry.get(),
                                                        date_month_year,
                                                        time2))
                                            cursor = db.cursor()
                                            cursor.execute("SELECT * FROM donate")
                                            print(cursor.fetchall())
                                            db.commit()
                                            cursor.close()
                                            db.close()

                                            # to destroy and add a value to the blood val
                                            if info_b_entry.get() == "B+":
                                                b_pos_str.set(int(b_pos_str.get()) + int(info_requirement_entry.get()))
                                            elif info_b_entry.get() == "B-":
                                                b_neg_str.set(int(b_neg_str.get()) + int(info_requirement_entry.get()))
                                            elif info_b_entry.get() == "A+":
                                                a_pos_str.set(int(a_pos_str.get()) + int(info_requirement_entry.get()))
                                            elif info_b_entry.get() == "A-":
                                                a_neg_str.set(int(a_neg_str.get()) + int(info_requirement_entry.get()))
                                            elif info_b_entry.get() == "AB+":
                                                ab_pos_str.set(int(ab_pos_str.get()) +
                                                               int(info_requirement_entry.get()))
                                            elif info_b_entry.get() == "AB-":
                                                ab_neg_str.set(int(ab_neg_str.get()) +
                                                               int(info_requirement_entry.get()))
                                            elif info_b_entry.get() == "O+":
                                                o_pos_str.set(int(o_pos_str.get()) + int(info_requirement_entry.get()))
                                            elif info_b_entry.get() == "O-":
                                                o_neg_str.set(int(o_neg_str.get()) + int(info_requirement_entry.get()))

                                            a_pos_entry = tkinter.Entry(values, textvariable=a_pos_str,
                                                                        state="disabled",
                                                                        font=("large_font", 15, "bold"))
                                            a_pos_entry.place(x=100, y=15, width=40)
                                            a_neg_entry = tkinter.Entry(values, textvariable=a_neg_str,
                                                                        state="disabled",
                                                                        font=("large_font", 15, "bold"))
                                            a_neg_entry.place(x=100, y=50, width=40)
                                            b_pos_entry = tkinter.Entry(values, textvariable=b_pos_str,
                                                                        state="disabled",
                                                                        font=("large_font", 15, "bold"))
                                            b_pos_entry.place(x=100, y=85, width=40)
                                            b_neg_entry = tkinter.Entry(values, textvariable=b_neg_str,
                                                                        state="disabled",
                                                                        font=("large_font", 15, "bold"))
                                            b_neg_entry.place(x=100, y=120, width=40)
                                            ab_pos_entry = tkinter.Entry(values, textvariable=ab_pos_str,
                                                                         state="disabled",
                                                                         font=("large_font", 15, "bold"))
                                            ab_pos_entry.place(x=100, y=155, width=40)
                                            ab_neg_entry = tkinter.Entry(values, textvariable=ab_neg_str,
                                                                         state="disabled",
                                                                         font=("large_font", 15, "bold"))
                                            ab_neg_entry.place(x=100, y=190, width=40)
                                            o_pos_entry = tkinter.Entry(values, textvariable=o_pos_str,
                                                                        state="disabled",
                                                                        font=("large_font", 15, "bold"))
                                            o_pos_entry.place(x=100, y=225, width=40)
                                            o_neg_entry = tkinter.Entry(values, textvariable=o_neg_str,
                                                                        state="disabled",
                                                                        font=("large_font", 15, "bold"))
                                            o_neg_entry.place(x=100, y=260, width=40)
                                            on_clear2()

                                        else:
                                            messagebox.showerror("Error", "You must wait at least for 3 "
                                                                          "months before donating"
                                                                          " again", parent=login_window)
                                    else:
                                        messagebox.showerror("Error", "Invalid Blood Type", parent=login_window)
                                else:
                                    messagebox.showerror("Error", "Requirement should be between 0 and 6",
                                                         parent=login_window)
                            else:
                                messagebox.showerror("Error", "Invalid Contact!!", parent=login_window)

                        else:
                            messagebox.showerror("Error", "Invalid Email!!", parent=login_window)

                    else:
                        messagebox.showerror("Error", "Your name should match with username", parent=login_window)

                    # to clear entries once donate button is pressed
                    on_clear2()

                def on_add():
                    # on pressing add request button
                    if username_entry_user.get() == name_entry.get():
                        if mail_entry.get()[-4:] == ".com":
                            if len(phone_entry.get()) == 10:
                                if requirement_entry.get() in ('1', '2', '3', '4', '5'):
                                    if len(blood_entry.get()) > 1:
                                        current_date_time = datetime.datetime.now()
                                        date_month_year = "{0}-{1}-{2}".format(current_date_time.day,
                                                                               current_date_time.month,
                                                                               current_date_time.year)
                                        time2 = "{0}:{1}:{2}".format(current_date_time.hour, current_date_time.minute,
                                                                     current_date_time.second)
                                        db = sqlite3.connect("request.sqlite")
                                        db.execute("CREATE TABLE IF NOT EXISTS request(name TEXT, email TEXT,"
                                                   " phone INTEGER,"
                                                   " requirement TEXT, blood TEXT, date TEXT, time TEXT)")
                                        db.execute("INSERT INTO request(name, email, phone, requirement, blood,"
                                                   " date, time) "
                                                   "                                    VALUES(?, ?, ?, ?, ?, ?, ?)",
                                                   (name_entry.get(), mail_entry.get(), phone_entry.get(),
                                                    requirement_entry.get(),
                                                    blood_entry.get(), date_month_year, time2))
                                        cursor = db.cursor()
                                        cursor.execute("SELECT * FROM request")
                                        print(cursor.fetchall())
                                        db.commit()
                                        cursor.close()
                                        db.close()

                                        destroy()
                                        blood_val_sub()

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

                                        on_clear()

                                    else:
                                        messagebox.showerror("Error", "Invalid Blood Type", parent=login_window)
                                else:
                                    messagebox.showerror("Error", "Requirement should be between 0 and 6",
                                                         parent=login_window)
                            else:
                                messagebox.showerror("Error", "Invalid Contact!!", parent=login_window)

                        else:
                            messagebox.showerror("Error", "Invalid Email!!", parent=login_window)

                    else:
                        messagebox.showerror("Error", "Your name should match with username", parent=login_window)

                def my_donations():
                    # to display my donations
                    my_donation_page = Toplevel()
                    my_donation_page.title("My donation data")
                    my_donation_page.geometry("1420x440")
                    my_donation_page.resizable(False, False)
                    my_donation_page.config(bg="maroon")

                    # to print the data
                    collect = []
                    data = sqlite3.connect('donate.sqlite')
                    cursor1 = data.cursor()
                    name3 = username_entry_user.get()
                    cursor1.execute("SELECT * FROM donate WHERE (name = ?)", [name3])
                    rows = cursor1.fetchall()
                    print(rows)
                    collect.append(cursor1.fetchall())
                    style = ttk.Style()
                    style.configure("mystyle.Treeview", bd=5, font=("caliber", 15))
                    tree_view_my_donations = ttk.Treeview(my_donation_page, columns=(1, 2, 3, 4, 5, 6, 7),
                                                          show="headings",
                                                          height=20, style="mystyle.Treeview")
                    tree_view_my_donations.place(x=5, y=5)
                    tree_view_my_donations.heading(1, text="Name")
                    tree_view_my_donations.heading(2, text="Email")
                    tree_view_my_donations.heading(3, text="Contact")
                    tree_view_my_donations.heading(4, text="Units")
                    tree_view_my_donations.heading(5, text="Blood Type")
                    tree_view_my_donations.heading(6, text="Date  (DD-MM-YYYY)")
                    tree_view_my_donations.heading(7, text="Time  (Hr:Min:Sec)")
                    tree_view_my_donations.column(1, width=350)
                    tree_view_my_donations.column(2, width=350)
                    tree_view_my_donations.column(3, width=150)
                    tree_view_my_donations.column(4, width=100)
                    tree_view_my_donations.column(5, width=100)

                    for i in rows:
                        tree_view_my_donations.insert('', 'end', values=i)

                def my_requests():
                    # to display my requests
                    my_requests_page = Toplevel()
                    my_requests_page.title("My request data")
                    my_requests_page.geometry("1420x440")
                    my_requests_page.config(bg="maroon")
                    my_requests_page.resizable(False, False)

                    # to print the data
                    collect2 = []
                    data2 = sqlite3.connect('request.sqlite')
                    cursor2 = data2.cursor()
                    name5 = username_entry_user.get()
                    cursor2.execute("SELECT * FROM request WHERE (name = ?)", [name5])
                    rows = cursor2.fetchall()
                    print(rows)
                    collect2.append(cursor2.fetchall())
                    style = ttk.Style()
                    style.configure("mystyle.Treeview", bd=5, font=("caliber", 15))
                    tree_view_my_requests = ttk.Treeview(my_requests_page, columns=(1, 2, 3, 4, 5, 6, 7),
                                                         show="headings",
                                                         height=20, style="mystyle.Treeview")
                    tree_view_my_requests.place(x=5, y=5)
                    tree_view_my_requests.heading(1, text="Name")
                    tree_view_my_requests.heading(2, text="Email")
                    tree_view_my_requests.heading(3, text="Contact")
                    tree_view_my_requests.heading(4, text="Requirement")
                    tree_view_my_requests.heading(5, text="Blood Type")
                    tree_view_my_requests.heading(6, text="Date  (DD-MM-YYYY)")
                    tree_view_my_requests.heading(7, text="Time  (Hr:Min:Sec)")
                    tree_view_my_requests.column(1, width=350)
                    tree_view_my_requests.column(2, width=350)
                    tree_view_my_requests.column(3, width=150)
                    tree_view_my_requests.column(4, width=100)
                    tree_view_my_requests.column(5, width=100)

                    for i in rows:
                        tree_view_my_requests.insert('', 'end', values=i)

                def log_out():
                    ask = tkinter.messagebox.askquestion(" ", "Are you Sure you want to Log-Out?", parent=login_window,
                                                         icon="warning")
                    if ask == "yes":
                        login_window.destroy()
                        username_entry_user.delete(0, 'end')
                        username_entry_password_user.delete(0, 'end')

                # when login button is pressed on login page
                login_window = Toplevel()
                login_window.title("Login")
                login_window.geometry("1920x1080+-5+-1")
                login_window.configure(background="grey92")
                # for text label Welcome BAck on the login page
                labeled1 = tkinter.LabelFrame(login_window, bd=10, relief="groove", fg="gold", bg="dark blue")
                labeled1.place(x=0, y=0, relwidth=1, height=120)
                text1_label = tkinter.Label(labeled1, text="\t\t\t\t                    Welcome", bg="dark blue",
                                            fg="gold",
                                            font=("times new roman", 30, "bold"))
                text1_label.grid(row=0, column=0, padx=20, pady=20)
                # logout button
                logout_button = tkinter.Button(labeled1, image=photos[4], relief="raised", bd=5, command=log_out)
                logout_button.place(x=1700, y=25, height=50)
                # contact us at bottom of the page
                contact_us_frame = tkinter.LabelFrame(login_window, bd=10, relief="groove", bg="dark blue")
                contact_us_frame.place(x=0, y=660, height=390, width=1920)
                reach_us_label = tkinter.Label(contact_us_frame, bg="dark blue", fg="gold",
                                               text="Reach us at: -\n\nStreet: B-7 Deendayal Nagar, Navghar Road,"
                                                    " Mulund (east)\n"
                                                    "City: Mumbai     "
                                                    "State: Maharashtra     "
                                                    "Zip code: 400081", font=("Caliber", 20, "normal"))
                reach_us_label.place(x=10, y=215, height=120, width=820)
                photo_label = tkinter.Label(contact_us_frame, image=photos[3])
                photo_label.place(x=880, y=230, height=130, width=130)
                contact_us_label = tkinter.Label(contact_us_frame, bg="dark blue", fg="gold",
                                                 text="Contact us at:-\nLandline: 02225854754\nMobile:"
                                                      " +91-855-562-0355\n"
                                                      "Email Address:"
                                                 " onlinebloodbankmanagemenet@gmail.com", font=("Caliber", 20,
                                                                                                "normal"))
                contact_us_label.place(x=1030, y=215, height=120, width=780)
                # for requesting half
                request_label = tkinter.LabelFrame(login_window, bd=10, relief="groove", fg="gold", bg="dark blue")
                request_label.place(x=0, y=120, relwidth=0.5, height=100)
                request_label_text = tkinter.Label(request_label, text="\t\tRequest Blood", bg="dark blue", fg="gold",
                                                   font=("times new roman", 30, "bold"))
                request_label_text.grid(row=0, column=0, padx=20, pady=20)
                # for data in requesting half
                info_box = tkinter.Label(login_window, bd=10, relief="groove", bg="maroon")
                info_box.place(x=0, y=220, relwidth=0.5, height=660)
                name = tkinter.Label(info_box, text="Name", bg="maroon", fg="white", font=("times new roman", 22,
                                                                                           "italic"))
                name.place(x=10, y=10)
                email = tkinter.Label(info_box, text="Email", bg="maroon", fg="white", font=("times new roman", 22,
                                                                                             "italic"))
                email.place(x=10, y=70)
                phone = tkinter.Label(info_box, text="Contact", bg="maroon", fg="white", font=("times new roman", 22,
                                                                                               "italic"))
                phone.place(x=10, y=130)
                blood = tkinter.Label(info_box, text="Blood Type", bg="maroon", fg="white", font=("times new roman", 22,
                                                                                                  "italic"))
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
                button_frame1.place(x=10, y=460, width=880, height=100)
                # buttons in button frame

                add_entry = tkinter.Button(button_frame1, text="Add Request", bg="dark blue", fg="white",
                                           relief="raised",
                                           font=("large_font", 15, "bold"), command=on_add)
                add_entry.place(x=40, y=22)
                delete_entry = tkinter.Button(button_frame1, text="Delete Request", bg="dark blue", fg="white",
                                              relief="raised",
                                              font=("large_font", 15, "bold"), command=on_del)
                delete_entry.place(x=250, y=22)
                clear_entry = tkinter.Button(button_frame1, text="Clear Request", bg="dark blue", fg="white",
                                             relief="raised",
                                             font=("large_font", 15, "bold"), command=on_clear)
                clear_entry.place(x=480, y=22)
                requests = tkinter.Button(button_frame1, text="My Requests", bg="dark blue", fg="white",
                                          relief="raised",
                                          font=("large_font", 15, "bold"), command=my_requests)
                requests.place(x=690, y=22)

                # to show the quantity available of blood
                values = tkinter.LabelFrame(info_box, text="Available blood in Bank", bg="maroon", fg="gold",
                                            font=("large_font", 15, "bold"), relief="groove", bd=10)
                values.place(x=600, y=10, width=300, height=340)
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

                a_positive_entry = tkinter.Entry(values, textvariable=a_pos_str, state="disabled",
                                                 font=("large_font", 15, "bold"))
                a_positive_entry.place(x=100, y=15, width=40)
                a_negative_entry = tkinter.Entry(values, textvariable=a_neg_str, state="disabled",
                                                 font=("large_font", 15, "bold"))
                a_negative_entry.place(x=100, y=50, width=40)
                b_positive_entry = tkinter.Entry(values, textvariable=b_pos_str, state="disabled",
                                                 font=("large_font", 15, "bold"))
                b_positive_entry.place(x=100, y=85, width=40)
                b_negative_entry = tkinter.Entry(values, textvariable=b_neg_str, state="disabled",
                                                 font=("large_font", 15, "bold"))
                b_negative_entry.place(x=100, y=120, width=40)
                ab_positive_entry = tkinter.Entry(values, textvariable=ab_pos_str, state="disabled",
                                                  font=("large_font", 15, "bold"))
                ab_positive_entry.place(x=100, y=155, width=40)
                ab_negative_entry = tkinter.Entry(values, textvariable=ab_neg_str, state="disabled",
                                                  font=("large_font", 15, "bold"))
                ab_negative_entry.place(x=100, y=190, width=40)
                o_positive_entry = tkinter.Entry(values, textvariable=o_pos_str, state="disabled",
                                                 font=("large_font", 15, "bold"))
                o_positive_entry.place(x=100, y=225, width=40)
                o_negative_entry = tkinter.Entry(values, textvariable=o_neg_str, state="disabled",
                                                 font=("large_font", 15, "bold"))
                o_negative_entry.place(x=100, y=260, width=40)

                # for donating half
                donate_label = tkinter.LabelFrame(login_window, bd=10, relief="groove", bg="dark blue")
                donate_label.place(x=(1920/2), y=120, relwidth=0.5, height=100)
                donate_label_text = tkinter.Label(donate_label, text="\t\tDonate Blood", bg="dark blue", fg="gold",
                                                  font=("times new roman", 30, "bold"))
                donate_label_text.place(x=80, y=20)

                # for making a label frame inside Donation half
                info_box2 = tkinter.Label(login_window, bd=10, relief="groove", bg="maroon")
                info_box2.place(x=(1920/2), y=220, relwidth=0.5, height=660)

                info_name = tkinter.Label(info_box2, text="Name", bg="maroon", fg="white",
                                          font=("times new roman", 22, "italic"))
                info_name.place(x=10, y=10)
                info_email = tkinter.Label(info_box2, text="Email", bg="maroon", fg="white",
                                           font=("times new roman", 22, "italic"))
                info_email.place(x=10, y=70)
                info_phone = tkinter.Label(info_box2, text="Contact", bg="maroon", fg="white",
                                           font=("times new roman", 22, "italic"))
                info_phone.place(x=10, y=130)
                info_b = tkinter.Label(info_box2, text="Blood Type", bg="maroon", fg="white",
                                       font=("times new roman", 22, "italic"))
                info_b.place(x=10, y=190)
                info_requirement = tkinter.Label(info_box2, text="Unit\t\t\t1 unit = 350ml", bg="maroon", fg="white",
                                                 font=("times new roman", 22, "italic"))
                info_requirement.place(x=10, y=250)
                info_last_date = tkinter.Label(info_box2, text="Last Donation\t\t (how many months since last "
                                                               "donation)",
                                               bg="maroon", fg="white", font=("times new roman", 22, "italic"))
                info_last_date.place(x=10, y=310)
                info_name_entry = tkinter.Entry(info_box2, relief="sunken", font=("large_font", 15, "normal"))
                info_name_entry.place(x=200, y=15)
                info_email_entry = tkinter.Entry(info_box2, relief="sunken", font=("large_font", 15, "normal"))
                info_email_entry.place(x=200, y=75)
                info_phone_entry = tkinter.Entry(info_box2, relief="sunken", font=("large_font", 15, "normal"))
                info_phone_entry.place(x=200, y=135)
                info_b_entry = ttk.Combobox(info_box2, font=("large_font", 15, "normal"), width=10)
                info_b_entry['values'] = ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')
                info_b_entry.place(x=200, y=195)
                info_requirement_entry = Spinbox(info_box2, from_=1, to=5, font=("large_font", 15, "normal"), width=10)
                info_requirement_entry.place(x=200, y=255)
                info_last_date_entry = ttk.Combobox(info_box2, font=("large_font", 15, "normal"), width=10)
                info_last_date_entry['values'] = ('< 1', '> 3', 'First time donation')
                info_last_date_entry.place(x=200, y=315)

                # button frame
                button_frame2 = Frame(info_box2, bd=5, relief="ridge", bg="maroon")
                button_frame2.place(x=20, y=460, width=870, height=100)
                # buttons in button frame

                info_add_entry = tkinter.Button(button_frame2, text="Add Donation", bg="dark blue", fg="white",
                                                relief="raised",
                                                font=("large_font", 15, "bold"), command=on_donate)
                info_add_entry.place(x=40, y=22)
                info_delete_entry = tkinter.Button(button_frame2, text="Delete Donation", bg="dark blue", fg="white",
                                                   relief="raised", font=("large_font", 15, "bold"), command=on_del2)
                info_delete_entry.place(x=250, y=22)
                info_clear_entry = tkinter.Button(button_frame2, text="Clear Donation", bg="dark blue", fg="white",
                                                  relief="raised",
                                                  font=("large_font", 15, "bold"), command=on_clear2)
                info_clear_entry.place(x=480, y=22)
                info_my_donation = tkinter.Button(button_frame2, text="My Donations", bg="dark blue", fg="white",
                                                  relief="raised",
                                                  font=("large_font", 15, "bold"), command=my_donations)
                info_my_donation.place(x=690, y=22)
            break
        else:
            messagebox.showerror("Error", "Invalid Username or Password!!", parent=mainWindow)
            break

# **********************************************************************************************************************
# Below are the functions for admin page


def on_login_admin():
    if username_entry_hospital.get() == "Admin" and username_entry_password_hospital.get() == "thisisadmin":
        admin_login = Toplevel()
        admin_login.geometry("1920x1080+-5+-1")
        admin_login.config(bg="maroon")
        admin_login.title("Admin Login Page")

        # TO ADD welcome bar at the top
        labeled_ad = tkinter.LabelFrame(admin_login, bd=10, relief="groove", fg="gold", bg="dark blue")
        labeled_ad.place(x=0, y=0, relwidth=1, height=120)
        text_ad_label = tkinter.Label(labeled_ad, text="\t\t\t\t                    Welcome", bg="dark blue", fg="gold",
                                      font=("times new roman", 30, "bold"))
        text_ad_label.grid(row=0, column=0, padx=20, pady=20)

        # for setting nav bar:-
        def on_click_nav():
            def on_cross():
                nav_root.destroy()

            def on_registered_users():
                # to destroy admin page once registered users button in navigation bar is pressed
                admin_login.destroy()

                # to set up registered users page
                reg_users_page = Toplevel()
                reg_users_page.geometry("1920x1080+-5+-1")
                reg_users_page.config(bg="maroon")
                reg_users_page.title("Admin Login Page")

                # TO ADD welcome bar at the top
                labeled_ad1 = tkinter.LabelFrame(reg_users_page, bd=10, relief="groove", fg="gold", bg="dark blue")
                labeled_ad1.place(x=0, y=0, relwidth=1, height=120)
                text_ad_label1 = tkinter.Label(labeled_ad1, text="\t\t\t\t            Registered Users", bg="dark blue",
                                               fg="gold", font=("times new roman", 30, "bold"))
                text_ad_label1.grid(row=0, column=0, padx=20, pady=20)

                def on_click_nav2():
                    def on_cross2():
                        nav_root2.destroy()

                    def on_registered_users2():
                        reg_users_page.destroy()

                        on_registered_users()

                    def on_home2():
                        reg_users_page.destroy()

                        on_login_admin()

                    def on_queries2():
                        reg_users_page.destroy()

                        on_queries()

                    def on_user_activity2():
                        reg_users_page.destroy()

                        on_user_activity()

                    # Setting Navbar frame:
                    nav_root2 = tkinter.Frame(reg_users_page, bg="grey", height=1000, width=700, bd=20)
                    nav_root2.place(x=30, y=30)

                    # Close nav bar photo
                    close_nav2 = tkinter.Button(nav_root2, image=photos[6], relief="raised", bd=5, command=on_cross2)
                    close_nav2.place(x=600, y=25, width=40, height=40)

                    # setting the frame
                    nav_root_frame2 = tkinter.Frame(nav_root2, bd=10, bg="black")
                    nav_root_frame2.place(x=20, y=80, height=800, width=620)

                    # setting contents in the navigation bar
                    home_image2 = tkinter.Label(nav_root2, image=photos[12])
                    home_image2.place(x=50, y=130)
                    home2 = tkinter.Button(nav_root2, relief="raised", font=("caliber", 17, "normal"),
                                           text="Home", fg="gold", bg="brown4", bd=5, command=on_home2)
                    home2.place(x=200, y=140, width=210)
                    registered_users_img2 = tkinter.Label(nav_root2, image=photos[11])
                    registered_users_img2.place(x=50, y=330)
                    registered_users2 = tkinter.Button(nav_root2, relief="raised", font=("caliber", 17, "normal"),
                                                       text="Registered Users", fg="gold", bg="brown4", bd=5,
                                                       command=on_registered_users2)
                    registered_users2.place(x=200, y=330, width=210)
                    activity_history_img2 = tkinter.Label(nav_root2, image=photos[13])
                    activity_history_img2.place(x=50, y=520)
                    activity_history2 = tkinter.Button(nav_root2, relief="raised", font=("caliber", 17, "normal"),
                                                       text="User Activity", fg="gold", bg="brown4", bd=5,
                                                       command=on_user_activity2)
                    activity_history2.place(x=200, y=520, width=210)
                    queries_user_img2 = tkinter.Label(nav_root2, image=photos[14])
                    queries_user_img2.place(x=50, y=710)
                    queries_user2 = tkinter.Button(nav_root2, relief="raised", font=("caliber", 17, "normal"),
                                                   text="User Queries", fg="gold", bg="brown4", bd=5,
                                                   command=on_queries2)
                    queries_user2.place(x=200, y=710, width=210)

                    vertical_border_a = tkinter.Label(nav_root_frame2)
                    vertical_border_a.place(x=130, y=0, width=5, height=800)
                    horizontal_border_a = tkinter.Label(nav_root_frame2)
                    horizontal_border_a.place(x=0, y=165, width=620, height=5)
                    horizontal_border_b = tkinter.Label(nav_root_frame2)
                    horizontal_border_b.place(x=0, y=365, width=620, height=5)
                    horizontal_border_c = tkinter.Label(nav_root_frame2)
                    horizontal_border_c.place(x=0, y=555, width=620, height=5)

                def on_se_arch():
                    name_get = se_arch.get()
                    if name_get != "":
                        tree_view.destroy()
                        data2 = sqlite3.connect('sign_up.sqlite')
                        cursor2 = data2.cursor()
                        cursor2.execute("SELECT * FROM sign_up")
                        cursor2.execute("SELECT * FROM sign_up WHERE (name =?)", [name_get])
                        rows2 = cursor2.fetchall()
                        style2 = ttk.Style()
                        style2.configure("mystyle.Treeview", bd=5, font=("caliber", 14), rowheight=40)
                        tree_view2 = ttk.Treeview(frame1, columns=1, show="headings", height=43,
                                                  style="mystyle.Treeview")
                        tree_view2.place(x=0, y=0)
                        tree_view2.heading(1, text="Name")
                        tree_view2.column(1, width=355)

                        for a in rows2:
                            tree_view2.insert('', 'end', values=a)

                        cursor2.close()
                        data2.close()

                        def get_row2(event):
                            item = tree_view2.item(tree_view2.focus())
                            t1.set((item['values'][1]))
                            t2.set((item['values'][2]))
                            t3.set((item['values'][3]))
                            t4.set((item['values'][4]))
                            t5.set((item['values'][5]))
                            t6.set((item['values'][6]))
                            t7.set((item['values'][7]))
                            t8.set((item['values'][8]))
                            t9.set((item['values'][9]))
                            address_label2_entry.delete(1.0, 'end')
                            address_label2_entry.insert(1.0, t7.get())

                        tree_view2.bind('<Double 1>', get_row2)
                    else:
                        reg_users_page.destroy()

                        on_registered_users()

                def get_row(event):
                    item = tree_view.item(tree_view.focus())
                    t1.set((item['values'][1]))
                    t2.set((item['values'][2]))
                    t3.set((item['values'][3]))
                    t4.set((item['values'][4]))
                    t5.set((item['values'][5]))
                    t6.set((item['values'][6]))
                    t7.set((item['values'][7]))
                    t8.set((item['values'][8]))
                    t9.set((item['values'][9]))
                    address_label2_entry.delete(1.0, 'end')
                    address_label2_entry.insert(1.0, t7.get())

                nav_icon2 = tkinter.Button(reg_users_page, image=photos[5], relief="raised", bd=5,
                                           command=on_click_nav2)
                nav_icon2.place(x=30, y=30)

                frame1 = tkinter.LabelFrame(reg_users_page, bd=10, font=("caliber", 18, "normal"),
                                            text="Registered Users")
                frame1.place(x=0, y=120, height=930, width=380)
                style = ttk.Style()
                style.configure("mystyle.Treeview", bd=5, font=("caliber", 14), rowheight=40)
                tree_view = ttk.Treeview(frame1, columns=1, show="headings", height=43,
                                         style="mystyle.Treeview")
                tree_view.place(x=0, y=0)
                tree_view.heading(1, text="Name")
                tree_view.column(1, width=355)

                frame2 = tkinter.Frame(reg_users_page, bd=10, bg="maroon")
                frame2.place(x=385, y=320, height=720, width=1520)

                data = sqlite3.connect('sign_up.sqlite')
                cursor1 = data.cursor()
                cursor1.execute("SELECT * FROM sign_up")
                rows = cursor1.fetchall()
                for i in rows:
                    tree_view.insert('', 'end', values=i)
                cursor1.close()
                data.close()

                # it is the event listener .... double click to get the values in the tree view
                tree_view.bind('<Double 1>', get_row)

                # to create t1, t2 i.e text variable that will display the message and subject
                t1 = StringVar()
                t2 = StringVar()
                t3 = StringVar()
                t4 = StringVar()
                t5 = StringVar()
                t6 = StringVar()
                t7 = StringVar()
                t8 = StringVar()
                t9 = StringVar()

                contact_label2 = tkinter.Label(frame2, fg="gold", bg="maroon", font=("caliber", 18, "normal"),
                                               text="Phone Number")
                contact_label2.place(x=10, y=10)
                contact_label2_entry = tkinter.Entry(frame2, font=("caliber", 16, "normal"), text=t4)
                contact_label2_entry.place(x=200, y=15, width=300)
                gender_label2 = tkinter.Label(frame2, fg="gold", bg="maroon", font=("caliber", 18, "normal"),
                                              text="Gender")
                gender_label2.place(x=550, y=10)
                gender_label2_entry = tkinter.Entry(frame2, font=("caliber", 16, "normal"), text=t2)
                gender_label2_entry.place(x=660, y=15)
                password_label2 = tkinter.Label(frame2, fg="gold", bg="maroon", font=("caliber", 18, "normal"),
                                                text="Password")
                password_label2.place(x=10, y=100)
                password_label2_entry = tkinter.Entry(frame2, font=("caliber", 16, "normal"), text=t3)
                password_label2_entry.place(x=200, y=105)
                email_label2 = tkinter.Label(frame2, fg="gold", bg="maroon", font=("caliber", 18, "normal"),
                                             text="E-Main")
                email_label2.place(x=550, y=100)
                email_label2_entry = tkinter.Entry(frame2, font=("caliber", 16, "normal"), text=t1)
                email_label2_entry.place(x=660, y=105)
                age_label2 = tkinter.Label(frame2, fg="gold", bg="maroon", font=("caliber", 18, "normal"), text="Age")
                age_label2.place(x=1000, y=10)
                age_label2_entry = tkinter.Entry(frame2, font=("caliber", 16, "normal"), text=t6)
                age_label2_entry.place(x=1100, y=15)
                dob_label2 = tkinter.Label(frame2, fg="gold", bg="maroon", font=("caliber", 18, "normal"),
                                           text="DOB")
                dob_label2.place(x=1000, y=100)
                dob_label2_entry = tkinter.Entry(frame2, font=("caliber", 16, "normal"), text=t5)
                dob_label2_entry.place(x=1100, y=105)
                time_label2 = tkinter.Label(frame2, fg="gold", bg="maroon", font=("caliber", 18, "normal"), text="Time")
                time_label2.place(x=10, y=200)
                time_label2_entry = tkinter.Entry(frame2, font=("caliber", 16, "normal"), text=t9)
                time_label2_entry.place(x=200, y=205)
                date_label2 = tkinter.Label(frame2, fg="gold", bg="maroon", font=("caliber", 18, "normal"), text="Date")
                date_label2.place(x=550, y=200)
                date_label2_entry = tkinter.Entry(frame2, font=("caliber", 16, "normal"), text=t8)
                date_label2_entry.place(x=660, y=205)
                address_label2 = tkinter.Label(frame2, fg="gold", bg="maroon", font=("caliber", 18, "normal"),
                                               text="Address")
                address_label2.place(x=10, y=300)
                address_label2_entry = tkinter.Text(frame2, font=("caliber", 16, "normal"))
                address_label2_entry.place(x=190, y=305, height=300)

                se_arch = tkinter.Entry(reg_users_page, font=("caliber", 16, "normal"))
                se_arch.place(x=950, y=200, width=330)
                se_arch_img = tkinter.Button(reg_users_page, image=photos[22], relief="raised", bd=5,
                                             command=on_se_arch)
                se_arch_img.place(x=1330, y=193, height=38)

            def on_queries():
                # to destroy admin page once registered users button in navigation bar is pressed
                admin_login.destroy()

                # to set up registered users page
                query_page = Toplevel()
                query_page.geometry("1920x1080+-5+-1")
                query_page.config(bg="maroon")
                query_page.title("Admin Login Page")

                # TO ADD welcome bar at the top
                labeled_ad2 = tkinter.LabelFrame(query_page, bd=10, relief="groove", fg="gold", bg="dark blue")
                labeled_ad2.place(x=0, y=0, relwidth=1, height=120)
                text_ad_label2 = tkinter.Label(labeled_ad2, text="\t\t\t\t             User Queries", bg="dark blue",
                                               fg="gold", font=("times new roman", 30, "bold"))
                text_ad_label2.grid(row=0, column=0, padx=20, pady=20)

                def on_click_nav3():
                    def on_cross3():
                        nav_root3.destroy()

                    def on_registered_users3():
                        query_page.destroy()

                        on_registered_users()

                    def on_home3():
                        query_page.destroy()

                        on_login_admin()

                    def on_queries3():
                        query_page.destroy()

                        on_queries()

                    def on_user_activity3():
                        query_page.destroy()

                        on_user_activity()

                    # Setting Navbar frame:
                    nav_root3 = tkinter.Frame(query_page, bg="grey", height=1000, width=700, bd=20)
                    nav_root3.place(x=30, y=30)

                    # Close nav bar photo
                    close_nav3 = tkinter.Button(nav_root3, image=photos[6], relief="raised", bd=5, command=on_cross3)
                    close_nav3.place(x=600, y=25, width=40, height=40)

                    # setting the frame
                    nav_root_frame3 = tkinter.Frame(nav_root3, bd=10, bg="black")
                    nav_root_frame3.place(x=20, y=80, height=800, width=620)

                    # setting contents in the navigation bar
                    home_image2 = tkinter.Label(nav_root3, image=photos[12])
                    home_image2.place(x=50, y=130)
                    home2 = tkinter.Button(nav_root3, relief="raised", font=("caliber", 17, "normal"),
                                           text="Home", fg="gold", bg="brown4", bd=5, command=on_home3)
                    home2.place(x=200, y=140, width=210)
                    registered_users_img2 = tkinter.Label(nav_root3, image=photos[11])
                    registered_users_img2.place(x=50, y=330)
                    registered_users2 = tkinter.Button(nav_root3, relief="raised", font=("caliber", 17, "normal"),
                                                       text="Registered Users", fg="gold", bg="brown4", bd=5,
                                                       command=on_registered_users3)
                    registered_users2.place(x=200, y=330, width=210)
                    activity_history_img2 = tkinter.Label(nav_root3, image=photos[13])
                    activity_history_img2.place(x=50, y=520)
                    activity_history2 = tkinter.Button(nav_root3, relief="raised", font=("caliber", 17, "normal"),
                                                       text="User Activity", fg="gold", bg="brown4", bd=5,
                                                       command=on_user_activity3)
                    activity_history2.place(x=200, y=520, width=210)
                    queries_user_img2 = tkinter.Label(nav_root3, image=photos[14])
                    queries_user_img2.place(x=50, y=710)
                    queries_user2 = tkinter.Button(nav_root3, relief="raised", font=("caliber", 17, "normal"),
                                                   text="User Queries", fg="gold", bg="brown4", bd=5,
                                                   command=on_queries3)
                    queries_user2.place(x=200, y=710, width=210)

                    vertical_border_a1 = tkinter.Label(nav_root_frame3)
                    vertical_border_a1.place(x=130, y=0, width=5, height=800)
                    horizontal_border_a1 = tkinter.Label(nav_root_frame3)
                    horizontal_border_a1.place(x=0, y=165, width=620, height=5)
                    horizontal_border_b1 = tkinter.Label(nav_root_frame3)
                    horizontal_border_b1.place(x=0, y=365, width=620, height=5)
                    horizontal_border_c1 = tkinter.Label(nav_root_frame3)
                    horizontal_border_c1.place(x=0, y=555, width=620, height=5)

                nav_icon3 = tkinter.Button(query_page, image=photos[5], relief="raised", bd=5, command=on_click_nav3)
                nav_icon3.place(x=30, y=30)

                # to open database
                db3 = sqlite3.connect('queries.sqlite')
                cursor = db3.cursor()

                # to update the tree table once the query is dealt with(deleted)
                def update():
                    query_page.destroy()

                    on_queries()

                # when double clicked the data in the tree view it will display the subject and the query
                def get_row(event):
                    item = tree_view.item(tree_view.focus())
                    t1.set((item['values'][3]))
                    t2.set((item['values'][4]))
                    message_label_entry.delete(1.0, 'end')
                    message_label_entry.insert(1.0, t2.get())

                # to close the query once dealt with
                def on_close():
                    user_id = t1.get()
                    print(user_id)
                    if user_id == "":
                        messagebox.showerror("Error", "Please Double Click the required field if you wish"
                                                      " to delete it!",
                                             parent=query_page)

                    else:
                        ask = messagebox.askquestion("Conform Delete?", "Are You sure you want to delete this data?",
                                                     parent=query_page)
                        if ask == "yes":
                            cursor.execute("DELETE FROM queries WHERE (subject = ?) ", [user_id])

                            db3.commit()
                            update()

                # to design the page
                data_frame1 = tkinter.LabelFrame(query_page, text="User Details", font="large_font", fg="gold", bd=10,
                                                 bg="maroon")
                data_frame1.place(x=0, y=120, width=900, height=925)
                data_frame2 = tkinter.LabelFrame(query_page, text="User Queries", font="large_font", fg="gold", bd=10,
                                                 bg="maroon")
                data_frame2.place(x=900, y=120, width=1010, height=925)

                # to change the font size of tree view
                style = ttk.Style()
                style.configure("mystyle.Treeview", bd=5, font=("caliber", 15), rowheight=40)
                # TO DESIGN THE TREE VIEW TABLE
                tree_view = ttk.Treeview(data_frame1, columns=(1, 2, 3), show="headings", height=21,
                                         style="mystyle.Treeview")
                tree_view.place(x=20, y=20)
                tree_view.heading(1, text="Name")
                tree_view.heading(2, text="Email")
                tree_view.heading(3, text="Phone")
                tree_view.column(1, width=345)
                tree_view.column(2, width=345)
                tree_view.column(3, width=150)

                # it is the event listener .... double click to get the values in the tree view
                tree_view.bind('<Double 1>', get_row)

                # to store data in the database
                db3 = sqlite3.connect('queries.sqlite')
                cursor = db3.cursor()
                cursor.execute("SELECT * FROM queries")
                rows = cursor.fetchall()

                # to create t1, t2 i.e text variable that will display the message and subject
                t1 = StringVar()
                t2 = StringVar()

                # to print values row wise in tree view table
                for i in rows:
                    tree_view.insert('', 'end', values=i)

                # to create labels subject and message and their respective entries
                subject_label = tkinter.Label(data_frame2, text="Subject", font=("caliber", 20, "bold"), bg="maroon",
                                              fg="gold")
                subject_label.place(x=20, y=20)
                subject_label_entry = tkinter.Entry(data_frame2, font=("caliber", 16, "normal"), text=t1,
                                                    state='readonly')
                subject_label_entry.place(x=150, y=25, width=800)

                message_label = tkinter.Label(data_frame2, text="Message", font=("caliber", 20, "bold"), bg="maroon",
                                              fg="gold")
                message_label.place(x=20, y=100)
                message_label_entry = tkinter.Text(data_frame2)
                message_label_entry.place(x=80, y=170, width=830, height=400)
                message_label_entry.configure(font="mystyle.Treeview")

                close_query = tkinter.Button(data_frame2, text="Close Query", fg="gold", bg="green", font="large_font",
                                             command=on_close)
                close_query.place(x=390, y=680)

            def on_user_activity():
                # to destroy admin page once registered users button in navigation bar is pressed
                admin_login.destroy()

                # to set up registered users page
                user_activity_page = Toplevel()
                user_activity_page.geometry("1920x1080+-5+-1")
                user_activity_page.config(bg="maroon")
                user_activity_page.title("Admin Login Page")

                # TO ADD welcome bar at the top
                labeled_ad3 = tkinter.LabelFrame(user_activity_page, bd=10, relief="groove", fg="gold", bg="dark blue")
                labeled_ad3.place(x=0, y=0, relwidth=1, height=120)
                text_ad_label3 = tkinter.Label(labeled_ad3, text="\t\t\t\t            User Activities", bg="dark blue",
                                               fg="gold", font=("times new roman", 30, "bold"))
                text_ad_label3.grid(row=0, column=0, padx=20, pady=20)

                nav_icon3 = tkinter.Button(user_activity_page, image=photos[5], relief="raised", bd=5)
                nav_icon3.place(x=30, y=30)

                def on_click_nav4():
                    def on_cross4():
                        nav_root4.destroy()

                    def on_registered_users4():
                        user_activity_page.destroy()

                        on_registered_users()

                    def on_home4():
                        user_activity_page.destroy()

                        on_login_admin()

                    def on_queries4():
                        user_activity_page.destroy()

                        on_queries()

                    def on_user_activity4():
                        user_activity_page.destroy()

                        on_user_activity()

                    # Setting Navbar frame:
                    nav_root4 = tkinter.Frame(user_activity_page, bg="grey", height=1000, width=700, bd=20)
                    nav_root4.place(x=30, y=30)

                    # Close nav bar photo
                    close_nav4 = tkinter.Button(nav_root4, image=photos[6], relief="raised", bd=5, command=on_cross4)
                    close_nav4.place(x=600, y=25, width=40, height=40)

                    # setting the frame
                    nav_root_frame4 = tkinter.Frame(nav_root4, bd=10, bg="black")
                    nav_root_frame4.place(x=20, y=80, height=800, width=620)

                    # setting contents in the navigation bar
                    home_image3 = tkinter.Label(nav_root4, image=photos[12])
                    home_image3.place(x=50, y=130)
                    home3 = tkinter.Button(nav_root4, relief="raised", font=("caliber", 17, "normal"),
                                           text="Home", fg="gold", bg="brown4", bd=5, command=on_home4)
                    home3.place(x=200, y=140, width=210)
                    registered_users_img3 = tkinter.Label(nav_root4, image=photos[11])
                    registered_users_img3.place(x=50, y=330)
                    registered_users3 = tkinter.Button(nav_root4, relief="raised", font=("caliber", 17, "normal"),
                                                       text="Registered Users", fg="gold", bg="brown4", bd=5,
                                                       command=on_registered_users4)
                    registered_users3.place(x=200, y=330, width=210)
                    activity_history_img3 = tkinter.Label(nav_root4, image=photos[13])
                    activity_history_img3.place(x=50, y=520)
                    activity_history3 = tkinter.Button(nav_root4, relief="raised", font=("caliber", 17, "normal"),
                                                       text="User Activity", fg="gold", bg="brown4", bd=5,
                                                       command=on_user_activity4)
                    activity_history3.place(x=200, y=520, width=210)
                    queries_user_img3 = tkinter.Label(nav_root4, image=photos[14])
                    queries_user_img3.place(x=50, y=710)
                    queries_user3 = tkinter.Button(nav_root4, relief="raised", font=("caliber", 17, "normal"),
                                                   text="User Queries", fg="gold", bg="brown4", bd=5,
                                                   command=on_queries4)
                    queries_user3.place(x=200, y=710, width=210)

                    vertical_border_a2 = tkinter.Label(nav_root_frame4)
                    vertical_border_a2.place(x=130, y=0, width=5, height=800)
                    horizontal_border_a2 = tkinter.Label(nav_root_frame4)
                    horizontal_border_a2.place(x=0, y=165, width=620, height=5)
                    horizontal_border_b2 = tkinter.Label(nav_root_frame4)
                    horizontal_border_b2.place(x=0, y=365, width=620, height=5)
                    horizontal_border_c2 = tkinter.Label(nav_root_frame4)
                    horizontal_border_c2.place(x=0, y=555, width=620, height=5)

                def on_click_search():
                    name_get = name_entry.get()
                    if name_get != "":
                        tree_view.destroy()
                        tree_view2.destroy()
                        data2 = sqlite3.connect('request.sqlite')
                        cursor2 = data2.cursor()
                        cursor2.execute("SELECT * FROM request")
                        cursor2.execute("SELECT * FROM request WHERE (name =?)", [name_get])
                        rows2 = cursor2.fetchall()
                        style2 = ttk.Style()
                        style2.configure("mystyle.Treeview", bd=5, font=("caliber", 16), rowheight=40)
                        tree_view3 = ttk.Treeview(frame2, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height=10,
                                                  style="mystyle.Treeview")
                        tree_view3.place(x=0, y=0)
                        tree_view3.heading(1, text="Name")
                        tree_view3.heading(2, text="Email")
                        tree_view3.heading(3, text="Phone")
                        tree_view3.heading(4, text="Units")
                        tree_view3.heading(5, text="Blood Type")
                        tree_view3.heading(6, text="Date")
                        tree_view3.heading(7, text="Time")
                        tree_view3.column(1, width=385)
                        tree_view3.column(2, width=385)
                        tree_view3.column(3, width=170)
                        tree_view3.column(4, width=120)
                        tree_view3.column(5, width=120)

                        for a in rows2:
                            tree_view3.insert('', 'end', values=a)

                        cursor2.close()
                        data2.close()

                        data3 = sqlite3.connect('donate.sqlite')
                        cursor3 = data3.cursor()
                        cursor3.execute("SELECT * FROM donate")
                        cursor3.execute("SELECT * FROM donate WHERE (name =?)", [name_get])
                        rows3 = cursor3.fetchall()
                        style3 = ttk.Style()
                        style3.configure("mystyle.Treeview", bd=5, font=("caliber", 16), rowheight=40)
                        tree_view4 = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height=10,
                                                  style="mystyle.Treeview")
                        tree_view4.place(x=0, y=0)
                        tree_view4.heading(1, text="Name")
                        tree_view4.heading(2, text="Email")
                        tree_view4.heading(3, text="Phone")
                        tree_view4.heading(4, text="Units")
                        tree_view4.heading(5, text="Blood Type")
                        tree_view4.heading(6, text="Date")
                        tree_view4.heading(7, text="Time")
                        tree_view4.column(1, width=385)
                        tree_view4.column(2, width=385)
                        tree_view4.column(3, width=170)
                        tree_view4.column(4, width=120)
                        tree_view4.column(5, width=120)

                        for a in rows3:
                            tree_view4.insert('', 'end', values=a)

                        cursor3.close()
                        data3.close()
                    else:
                        user_activity_page.destroy()

                        on_user_activity()

                nav_icon4 = tkinter.Button(user_activity_page, image=photos[5], relief="raised", bd=5,
                                           command=on_click_nav4)
                nav_icon4.place(x=30, y=30)

                frame1 = tkinter.LabelFrame(user_activity_page, bd=10, font=("caliber", 18, "normal"),
                                            text="User Donation")
                frame1.place(x=300, y=120, height=470, width=1620)
                style = ttk.Style()
                style.configure("mystyle.Treeview", bd=5, font=("Caliber", 14), rowheight=40)
                tree_view = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height=10,
                                         style="mystyle.Treeview")
                tree_view.place(x=0, y=0)
                tree_view.heading(1, text="Name")
                tree_view.heading(2, text="Email")
                tree_view.heading(3, text="Phone")
                tree_view.heading(4, text="Units")
                tree_view.heading(5, text="Blood Type")
                tree_view.heading(6, text="Date")
                tree_view.heading(7, text="Time")
                tree_view.column(1, width=385)
                tree_view.column(2, width=385)
                tree_view.column(3, width=170)
                tree_view.column(4, width=120)
                tree_view.column(5, width=120)

                data = sqlite3.connect('donate.sqlite')
                cursor1 = data.cursor()
                cursor1.execute("SELECT * FROM donate")
                rows = cursor1.fetchall()
                for i in rows:
                    tree_view.insert('', 'end', values=i)
                cursor1.close()
                data.close()

                frame2 = tkinter.LabelFrame(user_activity_page, bd=10, font=("caliber", 18, "normal"),
                                            text="User Requests")
                frame2.place(x=300, y=590, height=470, width=1620)
                tree_view2 = ttk.Treeview(frame2, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height=10,
                                          style="mystyle.Treeview")
                tree_view2.place(x=0, y=0)
                tree_view2.heading(1, text="Name")
                tree_view2.heading(2, text="Email")
                tree_view2.heading(3, text="Phone")
                tree_view2.heading(4, text="Requirement")
                tree_view2.heading(5, text="Blood Type")
                tree_view2.heading(6, text="Date")
                tree_view2.heading(7, text="Time")
                tree_view2.column(1, width=385)
                tree_view2.column(2, width=385)
                tree_view2.column(3, width=170)
                tree_view2.column(4, width=120)
                tree_view2.column(5, width=120)

                data = sqlite3.connect('request.sqlite')
                cursor1 = data.cursor()
                cursor1.execute("SELECT * FROM request")
                rows = cursor1.fetchall()
                for i in rows:
                    tree_view2.insert('', 'end', values=i)
                cursor1.close()
                data.close()

                frame3 = tkinter.LabelFrame(user_activity_page, font=("caliber", 18, "normal"), bg="brown")
                frame3.place(x=0, y=120, height=930, width=300)

                name = tkinter.Label(frame3, font=("Times ne Roman", 15, "normal"), text="Name", bg="brown", fg="gold")
                name.place(x=100, y=400)
                name_entry = tkinter.Entry(frame3, font="large")
                name_entry.place(x=20, y=450)

                search_button = tkinter.Button(frame3, bd=8, image=photos[22], command=on_click_search)
                search_button.place(x=100, y=500, height=50)

                note = tkinter.Label(frame3, font=("Times new Roman", 15, "normal"),
                                     text="Note:-\nTo get proper search "
                                          "result, please\n enter full"
                                          " name",
                                     bg="brown", fg="gold")
                note.place(x=5, y=700)

            def on_home():
                # to destroy admin page once registered users button in navigation bar is pressed
                admin_login.destroy()

                on_login_admin()

            # Setting Navbar frame:
            nav_root = tkinter.Frame(admin_login, bg="grey", height=1000, width=700, bd=20)
            nav_root.place(x=30, y=30)

            # Close nav bar photo
            close_nav = tkinter.Button(nav_root, image=photos[6], relief="raised", bd=5, command=on_cross)
            close_nav.place(x=600, y=25, width=40, height=40)

            # setting the frame
            nav_root_frame = tkinter.Frame(nav_root, bd=10, bg="black")
            nav_root_frame.place(x=20, y=80, height=800, width=620)

            # setting contents in the navigation bar
            home_image = tkinter.Label(nav_root, image=photos[12])
            home_image.place(x=50, y=130)
            home = tkinter.Button(nav_root, relief="raised", font=("caliber", 17, "normal"),
                                  text="Home", fg="gold", bg="brown4", bd=5, command=on_home)
            home.place(x=200, y=140, width=210)
            registered_users_img = tkinter.Label(nav_root, image=photos[11])
            registered_users_img.place(x=50, y=330)
            registered_users = tkinter.Button(nav_root, relief="raised", font=("caliber", 17, "normal"),
                                              text="Registered Users", fg="gold", bg="brown4", bd=5,
                                              command=on_registered_users)
            registered_users.place(x=200, y=330, width=210)
            activity_history_img = tkinter.Label(nav_root, image=photos[13])
            activity_history_img.place(x=50, y=520)
            activity_history = tkinter.Button(nav_root, relief="raised", font=("caliber", 17, "normal"),
                                              text="User Activity", fg="gold", bg="brown4", bd=5,
                                              command=on_user_activity)
            activity_history.place(x=200, y=520, width=210)
            queries_user_img = tkinter.Label(nav_root, image=photos[14])
            queries_user_img.place(x=50, y=710)
            queries_user = tkinter.Button(nav_root, relief="raised", font=("caliber", 17, "normal"),
                                          text="User Queries", fg="gold", bg="brown4", bd=5, command=on_queries)
            queries_user.place(x=200, y=710, width=210)

            vertical_border = tkinter.Label(nav_root_frame)
            vertical_border.place(x=130, y=0, width=5, height=800)
            horizontal_border_1 = tkinter.Label(nav_root_frame)
            horizontal_border_1.place(x=0, y=165, width=620, height=5)
            horizontal_border_2 = tkinter.Label(nav_root_frame)
            horizontal_border_2.place(x=0, y=365, width=620, height=5)
            horizontal_border_3 = tkinter.Label(nav_root_frame)
            horizontal_border_3.place(x=0, y=555, width=620, height=5)

        # TO ADD welcome bar at the top
        labeled_ad = tkinter.LabelFrame(admin_login, bd=10, relief="groove", fg="gold", bg="dark blue")
        labeled_ad.place(x=0, y=0, relwidth=1, height=120)
        text_ad_label = tkinter.Label(labeled_ad, text="\t\t\t\t                    Welcome", bg="dark blue",
                                      fg="gold", font=("times new roman", 30, "bold"))
        text_ad_label.grid(row=0, column=0, padx=20, pady=20)

        # Loading Nav Bar icon image
        nav_icon = tkinter.Button(admin_login, image=photos[5], relief="raised", bd=5, command=on_click_nav)
        nav_icon.place(x=30, y=30)

        # setting home page
        what_you_can_do = LabelFrame(admin_login, bd=15, relief="groove", bg="maroon", text="What you can do :-",
                                     font=("times new roman", 25, "normal"), fg="gold")
        what_you_can_do.place(x=270, y=250, height=650, width=1420)

        queries_img = tkinter.Label(what_you_can_do, image=photos[7])
        queries_img.place(x=30, y=40)
        queries1 = tkinter.Label(what_you_can_do, text="Read, answer and manage\n different queries.", bg="maroon",
                                 fg="gold", font=("caliber", 20, "normal"))
        queries1.place(x=200, y=65)
        manage_img = tkinter.Label(what_you_can_do, image=photos[8])
        manage_img.place(x=30, y=360)
        manage1 = tkinter.Label(what_you_can_do, text="Manage user access to\n Blood Bank page", bg="maroon",
                                fg="gold", font=("caliber", 20, "normal"))
        manage1.place(x=200, y=380)
        user_data_img = tkinter.Label(what_you_can_do, image=photos[9])
        user_data_img.place(x=700, y=40)
        user_data = tkinter.Label(what_you_can_do, text="View activity history of\n the user", bg="maroon",
                                  fg="gold", font=("caliber", 20, "normal"))
        user_data.place(x=870, y=65)
        database_img = tkinter.Label(what_you_can_do, image=photos[10])
        database_img.place(x=700, y=360)
        database = tkinter.Label(what_you_can_do, text="Manage and monitor Blood\n bank databases", bg="maroon",
                                 fg="gold", font=("caliber", 20, "normal"))
        database.place(x=870, y=385)

    else:
        messagebox.showerror("Error", "Invalid Username or Password!!", parent=mainWindow)


def queries_sec():
    def on_click_clear():
        qna_name_entry.delete(0, 'end')
        qna_email_entry.delete(0, 'end')
        qna_subject_entry.delete(0, 'end')
        qna_message_entry.delete(1.0, 'end')
        qna_contact_entry.delete(0, 'end')

    def on_click_send():
        if len(qna_name_entry.get()) > 2:
            if qna_email_entry.get()[-4:] == ".com":
                if len(qna_contact_entry.get()) == 10:
                    if len(qna_subject_entry.get()) > 3:
                        db3 = sqlite3.connect("queries.sqlite")
                        db3.execute("CREATE TABLE IF NOT EXISTS queries(name TEXT, email TEXT, phone INTEGER,"
                                    " subject TEXT, message TEXT)")
                        db3.execute("INSERT INTO queries(name, email, phone, subject, message) "
                                    "                                    VALUES(?, ?, ?, ?, ?)",
                                    (qna_name_entry.get(), qna_email_entry.get(), qna_contact_entry.get(),
                                     qna_subject_entry.get(), qna_message_entry.get(1.0, 'end')))
                        cursor = db3.cursor()
                        cursor.execute("SELECT * FROM queries")
                        db3.commit()
                        cursor.close()
                        db3.close()
                        messagebox.showinfo("Success", "Yay!! We have received your message.", parent=qna_page)
                        on_click_clear()
                    else:
                        messagebox.showerror("Error", "Invalid Subject\nPlease Write a proper subject", parent=qna_page)
                else:
                    messagebox.showerror("Error", "Invalid Phone Number", parent=qna_page)
            else:
                messagebox.showerror("Error", "Invalid Email Address", parent=qna_page)
        else:
            messagebox.showerror("Error", "Invalid Name", parent=qna_page)

    # to set up new page for q&a
    qna_page = Toplevel()
    qna_page.geometry("1920x1080+-5+-1")
    qna_page.config(bg="maroon")
    qna_page.title("Queries")

    # to set up image as the bg of the q&a page
    background2 = tkinter.Label(qna_page, image=photos[16])
    background2.place(x=0, y=0)

    # to set up the Label at the top
    qna_label = tkinter.Label(qna_page, bd=10, relief="groove", fg="gold", bg="dark blue")
    qna_label.place(x=0, y=0, relwidth=1, height=120)
    qna_text_label = tkinter.Label(qna_label, text="\t\t\t\t\t     Queries", bg="dark blue", fg="gold",
                                   font=("times new roman", 30, "bold"))
    qna_text_label.grid(row=0, column=0, padx=20, pady=20)

    # to set up the frame and labels in it
    qna_frame = tkinter.Frame(qna_page, bg="grey", bd=10)
    qna_frame.place(x=700, y=200, width=1100, height=700)
    qna_name = tkinter.Label(qna_frame, text="Name", font=("caliber", 25, "bold"), bg="grey")
    qna_name.place(x=20, y=10)
    qna_email = tkinter.Label(qna_frame, text="Email", font=("caliber", 25, "bold"), bg="grey")
    qna_email.place(x=600, y=10)
    qna_contact = tkinter.Label(qna_frame, text="Phone", font=("caliber", 25, "bold"), bg="grey")
    qna_contact.place(x=20, y=100)
    qna_subject = tkinter.Label(qna_frame, text="Subject", font=("caliber", 25, "bold"), bg="grey")
    qna_subject.place(x=20, y=200)
    qna_message = tkinter.Label(qna_frame, text="Message", font=("caliber", 25, "bold"), bg="grey")
    qna_message.place(x=20, y=300)
    qna_message_entry = scrolledtext.ScrolledText(qna_frame, font=("caliber", 16, "normal"))
    qna_message_entry.place(x=20, y=360, height=290, width=1040)
    qna_contact_entry = tkinter.Entry(qna_frame, font=("caliber", 16, "normal"))
    qna_contact_entry.place(x=180, y=110)
    qna_name_entry = tkinter.Entry(qna_frame, font=("caliber", 16, "normal"))
    qna_name_entry.place(x=180, y=20, width=350)
    qna_email_entry = tkinter.Entry(qna_frame, font=("caliber", 16, "normal"))
    qna_email_entry.place(x=720, y=20, width=350)
    qna_subject_entry = tkinter.Entry(qna_frame, font=("caliber", 16, "normal"))
    qna_subject_entry.place(x=180, y=210, width=800)

    # send message, clear message, back button
    qna_send_message = tkinter.Button(qna_page, image=photos[17], bd=5, bg="black", command=on_click_send)
    qna_send_message.place(x=1300, y=930)
    qna_clear_message = tkinter.Button(qna_page, image=photos[18], bd=5, bg="black", command=on_click_clear)
    qna_clear_message.place(x=1100, y=930)


def on_click_why():
    pygame.init()
    video_name = "mp4.mp4"
    video = imageio.get_reader(video_name)
    pygame.mixer.music.load("mp3.mp3")

    def stream(label):
        pygame.mixer.music.play()
        for image in video.iter_data():
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image
        wait_n_destroy()

    if __name__ == "__main__":
        root = tkinter.Toplevel()
        root.geometry("1920x1080")
        root.attributes('-disabled', True)
        root.overrideredirect(True)
        root.config(bg="red")
        my_label = tkinter.Label(root)
        my_label.place(x=0, y=0, height=1080, width=1920)
        thread = threading.Thread(target=stream, args=(my_label,))
        thread.daemon = 1
        thread.start()

    def wait_n_destroy():
        time.sleep(2)
        root.destroy()


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

# to make contact us button
contact_us = tkinter.Button(bd=5, relief="raised", image=photos[15], bg="black", command=queries_sec)
contact_us.place(x=1800, y=24)

# to present the logo
logo = tkinter.Label(labeled, image=photos[20])
logo.place(x=620, y=20)


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
                                                                                      "normal"), show="*")
username_entry_password_user.grid(row=3, column=1, padx=30)
print(username_entry_user.get())

username_hospital = tkinter.Label(login_frame_hospital, image=photos[0], bd=5)
username_hospital.grid(row=0, column=0, pady=30, padx=20)
username_entry_hospital = tkinter.Entry(login_frame_hospital, relief="groove", font=("large_font", 15,
                                                                                     "normal"))
username_entry_hospital.grid(row=0, column=1, padx=30)
username_password_hospital = tkinter.Label(login_frame_hospital, image=photos[1], bd=5)
username_password_hospital.grid(row=3, column=0)
username_entry_password_hospital = tkinter.Entry(login_frame_hospital, relief="groove", font=("large_font", 15,
                                                                                              "normal"), show="*")
username_entry_password_hospital.grid(row=3, column=1)


# login buttons
user_login = tkinter.Button(login_frame_user, text="Login", bg="Green", fg="white", font=("caliber", 15, "italic bold"),
                            padx=40, relief="raised", command=login)
user_login.grid(row=4, column=1, pady=10)

hospital_login = tkinter.Button(login_frame_hospital, text="Login", bg="Green", fg="white",
                                font=("caliber", 15, "italic bold"), padx=40, relief="raised", command=on_login_admin)
hospital_login.grid(row=4, column=1, pady=10)
user_signup = tkinter.Button(login_frame_user, text="Sign Up!!", bg="red2", fg="white",
                             font=("caliber", 15, "italic bold"), padx=40, relief="raised", command=register)
user_signup.grid(row=5, column=1, pady=10)

# why donate blood button
why = tkinter.Button(mainWindow, font=("Times new Roman", 20, "normal"), bd=5, text="-----WHY DONATE BLOOD ?-----",
                     fg="gold", bg="black", relief="raised", command=on_click_why)
why.place(x=770, y=730)
mainWindow.mainloop()
