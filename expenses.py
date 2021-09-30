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


def supplies():
    pass


def storage():
    pass


def house_misc():
    pass


def insurance():
    pass


def gas():
    pass


def light():
    pass


def internet():
    pass


def phone():
    pass


def auto_ins():
    pass


def auto_maint():
    pass


def groceries():
    pass


def eatout():
    pass


def snacks():
    pass


def copay():
    pass


def meds():
    pass


def gym():
    pass


def streaming():
    pass


def events():
    pass


def subscriptions():
    pass


def ent_misc():
    pass


# =============== FRAMES ============================ #
housing_frame = ttk.Frame(main_frame)
housing_frame.grid(row=0, column=0, padx=10, pady=10)

utilities_frame = ttk.Frame(main_frame)
utilities_frame.grid(row=0, column=1, padx=10, pady=10)

auto_frame = ttk.Frame(main_frame)
auto_frame.grid(row=0, column=2, padx=10, pady=10)

food_frame = ttk.Frame(main_frame)
food_frame.grid(row=0, column=3, padx=10, pady=10)

health_frame = ttk.Frame(main_frame)
health_frame.grid(row=1, column=0, padx=10, pady=10)

entertainment_frame = ttk.Frame(main_frame)
entertainment_frame.grid(row=1, column=1, padx=10, pady=10)

# ================ EXPENSES CATEGORIES ================  #
# **************** Housing ***************************** #
housing_header = ttk.Label(housing_frame, text="Housing", font=section_font, justify="center")
housing_header.grid(row=0, column=0, columnspan=3)

housing_item = ttk.Label(housing_frame, text="Item", font=column_font)
housing_item.grid(row=1, column=0, padx=3)

housing_amount = ttk.Label(housing_frame, text="Amount", font=column_font)
housing_amount.grid(row=1, column=1, padx=3)
# ------------------------------------------------------------------------ #
mortgage_lbl = ttk.Label(housing_frame, text="Mortgage/Rent")
mortgage_lbl.grid(row=2, column=0, padx=3, pady=3)

mortgage_entry = IntVar()
mortgage_entry = ttk.Entry(housing_frame, textvariable=mortgage_entry, width=10)
mortgage_entry.grid(row=2, column=1, padx=3, pady=3)

