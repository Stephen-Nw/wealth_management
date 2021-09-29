from tkinter import *
from tkinter import ttk
from tkinter.font import Font

app_name = "Expenses"

root = Tk()
root.title("Interprimos Wealth Management Solution")
main_frame = ttk.Frame(root, padding=10, width=930, height=330)
main_frame.grid(row=0, column=0)

# ================ FONTS ====================================== #
section_font = Font(family="Helvetica", weight="bold", slant="italic", size=10)
column_font = Font(family="Helvetica", weight="bold", size=8)


# =============== FUNCTIONS ========================= #
def mortgage():
    pass


def water():
    pass


def auto_gas():
    pass


# =============== FRAMES ============================ #
housing_frame = ttk.Frame(main_frame)
housing_frame.grid(row=0, column=0, padx=10, pady=10)

utilities_frame = ttk.Frame(main_frame)
utilities_frame.grid(row=0, column=1, padx=10, pady=10)

auto_frame = ttk.Frame(main_frame)
auto_frame.grid(row=0, column=2, padx=10, pady=10)

# ================ EXPENSES CATEGORIES================= #
# **************** Housing***************************** #
housing_header = ttk.Label(housing_frame, text="Housing", font=section_font, justify="center")
housing_header.grid(row=0, column=0, columnspan=3)

housing_item = ttk.Label(housing_frame, text="Item", font=column_font)
housing_item.grid(row=1, column=0, padx=3)

housing_amount = ttk.Label(housing_frame, text="Amount", font=column_font)
housing_amount.grid(row=1, column=1, padx=3)

mortgage_lbl = ttk.Label(housing_frame, text="Mortgage/Rent")
mortgage_lbl.grid(row=2, column=0, padx=3, pady=3)

mortgage_entry = IntVar()
mortgage_entry = ttk.Entry(housing_frame, textvariable=mortgage_entry, width=10)
mortgage_entry.grid(row=2, column=1, padx=3, pady=3)

mortgage_btn = ttk.Button(housing_frame, text="Submit", command=mortgage)
mortgage_btn.grid(row=2, column=2, pady=3, padx=3)

# **************** Utilities ***************************** #
utilities_header = ttk.Label(utilities_frame, text="Utilities", font=section_font, justify="center")
utilities_header.grid(row=0, column=0, columnspan=3)

utilities_item = ttk.Label(utilities_frame, text="Item", font=column_font)
utilities_item.grid(row=1, column=0, padx=3)

utilities_amount = ttk.Label(utilities_frame, text="Amount", font=column_font)
utilities_amount.grid(row=1, column=1, padx=3)

water_lbl = ttk.Label(utilities_frame, text="Water")
water_lbl.grid(row=2, column=0, padx=3, pady=3)

water_entry = IntVar()
water_entry = ttk.Entry(utilities_frame, textvariable=water_entry, width=10)
water_entry.grid(row=2, column=1, padx=3, pady=3)

water_btn = ttk.Button(utilities_frame, text="Submit", command=water)
water_btn.grid(row=2, column=2, pady=3, padx=3)

# ***************** Automobiles ***************************** #
auto_header = ttk.Label(auto_frame, text="Automobile", font=section_font, justify="center")
auto_header.grid(row=0, column=0, columnspan=3)

auto_item = ttk.Label(auto_frame, text="Item", font=column_font)
auto_item.grid(row=1, column=0, padx=3)

auto_amount = ttk.Label(auto_frame, text="Amount", font=column_font)
auto_amount.grid(row=1, column=1, padx=3)

auto_gas_lbl = ttk.Label(auto_frame, text="Gas")
auto_gas_lbl.grid(row=2, column=0, padx=3, pady=3)

auto_gas_entry = IntVar()
auto_gas_entry = ttk.Entry(auto_frame, textvariable=auto_gas_entry, width=10)
auto_gas_entry.grid(row=2, column=1, padx=3, pady=3)

auto_gas_btn = ttk.Button(auto_frame, text="Submit", command=auto_gas)
auto_gas_btn.grid(row=2, column=2, pady=3, padx=3)

root.mainloop()
