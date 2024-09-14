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
            font=("times new roman", 13, "bold"),
            state="readonly",
        )
        enty_contact.grid(row=0, column=1)
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

        lblMeal_text = ttk.Entry(
            LabelFrameleft,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        lblMeal_text.grid(row=6, column=1)

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
            width=26,
            font=("times new roman", 13, "bold"),
        )
        lblSubTotal_text.grid(row=8, column=1)

        # ? total cost
        lblIdNumber = Label(
            LabelFrameleft,
            font=("times new roman", 13, "bold"),
            text=" Total Cost:",
            padx=2,
            pady=6,
        )
        lblIdNumber.grid(row=9, column=0, sticky=W)

        lblIdNumber_text = ttk.Entry(
            LabelFrameleft,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        lblIdNumber_text.grid(row=9, column=1)


if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()
