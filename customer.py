from tkinter import *


class Cust_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Managament System")
        self.root.geometry("1460x570+240+294")


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Window(root)
    root.mainloop()
