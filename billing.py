from tkinter import *
import random
import os
from tkinter import messagebox
from datetime import datetime


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")

        # Variables for product quantities
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_Gloves = IntVar()
        self.dettol = IntVar()
        self.newsprin = IntVar()
        self.thermal_gun = IntVar()
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.daal = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()
        self.sprite = IntVar()
        self.swing = IntVar()
        self.fanta = IntVar()
        self.mazza = IntVar()

        # Customer and billing info
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        self.c_date = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.c_date.set(datetime.now().strftime("%d-%m-%Y"))

        # Product dictionary
        self.products = {
            "Sanitizer": [self.sanitizer, 50],
            "Mask": [self.mask, 10],
            "Hand Gloves": [self.hand_Gloves, 30],
            "Dettol": [self.dettol, 80],
            "Newsprin": [self.newsprin, 25],
            "Thermal Gun": [self.thermal_gun, 500],
            "Rice": [self.rice, 60],
            "Food Oil": [self.food_oil, 120],
            "Wheat": [self.wheat, 40],
            "Daal": [self.daal, 70],
            "Flour": [self.flour, 30],
            "Maggi": [self.maggi, 15],
            "Sprite": [self.sprite, 40],
            "Swing": [self.swing, 35],
            "Fanta": [self.fanta, 45],
            "Mazza": [self.mazza, 38]
        }

        # Title
        title = Label(self.root, text="Billing Software", font=('times new roman', 30, 'bold'), pady=2, bd=12,
                      bg="#badc57", fg="Black", relief=GROOVE)
        title.pack(fill=X)

        # Customer Details Frame
        F2 = LabelFrame(self.root, text="Customer Details", font=("times new roman", 12, "bold"), bd=10, relief=GROOVE)
        F2.place(x=0, y=80, relwidth=1)

        Label(F2, text="Customer Name", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=20, pady=5)
        Entry(F2, textvariable=self.c_name, font="arial 12", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        Label(F2, text="Phone No.", font=("times new roman", 12, "bold")).grid(row=0, column=2, padx=20, pady=5)
        Entry(F2, textvariable=self.c_phone, font="arial 12", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        Label(F2, text="Bill Number", font=("times new roman", 12, "bold")).grid(row=0, column=4, padx=20, pady=5)
        Entry(F2, textvariable=self.bill_no, font="arial 12", bd=7, relief=SUNKEN, state='readonly').grid(row=0, column=5, pady=5, padx=10)

        Label(F2, text="Date", font=("times new roman", 12, "bold")).grid(row=0, column=6, padx=20, pady=5)
        Entry(F2, textvariable=self.c_date, font="arial 12", bd=7, relief=SUNKEN, state='readonly').grid(row=0, column=7, pady=5, padx=10)

        # Product Menu Frame
        F1 = LabelFrame(self.root, text="Product Menu", font=("times new roman", 12, "bold"), bd=10, relief=GROOVE)
        F1.place(x=0, y=180, width=690, height=500)

        row = 0
        for item, (var, price) in self.products.items():
            Label(F1, text=f"{item} (₹{price})", font=("times new roman", 12, "bold")).grid(row=row, column=0, padx=10,
                                                                                            pady=5, sticky="w")
            Entry(F1, textvariable=var, width=10, font="arial 12", bd=5, relief=SUNKEN).grid(row=row, column=1, padx=10,
                                                                                             pady=5)
            row += 1

        # Bill Area Frame
        F3 = Frame(self.root, bd=10, relief=GROOVE)
        F3.place(x=700, y=180, width=580, height=500)

        Label(F3, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.txtarea = Text(F3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # Button Frame
        btn_frame = Frame(self.root, bd=7, relief=GROOVE)
        btn_frame.place(x=0, y=680, relwidth=1, height=50)
        Button(btn_frame, text="Total", command=self.total, width=15, font="arial 12 bold").pack(side=LEFT, padx=10)
        Button(btn_frame, text="Generate Bill", command=self.generate_bill, width=15, font="arial 12 bold").pack(
            side=LEFT, padx=10)
        Button(btn_frame, text="Save Bill", command=self.save_bill, width=15, font="arial 12 bold").pack(side=LEFT,
                                                                                                         padx=10)

    def total(self):
        self.total_price = 0
        self.bill_text = ""
        for item, (var, price) in self.products.items():
            qty = var.get()
            if qty > 0:
                item_total = qty * price
                self.total_price += item_total
                self.bill_text += f"{item:<20} x{qty:<3} ₹{item_total:.2f}\n"
        self.bill_text += f"\n{'-' * 40}\nTotal Amount: ₹{self.total_price:.2f}"

    def generate_bill(self):
        if not self.c_name.get().strip() or not self.c_phone.get().strip():
            messagebox.showerror("Error", "Customer details are required")
            return

        self.total()  # Calculate totals and build bill_text

        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to Vishwajeet Store\n")
        self.txtarea.insert(END, f"Bill No   : {self.bill_no.get()}\n")
        self.txtarea.insert(END, f"Customer  : {self.c_name.get()}\n")
        self.txtarea.insert(END, f"Phone     : {self.c_phone.get()}\n")
        self.txtarea.insert(END, f"Date      : {self.c_date.get()}\n")
        self.txtarea.insert(END, "-" * 40 + "\n")
        self.txtarea.insert(END, f"{'Product':<20}{'Qty':<10}{'Price'}\n")
        self.txtarea.insert(END, "-" * 40 + "\n")
        self.txtarea.insert(END, self.bill_text)

    def save_bill(self):
        bill_data = self.txtarea.get('1.0', END)


        save_dir = "bills"
        os.makedirs(save_dir, exist_ok=True)

        safe_cust_name = "".join(c for c in self.c_name.get() if c.isalnum())

        filename = f"Bill_{self.bill_no.get()}_{safe_cust_name}.txt"
        file_path = os.path.join(save_dir, filename)

        try:
            with open(file_path, "w") as f:
                f.write(bill_data)
            messagebox.showinfo("Saved", f"Bill saved as:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save bill:\n{e}")


if __name__ == "__main__":
    root = Tk()
    app = Bill_App(root)
    root.mainloop()
