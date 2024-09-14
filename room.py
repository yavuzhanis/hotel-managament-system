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
        lbl_cust_ref = Label(
            LabelFrameleft,
            text="Customer Ref:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        enty_ref = ttk.Entry(
            LabelFrameleft,
            width=26,
            textvariable=self.var_ref,
            font=("times new roman", 13, "bold"),
            state="readonly",
        )
        enty_ref.grid(row=0, column=1)


if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()
