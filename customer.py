from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk


class Cust_Window:
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
            text="ADD CUSTOMER DETAILS",
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
            text="Customer Details",
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
            font=("times new roman", 13, "bold"),
        )
        enty_ref.grid(row=0, column=1)

        #! cust name
        cname = Label(
            LabelFrameleft,
            text="Customer Name:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        cname.grid(row=1, column=0, sticky=W)

        txtcname = ttk.Entry(
            LabelFrameleft,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        txtcname.grid(row=1, column=1)

        #! mother name
        motherName = Label(
            LabelFrameleft,
            text="Mother Name:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        motherName.grid(row=2, column=0, sticky=W)

        motherNameRef = ttk.Entry(
            LabelFrameleft,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        motherNameRef.grid(row=2, column=1)

        #! gender combobox
        lbl_gender = Label(
            LabelFrameleft,
            text=" Gender:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(
            LabelFrameleft,
            font=("arial", 12, "bold"),
            width=27,
            state="readonly",
        )
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        #! postcode
        lbl_postcode = Label(
            LabelFrameleft,
            text="Postcode:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_postcode.grid(row=4, column=0, sticky=W)

        enty_postcode = ttk.Entry(
            LabelFrameleft,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        enty_postcode.grid(row=4, column=1)

        # ? mobile number
        lbl_mnumber = Label(
            LabelFrameleft,
            text="Mobile Number:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_mnumber.grid(row=5, column=0, sticky=W)

        txtmobile = ttk.Entry(
            LabelFrameleft,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        txtmobile.grid(row=5, column=1)

        # ? email
        lbl_email = Label(
            LabelFrameleft,
            text="Email:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_email.grid(row=6, column=0, sticky=W)

        email_text = ttk.Entry(
            LabelFrameleft,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        email_text.grid(row=6, column=1)

        # ? nationality
        lbl_nationality = Label(
            LabelFrameleft,
            text="Nationality:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_nationality.grid(row=7, column=0, sticky=W)
        combo_nationality = ttk.Combobox(
            LabelFrameleft,
            font=("arial", 12, "bold"),
            width=27,
            state="readonly",
        )
        combo_nationality["value"] = (
            "Türk",
            "Alman",
            "Fransız",
            "İtalyan",
            "Japon",
            "Kanadalı",
            "Brezilyalı",
            "Hindistanlı",
            "Mısırlı",
        )
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        # TODO id proof type combo box
        lbl_idproof = Label(
            LabelFrameleft,
            text="Id Proof Type:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_idproof.grid(row=8, column=0, sticky=W)

        combo_idproof = ttk.Combobox(
            LabelFrameleft,
            font=("arial", 12, "bold"),
            width=27,
            state="readonly",
        )
        combo_idproof["value"] = ("AdharCard", "DrivingLicience", "Passport", "Other")
        combo_idproof.current(0)
        combo_idproof.grid(row=8, column=1)

        # ? id number
        lbl_id = Label(
            LabelFrameleft,
            text="Id Number:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_id.grid(row=9, column=0, sticky=W)

        id_text = ttk.Entry(
            LabelFrameleft,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        id_text.grid(row=9, column=1)

        # ? address
        lbl_address = Label(
            LabelFrameleft,
            text="Address:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_address.grid(row=10, column=0, sticky=W)

        address_text = ttk.Entry(
            LabelFrameleft,
            width=26,
            font=("times new roman", 13, "bold"),
        )
        address_text.grid(row=10, column=1)

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
        btnAdd.grid(row=0, column=0, padx=1)

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

        #! label frame
        table_frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="View Details and Search System",
            font=("times new roman", 12, "bold"),
            padx=2,
        )
        table_frame.place(x=435, y=60, width=1000, height=490)

        lbl_Searchby = Label(
            table_frame,
            text="Search By:",
            fg="red",
            font=("times new roman", 14, "bold"),
        )
        lbl_Searchby.grid(row=0, column=0, sticky=W, padx=2)

        combo_search = ttk.Combobox(
            table_frame,
            font=("arial", 12, "bold"),
            width=24,
            state="readonly",
        )
        combo_search["value"] = ("Mobile", "Ref")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        search_text = ttk.Entry(
            table_frame,
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

        #! SHOW DATA TABLE
        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=990, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cus_Details_Table = ttk.Treeview(
            details_table,
            column=(
                "ref",
                "name",
                "mother",
                "gender",
                "post",
                "mobile",
                "email",
                "nationality",
                "idproof",
                "idnumber",
                "address",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cus_Details_Table.xview)
        scroll_y.config(command=self.Cus_Details_Table.yview)

        self.Cus_Details_Table.heading("ref", text="Reference No")
        self.Cus_Details_Table.heading("name", text="Name")
        self.Cus_Details_Table.heading("mother", text="Mother Name")
        self.Cus_Details_Table.heading("gender", text="Gender")
        self.Cus_Details_Table.heading("post", text="PostCode")
        self.Cus_Details_Table.heading("mobile", text="Mobile No")
        self.Cus_Details_Table.heading("email", text="E-Mail")
        self.Cus_Details_Table.heading("nationality", text="Nationality")
        self.Cus_Details_Table.heading("idproof", text="Id Proof.")
        self.Cus_Details_Table.heading("idnumber", text="Id Number")
        self.Cus_Details_Table.heading("address", text="Adress")

        self.Cus_Details_Table["show"] = "headings"

        self.Cus_Details_Table.column("ref", width=100)
        self.Cus_Details_Table.column("name", width=100)
        self.Cus_Details_Table.column("mother", width=100)
        self.Cus_Details_Table.column("gender", width=100)
        self.Cus_Details_Table.column("post", width=100)
        self.Cus_Details_Table.column("mobile", width=100)
        self.Cus_Details_Table.column("email", width=100)
        self.Cus_Details_Table.column("nationality", width=100)
        self.Cus_Details_Table.column("idproof", width=100)
        self.Cus_Details_Table.column("idnumber", width=100)
        self.Cus_Details_Table.column("address", width=100)

        self.Cus_Details_Table.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Window(root)
    root.mainloop()
