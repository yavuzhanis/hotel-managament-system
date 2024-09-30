from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime, strptime
from datetime import datetime

import mysql.connector
from tkinter import messagebox


class DetailsRoom:
    def __init__(self, root):

        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1460x570+240+294")
        # ?  ------------------variables------------------

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
            text="New Rooms Add",
            font=("times new roman", 14, "bold"),
            padx=2,
        )
        LabelFrameleft.place(x=5, y=60, width=525, height=390)

        #! LABELS AND ENTRİES
        #!FLOOr
        lbl_floor = Label(
            LabelFrameleft,
            text="Floor:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_floor.grid(row=0, column=0, sticky=W)

        self.var_floor = StringVar()
        enty_floor = ttk.Entry(
            LabelFrameleft,
            textvariable=self.var_floor,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        enty_floor.grid(row=0, column=1, sticky=W)

        #! room no
        lbl_RoomNo = Label(
            LabelFrameleft,
            text="Room No:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_RoomNo.grid(row=1, column=0, sticky=W)
        self.var_RoomNo = StringVar()
        enty_RoomNo = ttk.Entry(
            LabelFrameleft,
            textvariable=self.var_RoomNo,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        enty_RoomNo.grid(row=1, column=1, sticky=W)
        #! room type
        lbl_RoomType = Label(
            LabelFrameleft,
            text="Room Type:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_RoomType.grid(row=2, column=0, sticky=W)
        self.var_roomType = StringVar()
        enty_RoomType = ttk.Entry(
            LabelFrameleft,
            textvariable=self.var_roomType,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        enty_RoomType.grid(row=2, column=1, sticky=W)

        #! buttons
        btn_frame = Frame(LabelFrameleft, bd=2, relief=RIDGE)
        btn_frame.place(x=20, y=200, width=400, height=40)

        btnAdd = Button(
            btn_frame,
            text="Add",
            font=("times new roman", 12, "bold"),
            bg="gold",
            command=self.add_data,
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
            fg="black",
            width=10,
        )
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(
            btn_frame,
            text="Reset",
            font=("times new roman", 12, "bold"),
            fg="black",
            width=10,
        )
        btnReset.grid(row=0, column=3, padx=1)

        # table frame
        table_frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Show Room Details",
            font=("times new roman", 12, "bold"),
            padx=2,
        )
        table_frame.place(x=555, y=75, width=800, height=380)

        # Scrollbar'ları önce tanımlıyoruz
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Sonra pack ediyoruz
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Oda tablosunu da doğru şekilde tanımlayın
        self.room_table = ttk.Treeview(
            table_frame,
            columns=("floor", "roomNo", "roomType"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomNo", text="Room No")
        self.room_table.heading("roomType", text="Room Type")

        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomNo", width=100)
        self.room_table.column("roomType", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursors)
        self.fetch_data()

    #! add data
    def add_data(self):
        if self.var_floor.get() == "" or self.var_roomType.get() == "":
            messagebox.showerror(
                "Error", "All fields are required!,please.", parent=self.root
            )
        else:
            try:
                con = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="ASDfgh2580.",
                    database="hotelManagament",
                )
                my_cursor = con.cursor()
                my_cursor.execute(
                    "insert into details values(%s,%s,%s)",
                    (
                        self.var_floor.get(),
                        self.var_RoomNo.get(),
                        self.var_roomType.get(),
                    ),
                )
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo(
                    "Success", "Room ADDED successfully!", parent=self.root
                )
            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Something went wrong!:{str(es)}", parent=self.root
                )

    #! fetch data
    def fetch_data(self):
        con = mysql.connector.connect(
            host="localhost",
            username="root",
            password="ASDfgh2580.",
            database="hotelManagament",
        )
        my_cursor = con.cursor()
        my_cursor.execute("select * from details")  #! db changed
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            con.commit()
        con.close()

    def get_cursors(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        print("Row values:", row)  # Bu satır row değerlerini yazdıracak

        if row:  # Eğer row boş değilse
            self.var_floor.set(row[0])
            self.var_RoomNo.set(row[1])
            self.var_roomType.set(row[2])
        else:
            print("No data found.")

    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror(
                "Error", "Please enter the Room Number", parent=self.root
            )
        else:
            try:
                con = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="ASDfgh2580.",
                    database="hotelManagament",
                )
                my_cursor = con.cursor()
                my_cursor.execute(
                    """
                    UPDATE details 
                    SET floor=%s, RoomType=%s, 
                    WHERE RoomNo=%s
                    """,
                    (
                        self.var_floor.get(),
                        self.var_roomType.get(),
                        self.var_RoomNo.get(),
                    ),
                )
                con.commit()
                self.fetch_data()

                con.close()
                messagebox.showinfo(
                    "Update",
                    "Room Details have been updated successfully",
                    parent=self.root,
                )
            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Something went wrong: {str(es)}", parent=self.root
                )


if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()
