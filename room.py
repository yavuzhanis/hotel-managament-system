from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class RoomBooking:
    def __init__(self, root):

        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1460x570+240+294")
        # ?  ------------------variables------------------

        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomAvailable = StringVar()
        self.var_meal = StringVar()
        self.var_noOfdays = StringVar()
        self.var_paidTax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        #! Style and theme setup
        style = ttk.Style()
        style.theme_use("clam")
        #! TITLE
        lbl_title = Label(
            self.root,
            text=" ROOMBOOKING DETAILS",
            font=("times new roman", 40, "bold"),
            bg="black",
            fg="gold",
            bd=4,
            relief=RIDGE,
        )
        lbl_title.place(x=0, y=0, width=1460, height=60)

        # ! LOGO
        img2 = Image.open(r"./images/logo-hotel.png")
        img2 = img2.resize((150, 50), Image.LANCZOS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        lblImg = Label(self.root, image=self.photoImg2, bd=0, relief=RIDGE)
        lblImg.place(x=0, y=0, width=150, height=60)

        #! label frame
        LabelFrameleft = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="RoomBooking Details",
            font=("times new roman", 14, "bold"),
            padx=2,
        )
        LabelFrameleft.place(x=5, y=60, width=425, height=490)

        #! labels and entrys
        lbl_cust_contact = Label(
            LabelFrameleft,
            text="Customer Contact:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        enty_contact = ttk.Entry(
            LabelFrameleft,
            width=26,
            textvariable=self.var_contact,
            font=("times new roman", 13, "bold"),
        )
        enty_contact.grid(row=0, column=1, sticky=W)
        #! fetch data button
        btnfetchData = Button(
            LabelFrameleft,
            command=self.fetch_contact,
            text="Fetch Data",
            font=("times new roman", 12, "bold"),
            bg="gold",
            fg="black",
            width=10,
        )
        btnfetchData.place(x=320, y=3)
        #! check IN date
        check_in_date = Label(
            LabelFrameleft,
            font=("times new roman", 13, "bold"),
            text="Check In DATE:",
            padx=2,
            pady=6,
        )
        check_in_date.grid(row=1, column=0, sticky=W)
        text_check_in_date = ttk.Entry(
            LabelFrameleft,
            textvariable=self.var_checkin,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        text_check_in_date.grid(row=1, column=1)
        #! check OUT date
        check_out_date = Label(
            LabelFrameleft,
            font=("times new roman", 13, "bold"),
            text="CheckOUT DATE:",
            padx=2,
            pady=6,
        )
        check_out_date.grid(row=2, column=0, sticky=W)
        text_check_out_date = ttk.Entry(
            LabelFrameleft,
            textvariable=self.var_checkout,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        text_check_out_date.grid(row=2, column=1)

        # ? ROOM TYPE
        label_Room_Type = Label(
            LabelFrameleft,
            font=("times new roman", 13, "bold"),
            text="Room Type:",
            padx=2,
            pady=6,
        )
        label_Room_Type.grid(row=3, column=0, sticky=W)

        combo_roomType = ttk.Combobox(
            LabelFrameleft,
            textvariable=self.var_roomtype,
            font=("arial", 12, "bold"),
            width=27,
            state="readonly",
        )
        combo_roomType["value"] = ("Single", "Double", "Luxury")
        combo_roomType.current(0)
        combo_roomType.grid(row=3, column=1)

        # TODO avaliable ROOM
        lblRoomAvaliable = Label(
            LabelFrameleft,
            font=("times new roman", 13, "bold"),
            text="Avaliable Room:",
            padx=2,
            pady=6,
        )
        lblRoomAvaliable.grid(row=4, column=0, sticky=W)

        lblRoomAvaliable_text = ttk.Entry(
            LabelFrameleft,
            textvariable=self.var_roomAvailable,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        lblRoomAvaliable_text.grid(row=4, column=1)
        #! meals
        lblMeal = Label(
            LabelFrameleft,
            font=("times new roman", 13, "bold"),
            text=" Meals:",
            padx=2,
            pady=6,
        )
        lblMeal.grid(row=5, column=0, sticky=W)

        lblMeal_text = ttk.Entry(
            LabelFrameleft,
            textvariable=self.var_meal,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        lblMeal_text.grid(row=5, column=1)

        # ? NO OF DAYS
        lblNo_OfDays = Label(
            LabelFrameleft,
            font=("times new roman", 13, "bold"),
            text=" No Of Days:",
            padx=2,
            pady=6,
        )
        lblNo_OfDays.grid(row=6, column=0, sticky=W)

        lblNo_OfDays_text = ttk.Entry(
            LabelFrameleft,
            textvariable=self.var_noOfdays,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        lblNo_OfDays_text.grid(row=6, column=1)

        # ? paid tax
        lblpaid_tax = Label(
            LabelFrameleft,
            font=("times new roman", 13, "bold"),
            text=" Paid Tax:",
            padx=2,
            pady=6,
        )
        lblpaid_tax.grid(row=7, column=0, sticky=W)

        lblpaid_tax_text = ttk.Entry(
            LabelFrameleft,
            textvariable=self.var_paidTax,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        lblpaid_tax_text.grid(row=7, column=1)

        # ? Sub total
        lblSubTotal = Label(
            LabelFrameleft,
            font=("times new roman", 13, "bold"),
            text="Sub Total:",
            padx=2,
            pady=6,
        )
        lblSubTotal.grid(row=8, column=0, sticky=W)

        lblSubTotal_text = ttk.Entry(
            LabelFrameleft,
            textvariable=self.var_actualtotal,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        lblSubTotal_text.grid(row=8, column=1)

        # ? total cost
        lbltotal = Label(
            LabelFrameleft,
            font=("times new roman", 13, "bold"),
            text=" Total Cost:",
            padx=2,
            pady=6,
        )
        lbltotal.grid(row=9, column=0, sticky=W)

        lbltotal_text = ttk.Entry(
            LabelFrameleft,
            textvariable=self.var_total,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        lbltotal_text.grid(row=9, column=1)

        #! ------------------------------------------Bill Button ----------------------------------------------------------------

        btnBill = Button(
            LabelFrameleft,
            text="Bill",
            font=("times new roman", 12, "bold"),
            bg="gold",
            fg="black",
            width=10,
        )
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        #! buttons
        btn_frame = Frame(LabelFrameleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=30)

        btnAdd = Button(
            btn_frame,
            text="Add",
            font=("times new roman", 12, "bold"),
            bg="gold",
            fg="black",
            width=10,
        )
        btnAdd.grid(row=0, column=0, padx=1, sticky=W)

        btnUpdate = Button(
            btn_frame,
            text="Update",
            font=("times new roman", 12, "bold"),
            bg="gold",
            fg="black",
            width=10,
        )
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(
            btn_frame,
            text="Delete",
            font=("times new roman", 12, "bold"),
            bg="red",
            fg="black",
            width=10,
        )
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(
            btn_frame,
            text="Reset",
            font=("times new roman", 12, "bold"),
            bg="gold",
            fg="black",
            width=10,
        )
        btnReset.grid(row=0, column=3, padx=1)
        #! ---------------------------Right Side Img------------------------------------
        img3 = Image.open(r"./images/room.jpg")
        img3 = img3.resize((520, 260), Image.LANCZOS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        lblImg = Label(self.root, image=self.photoImg3, bd=0, relief=RIDGE)
        lblImg.place(x=800, y=80, width=520, height=260)
        #!------------------- label frame --------------------------------
        table_frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="View Details and Search System",
            font=("times new roman", 12, "bold"),
            padx=2,
        )
        table_frame.place(x=435, y=280, width=1000, height=280)

        lbl_Searchby = Label(
            table_frame,
            text="Search By:",
            fg="red",
            font=("times new roman", 14, "bold"),
        )
        lbl_Searchby.grid(row=0, column=0, sticky=W, padx=2)
        self.search_var = StringVar()
        combo_search = ttk.Combobox(
            table_frame,
            textvariable=self.search_var,
            font=("arial", 12, "bold"),
            width=24,
            state="readonly",
        )
        combo_search["value"] = ("Contact", "Room")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.text_search = StringVar()
        search_text = ttk.Entry(
            table_frame,
            textvariable=self.text_search,
            width=24,
            font=("times new roman", 13, "bold"),
        )
        search_text.grid(row=0, column=2, padx=2)
        btnSearch = Button(
            table_frame,
            text="Search",
            font=("times new roman", 12, "bold"),
            bg="gold",
            fg="black",
            width=10,
        )
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(
            table_frame,
            text="Show All",
            font=("times new roman", 12, "bold"),
            bg="gold",
            fg="black",
            width=10,
        )
        btnShowAll.grid(row=0, column=4, padx=1)
        #! ---------------------SHOW DATA TABLE------------------------------------------------
        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=990, height=250)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cus_Details_Table = ttk.Treeview(
            details_table,
            column=(
                "contact",
                "checkInDate",
                "CheckOutDate",
                "RoomType",
                "RoomAvailability",
                "Meal",
                "NoOFdays",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cus_Details_Table.xview)
        scroll_y.config(command=self.Cus_Details_Table.yview)

        self.Cus_Details_Table.heading("contact", text="Contact")
        self.Cus_Details_Table.heading("checkInDate", text="CheckInDate")
        self.Cus_Details_Table.heading("CheckOutDate", text="CheckOutDate")
        self.Cus_Details_Table.heading("RoomType", text="RoomType")
        self.Cus_Details_Table.heading("RoomAvailability", text="Room Avaliable")
        self.Cus_Details_Table.heading("Meal", text="Meal")
        self.Cus_Details_Table.heading("NoOFdays", text="NoOFdays")

        self.Cus_Details_Table["show"] = "headings"

        self.Cus_Details_Table.column("contact", width=100)
        self.Cus_Details_Table.column("checkInDate", width=100)
        self.Cus_Details_Table.column("CheckOutDate", width=100)
        self.Cus_Details_Table.column("RoomType", width=100)
        self.Cus_Details_Table.column("RoomAvailability", width=100)
        self.Cus_Details_Table.column("Meal", width=100)
        self.Cus_Details_Table.column("NoOFdays", width=100)

        self.Cus_Details_Table.pack(fill=BOTH, expand=1)

    def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror(
                "Error", "Please enter a contact Number", parent=self.root
            )
        else:
            con = mysql.connector.connect(
                host="localhost",
                username="root",
                password="ASDfgh2580.",
                database="hotelManagament",
            )
            my_cursor = con.cursor()
            query = "SELECT NAME FROM customer WHERE Mobile=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "This number Not Found", parent=self.root)
            else:
                con.commit()
                con.close()

                showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame.place(x=455, y=68, width=300, height=180)

                lblName = Label(showDataFrame, text="Name:", font=("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                con = mysql.connector.connect(
                host="localhost",
                username="root",
                password="ASDfgh2580.",
                database="hotelManagament",
            )
                my_cursor = con.cursor()
                query = "SELECT GENDER FROM customer WHERE Mobile=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()


                lblGender = Label(showDataFrame, text="Gender:", font=("arial", 12, "bold"))
                lblGender.place(x=0, y=30)

                lbl2 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=30)


if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()
