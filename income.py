from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
import datetime as dt
from home_page import home

root = Tk()
root.title("Income")
main_frame = ttk.Frame(root, padding=10, width=950, height=350)
main_frame.grid(row=0, column=0)

# ================ STYLING ====================================== #
section_font = Font(family="Helvetica", weight="bold", slant="italic", size=10)
column_font = Font(family="Helvetica", weight="bold", size=8)
heading_color = "green1"
category_color = "AliceBlue"


# ================= FUNCTIONS ==================================== #
def pri_income(category, amount):
    pass


def sec_income(category, amount):
    pass


def spouse_income(category, amount):
    pass


def additional_income(category, amount):
    pass


def misc_income(category, amount):
    pass

def return_main():
    pass

def exit_fxn():
    pass


# =============== FRAMES ============================ #
s = ttk.Style()
s.configure('Section.TFrame', background=category_color, borderwidth=5, relief="solid")

income_frame = ttk.Frame(main_frame, style="Section.TFrame")
income_frame.grid(row=0, column=0, padx=5, pady=5)

# ============= Income ================================= #
income_item = ttk.Label(income_frame, text="Category", font=column_font)
income_item.grid(row=1, column=0, padx=3, pady=5)

income_amount = ttk.Label(income_frame, text="Amount", font=column_font)
income_amount.grid(row=1, column=1, padx=3)

pri_income_lbl = ttk.Label(income_frame, text="Primary income")
pri_income_lbl.grid(row=3, column=0, padx=3, pady=3)

pri_income_entry = IntVar()
pri_income_entry = ttk.Entry(income_frame, textvariable=pri_income_entry, width=10)
pri_income_entry.grid(row=3, column=1, padx=3, pady=3)

pri_income_btn = ttk.Button(income_frame, text="Submit", command=lambda: pri_income(pri_income_lbl["text"],
                                                                                    pri_income_entry.get()))
pri_income_btn.grid(row=3, column=2, pady=3, padx=3)

sec_income_lbl = ttk.Label(income_frame, text="Secondary income")
sec_income_lbl.grid(row=4, column=0, padx=3, pady=3)

sec_income_entry = IntVar()
sec_income_entry = ttk.Entry(income_frame, textvariable=sec_income_entry, width=10)
sec_income_entry.grid(row=4, column=1, padx=3, pady=3)

sec_income_btn = ttk.Button(income_frame, text="Submit", command=lambda: sec_income(sec_income_lbl["text"],
                                                                                    sec_income_entry.get()))
sec_income_btn.grid(row=4, column=2, pady=3, padx=3)

spouse_income_lbl = ttk.Label(income_frame, text="Spouse income")
spouse_income_lbl.grid(row=5, column=0, padx=3, pady=3)

spouse_income_entry = IntVar()
spouse_income_entry = ttk.Entry(income_frame, textvariable=spouse_income_entry, width=10)
spouse_income_entry.grid(row=5, column=1, padx=3, pady=3)

spouse_income_btn = ttk.Button(income_frame, text="Submit", command=lambda: spouse_income(spouse_income_lbl["text"],
                                                                                          spouse_income_entry.get()))
spouse_income_btn.grid(row=5, column=2, pady=3, padx=3)

additional_income_lbl = ttk.Label(income_frame, text="Additional income")
additional_income_lbl.grid(row=6, column=0, padx=3, pady=3)

additional_income_entry = IntVar()
additional_income_entry = ttk.Entry(income_frame, textvariable=additional_income_entry, width=10)
additional_income_entry.grid(row=6, column=1, padx=3, pady=3)

additional_income_btn = ttk.Button(income_frame, text="Submit",
                                   command=lambda: additional_income(additional_income_lbl["text"],
                                                                     additional_income_entry.get()))
additional_income_btn.grid(row=6, column=2, pady=3, padx=3)

misc_income_lbl = ttk.Label(income_frame, text="Miscellaneous")
misc_income_lbl.grid(row=7, column=0, padx=3, pady=3)

misc_income_entry = IntVar()
misc_income_entry = ttk.Entry(income_frame, textvariable=misc_income_entry, width=10)
misc_income_entry.grid(row=7, column=1, padx=3, pady=3)

misc_income_btn = ttk.Button(income_frame, text="Submit",
                             command=lambda: misc_income(misc_income_lbl["text"],
                                                         misc_income_entry.get()))
misc_income_btn.grid(row=7, column=2, pady=3, padx=3)

return_main_btn = ttk.Button(main_frame, text="Return to main page", command=return_main)
return_main_btn.grid(row=1, column=0, padx=5, pady=5)

exit_fxn_btn = ttk.Button(main_frame, text="Exit", command=exit_fxn)
exit_fxn_btn.grid(row=2, column=0)

root.mainloop()