mortgage_btn = ttk.Button(housing_frame, text="Submit", command=mortgage)
mortgage_btn.grid(row=2, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------- #
supplies_lbl = ttk.Label(housing_frame, text="Supplies")
supplies_lbl.grid(row=3, column=0, padx=3, pady=3)

supplies_entry = IntVar()
supplies_entry = ttk.Entry(housing_frame, textvariable=supplies_entry, width=10)
supplies_entry.grid(row=3, column=1, padx=3, pady=3)

supplies_btn = ttk.Button(housing_frame, text="Submit", command=supplies)
supplies_btn.grid(row=3, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
storage_lbl = ttk.Label(housing_frame, text="Storage")
storage_lbl.grid(row=4, column=0, padx=3, pady=3)

storage_entry = IntVar()
storage_entry = ttk.Entry(housing_frame, textvariable=storage_entry, width=10)
storage_entry.grid(row=4, column=1, padx=3, pady=3)

storage_btn = ttk.Button(housing_frame, text="Submit", command=storage)
storage_btn.grid(row=4, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
house_misc_lbl = ttk.Label(housing_frame, text="Miscellaneous")
house_misc_lbl.grid(row=5, column=0, padx=3, pady=3)

house_misc_entry = IntVar()
house_misc_entry = ttk.Entry(housing_frame, textvariable=house_misc_entry, width=10)
house_misc_entry.grid(row=5, column=1, padx=3, pady=3)

house_misc_btn = ttk.Button(housing_frame, text="Submit", command=house_misc)
house_misc_btn.grid(row=5, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
insurance_lbl = ttk.Label(housing_frame, text="Insurance")
insurance_lbl.grid(row=6, column=0, padx=3, pady=3)

insurance_entry = IntVar()
insurance_entry = ttk.Entry(housing_frame, textvariable=insurance_entry, width=10)
insurance_entry.grid(row=6, column=1, padx=3, pady=3)

insurance_btn = ttk.Button(housing_frame, text="Submit", command=insurance)
insurance_btn.grid(row=6, column=2, pady=3, padx=3)

# **************** Utilities ***************************** #
utilities_header = ttk.Label(utilities_frame, text="Utilities", font=section_font, justify="center")
utilities_header.grid(row=0, column=0, columnspan=3)

utilities_item = ttk.Label(utilities_frame, text="Item", font=column_font)
utilities_item.grid(row=1, column=0, padx=3)

utilities_amount = ttk.Label(utilities_frame, text="Amount", font=column_font)
utilities_amount.grid(row=1, column=1, padx=3)
# ------------------------------------------------------------------------ #
water_lbl = ttk.Label(utilities_frame, text="Water")
water_lbl.grid(row=2, column=0, padx=3, pady=3)

water_entry = IntVar()
water_entry = ttk.Entry(utilities_frame, textvariable=water_entry, width=10)
water_entry.grid(row=2, column=1, padx=3, pady=3)

water_btn = ttk.Button(utilities_frame, text="Submit", command=water)
water_btn.grid(row=2, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
gas_lbl = ttk.Label(utilities_frame, text="Gas")
gas_lbl.grid(row=3, column=0, padx=3, pady=3)

gas_entry = IntVar()
gas_entry = ttk.Entry(utilities_frame, textvariable=gas_entry, width=10)
gas_entry.grid(row=3, column=1, padx=3, pady=3)

gas_btn = ttk.Button(utilities_frame, text="Submit", command=gas)
gas_btn.grid(row=3, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
light_lbl = ttk.Label(utilities_frame, text="Electricity")
light_lbl.grid(row=4, column=0, padx=3, pady=3)

light_entry = IntVar()
light_entry = ttk.Entry(utilities_frame, textvariable=light_entry, width=10)
light_entry.grid(row=4, column=1, padx=3, pady=3)

light_btn = ttk.Button(utilities_frame, text="Submit", command=light)
light_btn.grid(row=4, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
internet_lbl = ttk.Label(utilities_frame, text="Internet")
internet_lbl.grid(row=5, column=0, padx=3, pady=3)

internet_entry = IntVar()
internet_entry = ttk.Entry(utilities_frame, textvariable=internet_entry, width=10)
internet_entry.grid(row=5, column=1, padx=3, pady=3)

internet_btn = ttk.Button(utilities_frame, text="Submit", command=internet)
internet_btn.grid(row=5, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
phone_lbl = ttk.Label(utilities_frame, text="Phone")
phone_lbl.grid(row=6, column=0, padx=3, pady=3)

phone_entry = IntVar()
phone_entry = ttk.Entry(utilities_frame, textvariable=phone_entry, width=10)
phone_entry.grid(row=6, column=1, padx=3, pady=3)

phone_btn = ttk.Button(utilities_frame, text="Submit", command=phone)
phone_btn.grid(row=6, column=2, pady=3, padx=3)

# ***************** Automobiles ***************************** #
auto_header = ttk.Label(auto_frame, text="Automobile", font=section_font, justify="center")
auto_header.grid(row=0, column=0, columnspan=3)

auto_item = ttk.Label(auto_frame, text="Item", font=column_font)
auto_item.grid(row=1, column=0, padx=3)

auto_amount = ttk.Label(auto_frame, text="Amount", font=column_font)
auto_amount.grid(row=1, column=1, padx=3)
# ------------------------------------------------------------------------ #
auto_gas_lbl = ttk.Label(auto_frame, text="Gas")
auto_gas_lbl.grid(row=2, column=0, padx=3, pady=3)

auto_gas_entry = IntVar()
auto_gas_entry = ttk.Entry(auto_frame, textvariable=auto_gas_entry, width=10)
auto_gas_entry.grid(row=2, column=1, padx=3, pady=3)

auto_gas_btn = ttk.Button(auto_frame, text="Submit", command=auto_gas)
auto_gas_btn.grid(row=2, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
auto_ins_lbl = ttk.Label(auto_frame, text="Insurance")
auto_ins_lbl.grid(row=3, column=0, padx=3, pady=3)

auto_ins_entry = IntVar()
auto_ins_entry = ttk.Entry(auto_frame, textvariable=auto_ins_entry, width=10)
auto_ins_entry.grid(row=3, column=1, padx=3, pady=3)

auto_ins_btn = ttk.Button(auto_frame, text="Submit", command=auto_ins)
auto_ins_btn.grid(row=3, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
auto_maint_lbl = ttk.Label(auto_frame, text="Maintenance")
auto_maint_lbl.grid(row=4, column=0, padx=3, pady=3)

auto_maint_entry = IntVar()
auto_maint_entry = ttk.Entry(auto_frame, textvariable=auto_maint_entry, width=10)
auto_maint_entry.grid(row=4, column=1, padx=3, pady=3)

auto_maint_btn = ttk.Button(auto_frame, text="Submit", command=auto_maint)
auto_maint_btn.grid(row=4, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
auto_blank1 = ttk.Label(auto_frame, text="")
auto_blank1.grid(row=5, column=0, padx=3, pady=3)
# ------------------------------------------------------------------------ #
auto_blank2 = ttk.Label(auto_frame, text="")
auto_blank2.grid(row=6, column=0, padx=3, pady=3)

# ***************** Food ***************************** #
food_header = ttk.Label(food_frame, text="Food", font=section_font, justify="center")
food_header.grid(row=0, column=0, columnspan=3)

food_item = ttk.Label(food_frame, text="Item", font=column_font)
food_item.grid(row=1, column=0, padx=3)

food_amount = ttk.Label(food_frame, text="Amount", font=column_font)
food_amount.grid(row=1, column=1, padx=3)
# ------------------------------------------------------------------------ #
groceries_lbl = ttk.Label(food_frame, text="Groceries")
groceries_lbl.grid(row=2, column=0, padx=3, pady=3)

groceries_entry = IntVar()
groceries_entry = ttk.Entry(food_frame, textvariable=groceries_entry, width=10)
groceries_entry.grid(row=2, column=1, padx=3, pady=3)

groceries_btn = ttk.Button(food_frame, text="Submit", command=groceries)
groceries_btn.grid(row=2, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
eatout_lbl = ttk.Label(food_frame, text="Eating Out")
eatout_lbl.grid(row=3, column=0, padx=3, pady=3)

eatout_entry = IntVar()
eatout_entry = ttk.Entry(food_frame, textvariable=eatout_entry, width=10)
eatout_entry.grid(row=3, column=1, padx=3, pady=3)

eatout_btn = ttk.Button(food_frame, text="Submit", command=eatout)
eatout_btn.grid(row=3, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
snacks_lbl = ttk.Label(food_frame, text="Snacks")
snacks_lbl.grid(row=4, column=0, padx=3, pady=3)

snacks_entry = IntVar()
snacks_entry = ttk.Entry(food_frame, textvariable=snacks_entry, width=10)
snacks_entry.grid(row=4, column=1, padx=3, pady=3)

snacks_btn = ttk.Button(food_frame, text="Submit", command=snacks)
snacks_btn.grid(row=4, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
food_blank1 = ttk.Label(food_frame, text="")
food_blank1.grid(row=5, column=0, padx=3, pady=3)
# ------------------------------------------------------------------------ #
food_blank2 = ttk.Label(food_frame, text="")
food_blank2.grid(row=6, column=0, padx=3, pady=3)

# ***************** Health ***************************** #
health_header = ttk.Label(health_frame, text="Health/Fitness", font=section_font, justify="center")
health_header.grid(row=0, column=0, columnspan=3)

health_item = ttk.Label(health_frame, text="Item", font=column_font)
health_item.grid(row=1, column=0, padx=3)

health_amount = ttk.Label(health_frame, text="Amount", font=column_font)
health_amount.grid(row=1, column=1, padx=3)
# ------------------------------------------------------------------------ #
copay_lbl = ttk.Label(health_frame, text="Copay")
copay_lbl.grid(row=2, column=0, padx=3, pady=3)

copay_entry = IntVar()
copay_entry = ttk.Entry(health_frame, textvariable=copay_entry, width=10)
copay_entry.grid(row=2, column=1, padx=3, pady=3)

copay_btn = ttk.Button(health_frame, text="Submit", command=copay)
copay_btn.grid(row=2, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
meds_lbl = ttk.Label(health_frame, text="Medications")
meds_lbl.grid(row=3, column=0, padx=3, pady=3)

meds_entry = IntVar()
meds_entry = ttk.Entry(health_frame, textvariable=meds_entry, width=10)
meds_entry.grid(row=3, column=1, padx=3, pady=3)

meds_btn = ttk.Button(health_frame, text="Submit", command=meds)
meds_btn.grid(row=3, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
gym_lbl = ttk.Label(health_frame, text="Gym")
gym_lbl.grid(row=4, column=0, padx=3, pady=3)

gym_entry = IntVar()
gym_entry = ttk.Entry(health_frame, textvariable=gym_entry, width=10)
gym_entry.grid(row=4, column=1, padx=3, pady=3)

gym_btn = ttk.Button(health_frame, text="Submit", command=gym)
gym_btn.grid(row=4, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
health_blank1 = ttk.Label(health_frame, text="")
health_blank1.grid(row=5, column=0, padx=3, pady=3)
# ------------------------------------------------------------------------ #
health_blank2 = ttk.Label(health_frame, text="")
health_blank2.grid(row=6, column=0, padx=3, pady=3)

# ***************** Entertainment ***************************** #
entertainment_header = ttk.Label(entertainment_frame, text="Entertainment", font=section_font, justify="center")
entertainment_header.grid(row=0, column=0, columnspan=3)

entertainment_item = ttk.Label(entertainment_frame, text="Item", font=column_font)
entertainment_item.grid(row=1, column=0, padx=3)

entertainment_amount = ttk.Label(entertainment_frame, text="Amount", font=column_font)
entertainment_amount.grid(row=1, column=1, padx=3)
# ------------------------------------------------------------------------ #
streaming_lbl = ttk.Label(entertainment_frame, text="Streaming")
streaming_lbl.grid(row=2, column=0, padx=3, pady=3)

streaming_entry = IntVar()
streaming_entry = ttk.Entry(entertainment_frame, textvariable=streaming_entry, width=10)
streaming_entry.grid(row=2, column=1, padx=3, pady=3)

streaming_btn = ttk.Button(entertainment_frame, text="Submit", command=streaming)
streaming_btn.grid(row=2, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
events_lbl = ttk.Label(entertainment_frame, text="Events")
events_lbl.grid(row=3, column=0, padx=3, pady=3)

events_entry = IntVar()
events_entry = ttk.Entry(entertainment_frame, textvariable=events_entry, width=10)
events_entry.grid(row=3, column=1, padx=3, pady=3)

events_btn = ttk.Button(entertainment_frame, text="Submit", command=events)
events_btn.grid(row=3, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
subscriptions_lbl = ttk.Label(entertainment_frame, text="Subscriptions")
subscriptions_lbl.grid(row=4, column=0, padx=3, pady=3)

subscriptions_entry = IntVar()
subscriptions_entry = ttk.Entry(entertainment_frame, textvariable=subscriptions_entry, width=10)
subscriptions_entry.grid(row=4, column=1, padx=3, pady=3)

subscriptions_btn = ttk.Button(entertainment_frame, text="Submit", command=subscriptions)
subscriptions_btn.grid(row=4, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
ent_misc_lbl = ttk.Label(entertainment_frame, text="Miscellaneous")
ent_misc_lbl.grid(row=5, column=0, padx=3, pady=3)

ent_misc_entry = IntVar()
ent_misc_entry = ttk.Entry(entertainment_frame, textvariable=ent_misc_entry, width=10)
ent_misc_entry.grid(row=5, column=1, padx=3, pady=3)

ent_misc_btn = ttk.Button(entertainment_frame, text="Submit", command=ent_misc)
ent_misc_btn.grid(row=5, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
ent_blank1 = ttk.Label(entertainment_frame, text="")
ent_blank1.grid(row=6, column=0, padx=3, pady=3)

root.mainloop()
