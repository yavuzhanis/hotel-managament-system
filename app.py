from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Window


class HotelManagamentSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Managament System")
        self.root.geometry("1700x900+0+0")
        # ! ÜST IMG
        img1 = Image.open(r"./images/hotel.png")
        img1 = img1.resize((1700, 180), Image.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        lblImg = Label(self.root, image=self.photoImg1, bd=4, relief=RIDGE)
        lblImg.place(x=0, y=0, width=1700, height=180)
        # ! LOGO
        img2 = Image.open(r"./images/logo-hotel.png")
        img2 = img2.resize((230, 180), Image.LANCZOS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        lblImg = Label(self.root, image=self.photoImg2, bd=4, relief=RIDGE)
        lblImg.place(x=0, y=0, width=230, height=180)
        #! TITLE
        lbl_title = Label(
            self.root,
            text="HOTEL MANAGAMENT SYSTEM",
            font=("times new roman", 40, "bold"),
            bg="black",
            fg="gold",
            bd=4,
            relief=RIDGE,
        )
        lbl_title.place(x=0, y=180, width=1750, height=50)
        #! main frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=220, width=1750, height=605)
        #! MENU
        lbl_menu = Label(
            main_frame,
            text="MENU",
            font=("times new roman", 20, "bold"),
            bg="black",
            fg="gold",
            bd=4,
            relief=RIDGE,
        )
        lbl_menu.place(x=0, y=0, width=230)

        #! btn frame
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=230, height=140)

        cust_btn = Button(
            btn_frame,
            text="CUSTOMER",
            command=self.cust_Details,
            width=27,
            font=("times new roman", 14, "bold"),
            bg="black",
            fg="gold",
            bd=0,
            cursor="hand1",
        )
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(
            btn_frame,
            text="ROOM",
            width=27,
            font=("times new roman", 14, "bold"),
            bg="black",
            fg="gold",
            bd=0,
            cursor="hand1",
        )
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(
            btn_frame,
            text="DETAILS",
            width=27,
            font=("times new roman", 14, "bold"),
            bg="black",
            fg="gold",
            bd=0,
            cursor="hand1",
        )
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(
            btn_frame,
            text="REPORT",
            width=27,
            font=("times new roman", 14, "bold"),
            bg="black",
            fg="gold",
            bd=0,
            cursor="hand1",
        )
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(
            btn_frame,
            text="LOGOUT",
            width=27,
            font=("times new roman", 14, "bold"),
            bg="black",
            fg="gold",
            bd=0,
            cursor="hand1",
        )
        logout_btn.grid(row=4, column=0, pady=1)

        #! right side img
        img3 = Image.open(r"./images/reception.jpg")
        img3 = img3.resize((1700, 590), Image.LANCZOS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        lblImg1 = Label(main_frame, image=self.photoImg3, bd=4, relief=RIDGE)
        lblImg1.place(x=225, y=0, width=1700, height=600)
        #! down image
        img4 = Image.open(r"./images/eat-hotel.png")
        img4 = img4.resize((230, 250), Image.LANCZOS)
        self.photoImg4 = ImageTk.PhotoImage(img4)
        lblImg2 = Label(main_frame, image=self.photoImg4, bd=4, relief=RIDGE)
        lblImg2.place(x=0, y=180, width=230, height=250)

        img5 = Image.open(r"./images/hotel-small.jpeg")
        img5 = img5.resize((230, 210), Image.LANCZOS)
        self.photoImg5 = ImageTk.PhotoImage(img5)
        lblImg3 = Label(main_frame, image=self.photoImg5, bd=4, relief=RIDGE)
        lblImg3.place(x=0, y=400, width=230, height=210)

    def cust_Details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Window(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagamentSystem(root)
    root.mainloop()
