from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
import datetime as dt
from finance_database import update_investments
from home_page import home


def investments_log():
    root = Tk()
    root.title("investments")
    main_frame = ttk.Frame(root, padding=10, width=950, height=350)
    main_frame.grid(row=0, column=0)

    # ================ STYLING ====================================== #
    column_font = Font(family="Helvetica", weight="bold", size=8)
    category_color = "AliceBlue"

    # ================= FUNCTIONS ==================================== #
    def investments_add(amount):
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

                update_investments(current_day, deposit_amount, withdrawal_amount)

        investments_entry.delete(0, END)

    def investments_remove(amount):
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

                update_investments(current_day, deposit_amount, withdrawal_amount)

        investments_entry.delete(0, END)

    def return_main():
        """Return user to main page"""
        root.destroy()
        home()

    def exit_fxn():
        """Return user to login page"""
        root.destroy()
        from main import main_page
        main_page()

    # =============== FRAMES ============================ #
    s = ttk.Style()
    s.configure('Section.TFrame', background=category_color, borderwidth=5, relief="solid")

    investments_frame = ttk.Frame(main_frame, style="Section.TFrame")
    investments_frame.grid(row=0, column=0, padx=5, pady=5)

    # ============= investments ================================= #
    investments_lbl = ttk.Label(investments_frame, text="Amount", font=column_font)
    investments_lbl.grid(row=0, column=0, padx=5, pady=5)

    investments_entry = IntVar()
    investments_entry = ttk.Entry(investments_frame, textvariable=investments_entry, width=10)
    investments_entry.grid(row=0, column=1, padx=5, pady=5)

    investments_add_btn = ttk.Button(investments_frame, text="Deposit", command=lambda: investments_add(investments_entry.get()))
    investments_add_btn.grid(row=0, column=2, pady=5, padx=5)

    investments_remove_btn = ttk.Button(investments_frame, text="Withdraw", command=lambda: investments_remove(investments_entry.get()))
    investments_remove_btn.grid(row=0, column=3, pady=5, padx=5)

    return_main_btn = ttk.Button(main_frame, text="Return to main page", command=return_main)
    return_main_btn.grid(row=1, column=0, padx=5, pady=5)

    exit_fxn_btn = ttk.Button(main_frame, text="Exit", command=exit_fxn)
    exit_fxn_btn.grid(row=2, column=0)

    root.mainloop()