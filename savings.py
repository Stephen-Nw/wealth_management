from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
import datetime as dt
from finance_database import update_savings
from home_page import home

root = Tk()
root.title("Savings")
main_frame = ttk.Frame(root, padding=10, width=950, height=350)
main_frame.grid(row=0, column=0)

# ================ STYLING ====================================== #
# section_font = Font(family="Helvetica", weight="bold", slant="italic", size=10)
column_font = Font(family="Helvetica", weight="bold", size=8)
# heading_color = "green1"
category_color = "AliceBlue"


# ================= FUNCTIONS ==================================== #
def savings_add(amount):
    try:
        deposit_amount = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if deposit_amount < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")
            withdrawal_amount = ""

            update_savings(current_day, deposit_amount, withdrawal_amount)

    savings_entry.delete(0, END)


def savings_remove(amount):
    try:
        withdrawal_amount = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if withdrawal_amount < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")
            deposit_amount = ""

            update_savings(current_day, deposit_amount, withdrawal_amount)

    savings_entry.delete(0, END)


def return_main():
    pass


def exit_fxn():
    pass


# =============== FRAMES ============================ #
s = ttk.Style()
s.configure('Section.TFrame', background=category_color, borderwidth=5, relief="solid")

savings_frame = ttk.Frame(main_frame, style="Section.TFrame")
savings_frame.grid(row=0, column=0, padx=5, pady=5)

# ============= Savings ================================= #
savings_lbl = ttk.Label(savings_frame, text="Amount", font=column_font)
savings_lbl.grid(row=0, column=0, padx=5, pady=5)

savings_entry = IntVar()
savings_entry = ttk.Entry(savings_frame, textvariable=savings_entry, width=10)
savings_entry.grid(row=0, column=1, padx=5, pady=5)

savings_add_btn = ttk.Button(savings_frame, text="Deposit", command=lambda: savings_add(savings_entry.get()))
savings_add_btn.grid(row=0, column=2, pady=5, padx=5)

savings_remove_btn = ttk.Button(savings_frame, text="Withdraw", command=lambda: savings_remove(savings_entry.get()))
savings_remove_btn.grid(row=0, column=3, pady=5, padx=5)

# return_main_btn = ttk.Button(main_frame, text="Return to main page", command=return_main)
# return_main_btn.grid(row=1, column=0, padx=5, pady=5)
#
# exit_fxn_btn = ttk.Button(main_frame, text="Exit", command=exit_fxn)
# exit_fxn_btn.grid(row=2, column=0)

root.mainloop()
