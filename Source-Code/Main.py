from tkinter import *
import qrcode
from PIL import ImageTk
from resizeimage import resizeimage


class Qr_Generator:
    def __init__(self, win):
        self.win = win
        self.win.geometry("900x500+300+150")
        self.win.title("QR Code Generator")
        self.win.resizable(False, False)

        title = Label(self.win, text="QR Code Generator", font=("times new roman", 40), bg="#053246", fg="white")
        title.place(x=0, y=0, relwidth=1)

        # Variables
        self.var_emp_id = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_designation = StringVar()

        # The first window
        global emp_frame
        # Labels
        emp_frame = Frame(self.win, bd=2, relief=RIDGE, bg="white")
        emp_frame.place(x=50, y=100, width=500, height=380)

        emp_title = Label(emp_frame, text="Employee Details", font=("goudy old style", 20), bg="#043256", fg="white")
        emp_title.place(x=0, y=0, relwidth=1)

        lbl_emp_id = Label(emp_frame, text="Employee ID", font=("times new roman", 15, "bold"), bg="white")
        lbl_emp_id.place(x=30, y=60)

        lbl_name = Label(emp_frame, text="Name", font=("times new roman", 15, "bold"), bg="white")
        lbl_name.place(x=30, y=110)

        lbl_department = Label(emp_frame, text="Department", font=("times new roman", 15, "bold"), bg="white")
        lbl_department.place(x=30, y=160)

        lbl_designation = Label(emp_frame, text="Designation", font=("times new roman", 15, "bold"), bg="white")
        lbl_designation.place(x=30, y=210)

        txt_emp_id = Entry(emp_frame, text="Employee ID", font=("goudy old style", 15), textvariable=self.var_emp_id, bg="LightBlue")
        txt_emp_id.place(x=200, y=60)

        # Entries
        txt_name = Entry(emp_frame, text="Name", font=("goudy old style", 15), textvariable=self.var_name, bg="LightBlue")
        txt_name.place(x=200, y=110)

        txt_department = Entry(emp_frame, text="Department", font=("goudy old style", 15), textvariable=self.var_department, bg="LightBlue")
        txt_department.place(x=200, y=160)

        txt_designation = Entry(emp_frame, text="Designation", font=("goudy old style", 15), textvariable=self.var_designation, bg="LightBlue")
        txt_designation.place(x=200, y=210)

        btn_generate = Button(emp_frame, text="Generate", command=self.generate, font=("times new roman", 18, "bold"), bg="#2196f3", fg="white")
        btn_generate.place(x=30, y=290, width=180, height=30)

        btn_clear = Button(emp_frame, text="Clear", command=self.clear, font=("times new roman", 18, "bold"), bg="#600f0f", fg="white")
        btn_clear.place(x=282, y=290, width=120, height=30)

        # The second window
        global qr_frame
        qr_frame = Frame(self.win, bd=2, relief=RIDGE, bg="white")
        qr_frame.place(x=600, y=100, width=250, height=380)

        qr_title = Label(qr_frame, text="Employee QR Code", font=("goudy old style", 19), bg="#043256", fg="white")
        qr_title.place(x=0, y=0, relwidth=1)

        self.qr_code = Label(qr_frame, text="No QR \nAvailable", font=("times new roman", 15), bg='#3f51b5', bd=3, relief=RAISED, fg="white")
        self.qr_code.place(x=35, y=64, width=180, height=180)

        btn_save = Button(qr_frame, text="Save", command=self.save, font=("times new roman", 18, "bold"), bg="#2196f3", fg="white")
        btn_save.place(x=65, y=290, width=120, height=30)

    # QR generation part
    def generate(self):
        if self.var_emp_id.get().isnumeric() == "" or self.var_name.get().isalpha() == "" or self.var_department.get() == "" or self.var_designation.get() == "":
            self.msg = "All fields are required!"
            self.lbl_msg = Label(emp_frame, text=self.msg, font=("times new roman", 18, "bold"), bg='red',
                                 fg="white").place(x=0, y=345, relwidth=1)
        else:
            if self.var_emp_id.get().isnumeric() and self.var_name.get().isalpha() and self.var_department.get().isalpha() and self.var_designation.get().isalpha():
                qr_data = f"Employee ID: {self.var_emp_id.get()}\nEmployee Name: {self.var_name.get()}\nDepartment: {self.var_department.get()}\nDesignation: {self.var_designation.get()}\n"
                global qr_code
                qr_code = qrcode.make(qr_data)
                qr_code = resizeimage.resize_cover(qr_code, [180, 180])

                self.img = ImageTk.PhotoImage(qr_code)
                self.qr_code = Label(qr_frame, image=self.img, font=("times new roman", 15), bg='#3f51b5',
                                     fg="white").place(x=35, y=64, width=180, height=180)

                self.msg = "QR Code has been Generated Successfully!"
                self.lbl_msg = Label(emp_frame, text=self.msg, font=("times new roman", 18, "bold"), bg='green',
                                     fg="white").place(x=0, y=345, relwidth=1)
            else:
                self.msg = "Your inputs are not valid, Please check them"
                self.lbl_msg = Label(emp_frame, text=self.msg, font=("times new roman", 18, "bold"), bg='red',
                                     fg="white").place(x=0, y=345, relwidth=1)

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_designation.set("")
        self.msg = ""
        self.lbl_msg = Label(emp_frame, text=self.msg, font=("times new roman", 18, "bold"), bg="white")
        self.lbl_msg.place(x=0, y=345, relwidth=1)
        self.qr_code = Label(qr_frame, text="No QR \nAvailable", font=("times new roman", 15), bg='#3f51b5', bd=3, relief=RAISED, fg="white")
        self.qr_code.place(x=35, y=64, width=180, height=180)

    def save(self):
        qr_code.save("Emp_QR/Emp_" + str(self.var_emp_id.get()) + ".png")


win = Tk()
obj = Qr_Generator(win)
win.mainloop()
