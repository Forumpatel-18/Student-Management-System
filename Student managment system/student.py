from ast import Delete
from calendar import c
from importlib.resources import contents
from logging import root
from multiprocessing.dummy import Manager
from optparse import Values
from re import L
from sqlite3 import Cursor
from this import d, s
from tkinter import*
from tkinter import ttk
from turtle import update
# from turtle import st, width
from webbrowser import get
# from xmlrpc.client import _HostType
import mysql.connector
from PIL import Image, ImageTk  # pip intsall pillow(PIL-pillow)
from tkinter import messagebox


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Student Management System')

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_sem = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_rollno = StringVar()
        self.var_Division = StringVar()
        self.var_dob = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()

        # for image
        img1 = Image.open("college_images/university.jpg")
        # antialias coverts high level image to low level
        img1 = img1.resize((700, 160), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # 1st image
        self.btn_1 = Button(self.root, image=self.photoimg1, cursor='hand2')
        self.btn_1.place(x=0, y=0, width=700, height=160)

        # 2nd image
        img2 = Image.open("college_images/graduation.jpeg")
        # antialias coverts high level image to low level
        img2 = img2.resize((700, 160), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        self.btn_2 = Button(self.root, image=self.photoimg2, cursor='hand2')
        self.btn_2.place(x=700, y=0, width=700, height=160)

        # bg image
        img4 = Image.open("college_images/university1.jpg")
        # antialias coverts high level image to low level
        img4 = img4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_lb1 = Label(self.root, image=self.photoimg4, bd=2, relief=RIDGE)
        bg_lb1.place(x=0, y=160, width=1530, height=710)

        # label title
        lb1_title = Label(bg_lb1, text='STUDENT MANAGEMENT SYSTEM', font=(
            'times new roman', 37, 'bold'), fg='white', bg='black')
        lb1_title.place(x=0, y=0, width=1530, height=40)

        #manageframe#
        Manage_frame = Frame(bg_lb1, bd=2, relief=RIDGE, bg='white')
        Manage_frame.place(x=0, y=40, width=1530, height=500)

        # LEFTPART
        # left frame
        DataLeftFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text='Student Information',
                                   font=('times new roman', 15, 'bold'), fg='red', bg='white')
        DataLeftFrame.place(x=10, y=7, width=600, height=480)

        # current course information
        std_lb1_info_frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text='Current course Information', font=(
            'times new roman', 15, 'bold'), fg='red', bg='white')
        std_lb1_info_frame.place(x=0, y=0, width=590, height=150)

       # Department
        lbl_dep = Label(std_lb1_info_frame, text='Department', font=(
            'arial', 15, 'bold'), fg='black', bg='white')
        lbl_dep.grid(row=0, column=0, padx=2, pady=5, sticky=W)
        combo_dep = ttk.Combobox(
            std_lb1_info_frame, textvariable=self.var_dep, font=('arial', 10), width=17, state="readonly")
        combo_dep['value'] = ("Select Department",
                              "COMPS", "IT", "EXTC", "MECH")
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1  # (dep takes column 0 so now column 1)#
                       , padx=2, pady=5, sticky=W)

        # course
        course_std = Label(std_lb1_info_frame, text='course', font=(
            'arial', 15, 'bold'), fg='black', bg='white')
        course_std.grid(row=1, column=0, padx=2, pady=5, sticky=W)
        course_txtcourse_std = ttk.Combobox(
            std_lb1_info_frame, textvariable=self.var_course, font=('arial', 10), width=17, state="readonly")
        course_txtcourse_std['value'] = ("Select Year",
                                         "FE", "SE", "TE", "BE")
        course_txtcourse_std.current(0)
        course_txtcourse_std.grid(row=1, column=1  # (dep takes column 0 so now column 1)#
                                  , padx=2, pady=5, sticky=W)

        # Semester
        sem_std = Label(std_lb1_info_frame, text='Semester', font=(
            'arial', 15, 'bold'), fg='black', bg='white')
        sem_std.grid(row=2, column=0, padx=2, pady=5, sticky=W)
        sem_txtcourse_std = ttk.Combobox(
            std_lb1_info_frame, textvariable=self.var_sem, font=('arial', 10), width=17, state="readonly")
        sem_txtcourse_std['value'] = ("Select Semester",
                                      "Summer(May)", "Winter(Dec)")
        sem_txtcourse_std.current(0)
        sem_txtcourse_std.grid(row=2, column=1  # (dep takes column 0 so now column 1)#
                               , padx=2, pady=5, sticky=W)

        # student class label information
        std_lb1_class_frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text='Student Information', font=(
            'times new roman', 15, 'bold'), fg='red', bg='white')
        std_lb1_class_frame.place(x=0, y=155, width=590, height=250)

        # PID
        lbl_pid = Label(std_lb1_class_frame, text='Student PID', font=(
            'arial', 15, 'bold'), fg='black', bg='white')
        lbl_pid.grid(row=0, column=0, padx=2, pady=7, sticky=W)
        id_entry = ttk.Entry(std_lb1_class_frame, textvariable=self.var_std_id, font=(
            'arial', 13), width=18)
        id_entry.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        # Name
        lbl_name = Label(std_lb1_class_frame, text='Student Name', font=(
            'arial', 15, 'bold'), fg='black', bg='white')
        lbl_name.grid(row=1, column=0, padx=2, pady=7, sticky=W)
        name_entry = ttk.Entry(std_lb1_class_frame, textvariable=self.var_std_name, font=(
            'arial', 13), width=18)
        name_entry.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        # Divisionision
        lbl_Division = Label(std_lb1_class_frame, text='Division', font=(
            'arial', 15, 'bold'), fg='black', bg='white')
        lbl_Division.grid(row=0, column=2, padx=2, pady=7, sticky=W)
        Division_entry = ttk.Entry(std_lb1_class_frame, textvariable=self.var_Division, font=(
            'arial', 13), width=18)
        Division_entry.grid(row=0, column=3, padx=2, pady=7, sticky=W)

        # Roll NO
        lbl_rollno = Label(std_lb1_class_frame, text='RollNo', font=(
            'arial', 15, 'bold'), fg='black', bg='white')
        lbl_rollno.grid(row=1, column=2, padx=2, pady=7, sticky=W)
        rollno_entry = ttk.Entry(std_lb1_class_frame, textvariable=self.var_rollno, font=(
            'arial', 13), width=18)
        rollno_entry.grid(row=1, column=3, padx=2, pady=7, sticky=W)

        # Gender
        lbl_gender = Label(std_lb1_class_frame, text='Gender', font=(
            'arial', 15, 'bold'), fg='black', bg='white')
        lbl_gender.grid(row=2, column=0, padx=2, pady=7, sticky=W)
        lbl_gender_std = ttk.Combobox(
            std_lb1_class_frame, textvariable=self.var_gender, font=('arial', 10), width=21, state="readonly")
        lbl_gender_std['value'] = ("Select Gender",
                                   "Male", "Female", "Other")
        lbl_gender_std.current(0)
        lbl_gender_std.grid(row=2, column=1  # (dep takes column 0 so now column 1)#
                            , padx=2, pady=10, sticky=W)

        # DOB
        lbl_dob = Label(std_lb1_class_frame, text='DOB', font=(
            'arial', 15, 'bold'), fg='black', bg='white')
        lbl_dob.grid(row=2, column=2, padx=2, pady=7, sticky=W)
        dob_entry = ttk.Entry(std_lb1_class_frame, textvariable=self.var_dob, font=(
            'arial', 13), width=18)
        dob_entry.grid(row=2, column=3, padx=2, pady=7, sticky=W)

        # Email
        lbl_email = Label(std_lb1_class_frame, text='Email', font=(
            'arial', 15, 'bold'), fg='black', bg='white')
        lbl_email.grid(row=3, column=0, padx=2, pady=7, sticky=W)
        email_entry = ttk.Entry(std_lb1_class_frame, textvariable=self.var_email, font=(
            'arial', 13), width=18)
        email_entry.grid(row=3, column=1, padx=2, pady=7, sticky=W)

        # Phone
        lbl_phone = Label(std_lb1_class_frame, text='Phone', font=(
            'arial', 15, 'bold'), fg='black', bg='white')
        lbl_phone.grid(row=3, column=2, padx=2, pady=7, sticky=W)
        phone_entry = ttk.Entry(std_lb1_class_frame, textvariable=self.var_phone, font=(
            'arial', 13), width=18)
        phone_entry.grid(row=3, column=3, padx=2, pady=7, sticky=W)

        # Address
        lbl_address = Label(std_lb1_class_frame, text='Address', font=(
            'arial', 15, 'bold'), fg='black', bg='white')
        lbl_address.grid(row=4, column=0, padx=2, pady=7, sticky=W)
        address_entry = ttk.Entry(std_lb1_class_frame, textvariable=self.var_address, font=(
            'arial', 13), width=18)
        address_entry.grid(row=4, column=1, padx=2, pady=7, sticky=W)

        # Buttonframe
        btn_frame = Frame(DataLeftFrame, bd=2, relief=RIDGE, bg='white')
        btn_frame.place(x=0, y=405, width=590, height=35)

        # add
        btn_save = Button(btn_frame, text='Save', command=self.add_data, font=(
            'arial', 11, 'bold'), width=15, fg='white', bg='green')
        btn_save.grid(row=0, column=0, sticky=W, padx=2)

        # update
        btn_update = Button(btn_frame, text='Update', command=self.update_data, font=(
            'arial', 11, 'bold'), width=15, fg='white', bg='green')
        btn_update.grid(row=0, column=1, sticky=W, padx=2)

        # delete
        btn_delete = Button(btn_frame, text='Delete', command=self.delete_data, font=(
            'arial', 11, 'bold'), width=15, fg='white', bg='green')
        btn_delete.grid(row=0, column=2, sticky=W, padx=2)

        # reset
        btn_reset = Button(btn_frame, text='Reset', command=self.reset_data, font=(
            'arial', 11, 'bold'), width=15, fg='white', bg='green')
        btn_reset.grid(row=0, column=3, sticky=W, padx=2)

        # RIGHTPART
        # right frame
        DataRightFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, text='Information', padx=2,
                                    font=('times new roman', 15, 'bold'), fg='red', bg='white')
        DataRightFrame.place(x=620, y=7, width=720, height=480)

        # search frame
        SearchFrame = LabelFrame(DataRightFrame, bd=4, relief=RIDGE, padx=2, text='Search Student Information',
                                 font=('times new roman', 15, 'bold'), fg='red', bg='white')
        SearchFrame.place(x=0, y=0, width=710, height=100)

        lbl_searchby = Label(SearchFrame, text='Search By:', font=(
            'arial', 15, 'bold'), fg='Black', bg='Grey')
        lbl_searchby.grid(row=0, column=0, padx=2, sticky=W)

        self.var_com_search = StringVar()
        seach_combobox = ttk.Combobox(
            SearchFrame, textvariable=self.var_com_search, font=('arial', 10), width=17, state="readonly")
        seach_combobox['value'] = ("Select Option",
                                   "Student_PID", "StudentName", "Department", "Email")
        seach_combobox.current(0)
        seach_combobox.grid(row=0, column=1  # (dep takes column 0 so now column 1)#
                            , padx=5, sticky=W)

        self.var_search = StringVar()
        name_entry = ttk.Entry(SearchFrame, textvariable=self.var_search, font=(
            'arial', 13), width=18)
        name_entry.grid(row=0, column=2, padx=5, sticky=W)

        # search btn
        btn_search = Button(SearchFrame, text='Search', command=self.search_data, font=(
            'arial', 11, 'bold'), width=15, fg='white', bg='Orange')
        btn_search.grid(row=0, column=3, sticky=W, padx=5)

        # show btn
        btn_showall = Button(SearchFrame, text='Show All', command=self.fetch_data, font=(
            'arial', 11, 'bold'), width=15, fg='white', bg='orange')
        btn_showall.grid(row=1, column=3, sticky=W, padx=5, pady=6)

        ################STUDENT TABLE AND SCROLL BAR###################
        table_frame = Frame(DataRightFrame, bd=4, relief=RIDGE)
        table_frame.place(x=0, y=100, width=710, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=(
            "Department", "course", "Semester", "Student_PID", "StudentName", "RollNo", "Division", "Gender", "DOB", "Phone", "Email", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department", text="Department")
        self.student_table.heading("course", text="course")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Student_PID", text="Student_PID")
        self.student_table.heading("StudentName", text="StudentName")
        self.student_table.heading("RollNo", text="RollNo")
        self.student_table.heading("Division", text="Division")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Address", text="Address")

        self.student_table["show"] = "headings"
        self.student_table.column('Department', width=100)
        self.student_table.column('course', width=100)
        self.student_table.column('Semester', width=100)
        self.student_table.column('Student_PID', width=100)
        self.student_table.column('StudentName', width=100)
        self.student_table.column('RollNo', width=100)
        self.student_table.column('Division', width=100)
        self.student_table.column('Gender', width=100)
        self.student_table.column('DOB', width=100)
        self.student_table.column('Phone', width=100)
        self.student_table.column('Email', width=100)
        self.student_table.column('Address', width=100)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind('<ButtonRelease>', self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if (self.var_dep.get() == "" or self.var_std_id.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_std_name.get() == "" or self.var_Division.get() == "" or self.var_Division.get() == "" or self.var_dob.get() == "" or self.var_sem.get() == "" or self.var_course.get() == "" or self.var_address.get() == "" or self.var_rollno.get() == ""):
            messagebox.showerror('Error', "All Fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', username="root", password="Forpat@123", database="sys")
                my_cursur = conn.cursor()
                my_cursur.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                    self.var_dep.get(), self.var_course.get(), self.var_sem.get(
                    ), self.var_std_id.get(), self.var_std_name.get(),
                    self.var_rollno.get(), self.var_Division.get(
                    ), self.var_gender.get(), self.var_dob.get(), self.var_phone.get(),
                    self.var_email.get(), self.var_address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    'Success', 'Successfully Added', parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    'Error', f"Due to:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host='localhost', username="root", password="Forpat@123", database="sys")
        my_cursur = conn.cursor()
        my_cursur.execute("select * from  student")
        data = my_cursur.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=''):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content['values']

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_sem.set(data[2])
        self.var_std_id.set(data[3])
        self.var_std_name.set(data[4])
        self.var_rollno.set(data[5])
        self.var_Division.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_phone.set(data[9])
        self.var_email.set(data[10])
        self.var_address.set(data[11])

    def update_data(self):
        if (self.var_dep.get() == "" or self.var_std_id.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_std_name.get() == "" or self.var_Division.get() == "" or self.var_dob.get() == "" or self.var_sem.get() == "" or self.var_course.get() == "" or self.var_address.get() == "" or self.var_rollno.get() == "" or self.var_gender.get() == ""):
            messagebox.showerror('Error', "All Fields are required")
        else:
            try:
                update = messagebox.askyesno(
                    'Update', 'Are you sure you want to update?', parent=self.root)

                if update > 0:
                    conn = mysql.connector.connect(
                        host='localhost', username="root", password="Forpat@123", database="sys")
                    my_cursur = conn.cursor()
                    my_cursur.execute(
                        'Update student set Department=%s,course=%s,Semester=%s,StudentName=%s,RollNo=%s,Division=%s,Gender=%s,DOB=%s,Phone=%s,Email=%s,Address=%s where Student_PID=%s',
                        (self.var_dep.get(), self.var_course.get(), self.var_sem.get(), self.var_std_name.get(),
                         self.var_rollno.get(), self.var_Division.get(
                        ), self.var_gender.get(), self.var_dob.get(),
                            self.var_phone.get(), self.var_email.get(), self.var_address.get(), self.var_std_id.get()))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Successfully updated", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    'Error', f"Due to:{str(es)}", parent=self.root)

    def delete_data(self):
        if (self.var_std_id.get() == ""):
            messagebox.showerror(
                'Error', "All Fields are required", parent=self.root)

        else:
            try:
                Delete = messagebox.askyesno(
                    'Delete', 'Are you sure you want to delete?', parent=self.root)
                if Delete > 0:
                    conn = mysql.connector.connect(
                        host='localhost', username="root", password="Forpat@123", database="sys")
                    my_cursur = conn.cursor()
                    sql = 'Delete from student where Student_PID=%s'
                    value = (self.var_std_id.get(),)
                    my_cursur.execute(sql, value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully deleted", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    'Error', f"Due to:{str(es)}", parent=self.root)

    def reset_data(self):

        self.var_dep.set('Select Department')
        self.var_course.set('Select Year')
        self.var_sem.set('Select Semester')
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_rollno.set("")
        self.var_Division.set("")
        self.var_gender.set('Select Gender')
        self.var_dob.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_address.set("")

    #search data#

    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror('Error', 'Please Select option')

        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', username="root", password="Forpat@123", database="sys")
                my_cursur = conn.cursor()
                my_cursur.execute(
                    "select * from student where " + str(self.var_com_search.get())+" LIKE '%" + str(self.var_search.get())+"%'")
                data = my_cursur.fetchall()
                if len(data) != 0:
                    self.student_table.delete(
                        *self.student_table.get_children())
                    for i in data:
                        self.student_table.insert('', END, values=i)

                    conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror(
                    'Error', f"Due to:{str(es)}", parent=self.root)


# for displayig the main window
if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()
