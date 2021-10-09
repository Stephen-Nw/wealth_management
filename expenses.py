from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
import datetime as dt
from finance_database import add_new_expense

app_name = "Expenses"

root = Tk()
root.title("Interprimos Wealth Management Solution")
main_style = ttk.Style()
main_style.configure("Main.TFrame", background="gray70")
main_frame = ttk.Frame(root, padding=10, width=930, height=330, style="Main.TFrame")
main_frame.grid(row=0, column=0)

# ================ STYLING ====================================== #
section_font = Font(family="Helvetica", weight="bold", slant="italic", size=10)
column_font = Font(family="Helvetica", weight="bold", size=8)
heading_color = "green1"
category_color = "AliceBlue"


# =============== FUNCTIONS ========================= #
def mortgage(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            mort_cat = category
            mort_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, mort_cat, mort_item, amt)

    mortgage_entry.delete(0, END)


def supplies(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            supplies_cat = category
            supplies_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, supplies_cat, supplies_item, amt)

    supplies_entry.delete(0, END)


def storage(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            storage_cat = category
            storage_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, storage_cat, storage_item, amt)

    storage_entry.delete(0, END)


def house_misc(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            house_misc_cat = category
            house_misc_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, house_misc_cat, house_misc_item, amt)

    house_misc_entry.delete(0, END)


def insurance(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            insurance_cat = category
            insurance_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, insurance_cat, insurance_item, amt)

    insurance_entry.delete(0, END)


def water(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            water_cat = category
            water_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, water_cat, water_item, amt)

    water_entry.delete(0, END)


def gas(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            gas_cat = category
            gas_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, gas_cat, gas_item, amt)

    gas_entry.delete(0, END)


def light(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            light_cat = category
            light_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, light_cat, light_item, amt)

    light_entry.delete(0, END)


def internet(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            internet_cat = category
            internet_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, internet_cat, internet_item, amt)

    internet_entry.delete(0, END)


def phone(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            phone_cat = category
            phone_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, phone_cat, phone_item, amt)

    phone_entry.delete(0, END)


def auto_gas(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            auto_gas_cat = category
            auto_gas_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, auto_gas_cat, auto_gas_item, amt)

    auto_gas_entry.delete(0, END)


def auto_ins(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            auto_ins_cat = category
            auto_ins_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, auto_ins_cat, auto_ins_item, amt)

    auto_ins_entry.delete(0, END)


def auto_maint(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            auto_maint_cat = category
            auto_maint_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, auto_maint_cat, auto_maint_item, amt)

    auto_maint_entry.delete(0, END)


def groceries(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            groceries_cat = category
            groceries_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, groceries_cat, groceries_item, amt)

    groceries_entry.delete(0, END)


def eatout(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            eatout_cat = category
            eatout_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, eatout_cat, eatout_item, amt)

    eatout_entry.delete(0, END)


def snacks(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            snacks_cat = category
            snacks_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, snacks_cat, snacks_item, amt)

    snacks_entry.delete(0, END)


def copay(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            copay_cat = category
            copay_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, copay_cat, copay_item, amt)

    copay_entry.delete(0, END)


def meds(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            meds_cat = category
            meds_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, meds_cat, meds_item, amt)

    meds_entry.delete(0, END)


def gym(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            gym_cat = category
            gym_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, gym_cat, gym_item, amt)

    gym_entry.delete(0, END)


def streaming(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            streaming_cat = category
            streaming_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, streaming_cat, streaming_item, amt)

    streaming_entry.delete(0, END)


def events(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            events_cat = category
            events_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, events_cat, events_item, amt)

    events_entry.delete(0, END)


def subscriptions(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            subscriptions_cat = category
            subscriptions_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, subscriptions_cat, subscriptions_item, amt)

    subscriptions_entry.delete(0, END)


def ent_misc(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            ent_misc_cat = category
            ent_misc_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, ent_misc_cat, ent_misc_item, amt)

    ent_misc_entry.delete(0, END)


def car_loans(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            car_loans_cat = category
            car_loans_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, car_loans_cat, car_loans_item, amt)

    car_loans_entry.delete(0, END)


def std_loans(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            std_loans_cat = category
            std_loans_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, std_loans_cat, std_loans_item, amt)

    std_loans_entry.delete(0, END)


def cards(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            cards_cat = category
            cards_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, cards_cat, cards_item, amt)

    cards_entry.delete(0, END)


def med_bills(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            med_bills_cat = category
            med_bills_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, med_bills_cat, med_bills_item, amt)

    med_bills_entry.delete(0, END)


def taxes(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            taxes_cat = category
            taxes_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, taxes_cat, taxes_item, amt)

    taxes_entry.delete(0, END)


def upkeep(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            upkeep_cat = category
            upkeep_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, upkeep_cat, upkeep_item, amt)

    upkeep_entry.delete(0, END)


def edu(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            edu_cat = category
            edu_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, edu_cat, edu_item, amt)

    edu_entry.delete(0, END)


def clothing(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            clothing_cat = category
            clothing_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, clothing_cat, clothing_item, amt)

    clothing_entry.delete(0, END)


def person_misc(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            person_misc_cat = category
            person_misc_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, person_misc_cat, person_misc_item, amt)

    person_misc_entry.delete(0, END)


def person_subscr(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            person_subscr_cat = category
            person_subscr_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, person_subscr_cat, person_subscr_item, amt)

    person_subscr_entry.delete(0, END)


def tithes(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            tithes_cat = category
            tithes_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, tithes_cat, tithes_item, amt)

    tithes_entry.delete(0, END)


def donations(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            donations_cat = category
            donations_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, donations_cat, donations_item, amt)

    donations_entry.delete(0, END)


def others(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            others_cat = category
            others_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, others_cat, others_item, amt)

    others_entry.delete(0, END)


def outing(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            outing_cat = category
            outing_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, outing_cat, outing_item, amt)

    outing_entry.delete(0, END)


def fam_clothing(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            fam_clothing_cat = category
            fam_clothing_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, fam_clothing_cat, fam_clothing_item, amt)

    fam_clothing_entry.delete(0, END)


def fam_gifts(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            fam_gifts_cat = category
            fam_gifts_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, fam_gifts_cat, fam_gifts_item, amt)

    fam_gifts_entry.delete(0, END)


def school(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            school_cat = category
            school_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, school_cat, school_item, amt)

    school_entry.delete(0, END)


def fam_misc(category, item, amount):
    try:
        amt = int(amount)
    except ValueError:
        messagebox.showerror(title="Error!!", message="Please type whole numbers only")
    else:
        if amt < 0:
            messagebox.showerror(title="Error!!", message="Number cannot be less than zero!!")
        else:
            fam_misc_cat = category
            fam_misc_item = item
            current_timestamp = dt.datetime.now()
            current_day = dt.datetime.strftime(current_timestamp, "%Y-%m-%d")

            add_new_expense(current_day, fam_misc_cat, fam_misc_item, amt)

    fam_misc_entry.delete(0, END)


# =============== FRAMES ============================ #
s = ttk.Style()
s.configure('Section.TFrame', background=category_color, borderwidth=5, relief="solid")

housing_frame = ttk.Frame(main_frame, style="Section.TFrame")
housing_frame.grid(row=0, column=0, padx=10, pady=10)

utilities_frame = ttk.Frame(main_frame, style="Section.TFrame")
utilities_frame.grid(row=0, column=1, padx=10, pady=10)

family_frame = ttk.Frame(main_frame, style="Section.TFrame")
family_frame.grid(row=0, column=2, padx=10, pady=10)

personal_frame = ttk.Frame(main_frame, style="Section.TFrame")
personal_frame.grid(row=0, column=3, padx=10, pady=10)

debt_frame = ttk.Frame(main_frame, style="Section.TFrame")
debt_frame.grid(row=1, column=0, padx=10, pady=10)

entertainment_frame = ttk.Frame(main_frame, style="Section.TFrame")
entertainment_frame.grid(row=1, column=1, padx=10, pady=10)

food_frame = ttk.Frame(main_frame, style="Section.TFrame")
food_frame.grid(row=1, column=2, padx=10, pady=10)

auto_frame = ttk.Frame(main_frame, style="Section.TFrame")
auto_frame.grid(row=1, column=3, padx=10, pady=10)

health_frame = ttk.Frame(main_frame, style="Section.TFrame")
health_frame.grid(row=2, column=0, padx=10, pady=10)

giving_frame = ttk.Frame(main_frame, style="Section.TFrame")
giving_frame.grid(row=2, column=1, padx=10, pady=10)

# ================ EXPENSES CATEGORIES ================  #
# **************** Housing ***************************** #
housing_header = ttk.Label(housing_frame, text="Housing", font=section_font, justify="center", background=heading_color)
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

mortgage_btn = ttk.Button(housing_frame, text="Submit", command=lambda: mortgage(housing_header["text"],
                                                                                 mortgage_lbl["text"],
                                                                                 mortgage_entry.get()))
mortgage_btn.grid(row=2, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------- #
supplies_lbl = ttk.Label(housing_frame, text="Supplies")
supplies_lbl.grid(row=3, column=0, padx=3, pady=3)

supplies_entry = IntVar()
supplies_entry = ttk.Entry(housing_frame, textvariable=supplies_entry, width=10)
supplies_entry.grid(row=3, column=1, padx=3, pady=3)

supplies_btn = ttk.Button(housing_frame, text="Submit", command=lambda: supplies(housing_header["text"],
                                                                                 supplies_lbl["text"],
                                                                                 supplies_entry.get()))
supplies_btn.grid(row=3, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
storage_lbl = ttk.Label(housing_frame, text="Storage")
storage_lbl.grid(row=4, column=0, padx=3, pady=3)

storage_entry = IntVar()
storage_entry = ttk.Entry(housing_frame, textvariable=storage_entry, width=10)
storage_entry.grid(row=4, column=1, padx=3, pady=3)

storage_btn = ttk.Button(housing_frame, text="Submit", command=lambda: storage(housing_header["text"],
                                                                               storage_lbl["text"],
                                                                               storage_entry.get()))
storage_btn.grid(row=4, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
house_misc_lbl = ttk.Label(housing_frame, text="Miscellaneous")
house_misc_lbl.grid(row=5, column=0, padx=3, pady=3)

house_misc_entry = IntVar()
house_misc_entry = ttk.Entry(housing_frame, textvariable=house_misc_entry, width=10)
house_misc_entry.grid(row=5, column=1, padx=3, pady=3)

house_misc_btn = ttk.Button(housing_frame, text="Submit", command=lambda: house_misc(housing_header["text"],
                                                                                     house_misc_lbl["text"],
                                                                                     house_misc_entry.get()))
house_misc_btn.grid(row=5, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
insurance_lbl = ttk.Label(housing_frame, text="Insurance")
insurance_lbl.grid(row=6, column=0, padx=3, pady=3)

insurance_entry = IntVar()
insurance_entry = ttk.Entry(housing_frame, textvariable=insurance_entry, width=10)
insurance_entry.grid(row=6, column=1, padx=3, pady=3)

insurance_btn = ttk.Button(housing_frame, text="Submit", command=lambda: insurance(housing_header["text"],
                                                                                   insurance_lbl["text"],
                                                                                   insurance_entry.get()))
insurance_btn.grid(row=6, column=2, pady=3, padx=3)

# **************** Utilities ***************************** #
utilities_header = ttk.Label(utilities_frame, text="Utilities", font=section_font, justify="center",
                             background=heading_color)
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

water_btn = ttk.Button(utilities_frame, text="Submit", command=lambda: water(utilities_header["text"],
                                                                             water_lbl["text"],
                                                                             water_entry.get()))
water_btn.grid(row=2, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
gas_lbl = ttk.Label(utilities_frame, text="Gas")
gas_lbl.grid(row=3, column=0, padx=3, pady=3)

gas_entry = IntVar()
gas_entry = ttk.Entry(utilities_frame, textvariable=gas_entry, width=10)
gas_entry.grid(row=3, column=1, padx=3, pady=3)

gas_btn = ttk.Button(utilities_frame, text="Submit", command=lambda: gas(utilities_header["text"],
                                                                         gas_lbl["text"],
                                                                         gas_entry.get()))
gas_btn.grid(row=3, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
light_lbl = ttk.Label(utilities_frame, text="Electricity")
light_lbl.grid(row=4, column=0, padx=3, pady=3)

light_entry = IntVar()
light_entry = ttk.Entry(utilities_frame, textvariable=light_entry, width=10)
light_entry.grid(row=4, column=1, padx=3, pady=3)

light_btn = ttk.Button(utilities_frame, text="Submit", command=lambda: light(utilities_header["text"],
                                                                             light_lbl["text"],
                                                                             light_entry.get()))
light_btn.grid(row=4, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
internet_lbl = ttk.Label(utilities_frame, text="Internet")
internet_lbl.grid(row=5, column=0, padx=3, pady=3)

internet_entry = IntVar()
internet_entry = ttk.Entry(utilities_frame, textvariable=internet_entry, width=10)
internet_entry.grid(row=5, column=1, padx=3, pady=3)

internet_btn = ttk.Button(utilities_frame, text="Submit", command=lambda: internet(utilities_header["text"],
                                                                                   internet_lbl["text"],
                                                                                   internet_entry.get()))
internet_btn.grid(row=5, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
phone_lbl = ttk.Label(utilities_frame, text="Phone")
phone_lbl.grid(row=6, column=0, padx=3, pady=3)

phone_entry = IntVar()
phone_entry = ttk.Entry(utilities_frame, textvariable=phone_entry, width=10)
phone_entry.grid(row=6, column=1, padx=3, pady=3)

phone_btn = ttk.Button(utilities_frame, text="Submit", command=lambda: phone(utilities_header["text"],
                                                                             phone_lbl["text"],
                                                                             phone_entry.get()))
phone_btn.grid(row=6, column=2, pady=3, padx=3)

# ***************** Automobiles ***************************** #
auto_header = ttk.Label(auto_frame, text="Automobile", font=section_font, justify="center", background=heading_color)
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

auto_gas_btn = ttk.Button(auto_frame, text="Submit", command=lambda: auto_gas(auto_header["text"],
                                                                              auto_gas_lbl["text"],
                                                                              auto_gas_entry.get()))
auto_gas_btn.grid(row=2, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
auto_ins_lbl = ttk.Label(auto_frame, text="Insurance")
auto_ins_lbl.grid(row=3, column=0, padx=3, pady=3)

auto_ins_entry = IntVar()
auto_ins_entry = ttk.Entry(auto_frame, textvariable=auto_ins_entry, width=10)
auto_ins_entry.grid(row=3, column=1, padx=3, pady=3)

auto_ins_btn = ttk.Button(auto_frame, text="Submit", command=lambda: auto_ins(auto_header["text"],
                                                                              auto_ins_lbl["text"],
                                                                              auto_ins_entry.get()))
auto_ins_btn.grid(row=3, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
auto_maint_lbl = ttk.Label(auto_frame, text="Maintenance")
auto_maint_lbl.grid(row=4, column=0, padx=3, pady=3)

auto_maint_entry = IntVar()
auto_maint_entry = ttk.Entry(auto_frame, textvariable=auto_maint_entry, width=10)
auto_maint_entry.grid(row=4, column=1, padx=3, pady=3)

auto_maint_btn = ttk.Button(auto_frame, text="Submit", command=lambda: auto_maint(auto_header["text"],
                                                                                  auto_maint_lbl["text"],
                                                                                  auto_maint_entry.get()))
auto_maint_btn.grid(row=4, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
auto_blank1 = ttk.Label(auto_frame, text="")
auto_blank1.grid(row=5, column=0, padx=3, pady=3)
# ------------------------------------------------------------------------ #
auto_blank2 = ttk.Label(auto_frame, text="")
auto_blank2.grid(row=6, column=0, padx=3, pady=3)

# ***************** Food ***************************** #
food_header = ttk.Label(food_frame, text="Food", font=section_font, justify="center", background=heading_color)
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

groceries_btn = ttk.Button(food_frame, text="Submit", command=lambda: groceries(food_header["text"],
                                                                                groceries_lbl["text"],
                                                                                groceries_entry.get()))
groceries_btn.grid(row=2, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
eatout_lbl = ttk.Label(food_frame, text="Eating Out")
eatout_lbl.grid(row=3, column=0, padx=3, pady=3)

eatout_entry = IntVar()
eatout_entry = ttk.Entry(food_frame, textvariable=eatout_entry, width=10)
eatout_entry.grid(row=3, column=1, padx=3, pady=3)

eatout_btn = ttk.Button(food_frame, text="Submit", command=lambda: eatout(food_header["text"],
                                                                          eatout_lbl["text"],
                                                                          eatout_entry.get()))
eatout_btn.grid(row=3, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
snacks_lbl = ttk.Label(food_frame, text="Snacks")
snacks_lbl.grid(row=4, column=0, padx=3, pady=3)

snacks_entry = IntVar()
snacks_entry = ttk.Entry(food_frame, textvariable=snacks_entry, width=10)
snacks_entry.grid(row=4, column=1, padx=3, pady=3)

snacks_btn = ttk.Button(food_frame, text="Submit", command=lambda: snacks(food_header["text"],
                                                                          snacks_lbl["text"],
                                                                          snacks_entry.get()))
snacks_btn.grid(row=4, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
food_blank1 = ttk.Label(food_frame, text="")
food_blank1.grid(row=5, column=0, padx=3, pady=3)
# ------------------------------------------------------------------------ #
food_blank2 = ttk.Label(food_frame, text="")
food_blank2.grid(row=6, column=0, padx=3, pady=3)

# ***************** Health ***************************** #
health_header = ttk.Label(health_frame, text="Health/Fitness", font=section_font, justify="center",
                          background=heading_color)
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

copay_btn = ttk.Button(health_frame, text="Submit", command=lambda: copay(health_header["text"],
                                                                          copay_lbl["text"],
                                                                          copay_entry.get()))
copay_btn.grid(row=2, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
meds_lbl = ttk.Label(health_frame, text="Medications")
meds_lbl.grid(row=3, column=0, padx=3, pady=3)

meds_entry = IntVar()
meds_entry = ttk.Entry(health_frame, textvariable=meds_entry, width=10)
meds_entry.grid(row=3, column=1, padx=3, pady=3)

meds_btn = ttk.Button(health_frame, text="Submit", command=lambda: meds(health_header["text"],
                                                                        meds_lbl["text"],
                                                                        meds_entry.get()))
meds_btn.grid(row=3, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
gym_lbl = ttk.Label(health_frame, text="Gym")
gym_lbl.grid(row=4, column=0, padx=3, pady=3)

gym_entry = IntVar()
gym_entry = ttk.Entry(health_frame, textvariable=gym_entry, width=10)
gym_entry.grid(row=4, column=1, padx=3, pady=3)

gym_btn = ttk.Button(health_frame, text="Submit", command=lambda: gym(health_header["text"],
                                                                      gym_lbl["text"],
                                                                      gym_entry.get()))
gym_btn.grid(row=4, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
health_blank1 = ttk.Label(health_frame, text="")
health_blank1.grid(row=5, column=0, padx=3, pady=3)
# ------------------------------------------------------------------------ #
health_blank2 = ttk.Label(health_frame, text="")
health_blank2.grid(row=6, column=0, padx=3, pady=3)

# ***************** Entertainment ***************************** #
entertainment_header = ttk.Label(entertainment_frame, text="Entertainment", font=section_font, justify="center",
                                 background=heading_color)
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

streaming_btn = ttk.Button(entertainment_frame, text="Submit", command=lambda: streaming(entertainment_header["text"],
                                                                                         streaming_lbl["text"],
                                                                                         streaming_entry.get()))
streaming_btn.grid(row=2, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
events_lbl = ttk.Label(entertainment_frame, text="Events")
events_lbl.grid(row=3, column=0, padx=3, pady=3)

events_entry = IntVar()
events_entry = ttk.Entry(entertainment_frame, textvariable=events_entry, width=10)
events_entry.grid(row=3, column=1, padx=3, pady=3)

events_btn = ttk.Button(entertainment_frame, text="Submit", command=lambda: events(entertainment_header["text"],
                                                                                   events_lbl["text"],
                                                                                   events_entry.get()))
events_btn.grid(row=3, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
subscriptions_lbl = ttk.Label(entertainment_frame, text="Subscriptions")
subscriptions_lbl.grid(row=4, column=0, padx=3, pady=3)

subscriptions_entry = IntVar()
subscriptions_entry = ttk.Entry(entertainment_frame, textvariable=subscriptions_entry, width=10)
subscriptions_entry.grid(row=4, column=1, padx=3, pady=3)

subscriptions_btn = ttk.Button(entertainment_frame, text="Submit",
                               command=lambda: subscriptions(entertainment_header["text"],
                                                             subscriptions_lbl["text"],
                                                             subscriptions_entry.get()))
subscriptions_btn.grid(row=4, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
ent_misc_lbl = ttk.Label(entertainment_frame, text="Miscellaneous")
ent_misc_lbl.grid(row=5, column=0, padx=3, pady=3)

ent_misc_entry = IntVar()
ent_misc_entry = ttk.Entry(entertainment_frame, textvariable=ent_misc_entry, width=10)
ent_misc_entry.grid(row=5, column=1, padx=3, pady=3)

ent_misc_btn = ttk.Button(entertainment_frame, text="Submit", command=lambda: ent_misc(entertainment_header["text"],
                                                                                       ent_misc_lbl["text"],
                                                                                       ent_misc_entry.get()))
ent_misc_btn.grid(row=5, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
ent_blank1 = ttk.Label(entertainment_frame, text="")
ent_blank1.grid(row=6, column=0, padx=3, pady=3)

# ***************** Debt ***************************** #
debt_header = ttk.Label(debt_frame, text="Debt", font=section_font, justify="center", background=heading_color)
debt_header.grid(row=0, column=0, columnspan=3)

debt_item = ttk.Label(debt_frame, text="Item", font=column_font)
debt_item.grid(row=1, column=0, padx=3)

debt_amount = ttk.Label(debt_frame, text="Amount", font=column_font)
debt_amount.grid(row=1, column=1, padx=3)
# ------------------------------------------------------------------------ #
car_loans_lbl = ttk.Label(debt_frame, text="Car")
car_loans_lbl.grid(row=2, column=0, padx=3, pady=3)

car_loans_entry = IntVar()
car_loans_entry = ttk.Entry(debt_frame, textvariable=car_loans_entry, width=10)
car_loans_entry.grid(row=2, column=1, padx=3, pady=3)

car_loans_btn = ttk.Button(debt_frame, text="Submit", command=lambda: car_loans(debt_header["text"],
                                                                                car_loans_lbl["text"],
                                                                                car_loans_entry.get()))
car_loans_btn.grid(row=2, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
std_loans_lbl = ttk.Label(debt_frame, text="Student loans")
std_loans_lbl.grid(row=3, column=0, padx=3, pady=3)

std_loans_entry = IntVar()
std_loans_entry = ttk.Entry(debt_frame, textvariable=std_loans_entry, width=10)
std_loans_entry.grid(row=3, column=1, padx=3, pady=3)

std_loans_btn = ttk.Button(debt_frame, text="Submit", command=lambda: std_loans(debt_header["text"],
                                                                                std_loans_lbl["text"],
                                                                                std_loans_entry.get()))
std_loans_btn.grid(row=3, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
cards_lbl = ttk.Label(debt_frame, text="Credit cards")
cards_lbl.grid(row=4, column=0, padx=3, pady=3)

cards_entry = IntVar()
cards_entry = ttk.Entry(debt_frame, textvariable=cards_entry, width=10)
cards_entry.grid(row=4, column=1, padx=3, pady=3)

cards_btn = ttk.Button(debt_frame, text="Submit", command=lambda: cards(debt_header["text"],
                                                                        cards_lbl["text"],
                                                                        cards_entry.get()))
cards_btn.grid(row=4, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
med_bills_lbl = ttk.Label(debt_frame, text="Medical bills")
med_bills_lbl.grid(row=5, column=0, padx=3, pady=3)

med_bills_entry = IntVar()
med_bills_entry = ttk.Entry(debt_frame, textvariable=med_bills_entry, width=10)
med_bills_entry.grid(row=5, column=1, padx=3, pady=3)

med_bills_btn = ttk.Button(debt_frame, text="Submit", command=lambda: med_bills(debt_header["text"],
                                                                                med_bills_lbl["text"],
                                                                                med_bills_entry.get()))
med_bills_btn.grid(row=5, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
taxes_lbl = ttk.Label(debt_frame, text="Taxes")
taxes_lbl.grid(row=6, column=0, padx=3, pady=3)

taxes_entry = IntVar()
taxes_entry = ttk.Entry(debt_frame, textvariable=taxes_entry, width=10)
taxes_entry.grid(row=6, column=1, padx=3, pady=3)

taxes_btn = ttk.Button(debt_frame, text="Submit", command=lambda: taxes(debt_header["text"],
                                                                        taxes_lbl["text"],
                                                                        taxes_entry.get()))
taxes_btn.grid(row=6, column=2, pady=3, padx=3)

# ***************** Personal ***************************** #
personal_header = ttk.Label(personal_frame, text="Personal", font=section_font, justify="center",
                            background=heading_color)
personal_header.grid(row=0, column=0, columnspan=3)

personal_item = ttk.Label(personal_frame, text="Item", font=column_font)
personal_item.grid(row=1, column=0, padx=3)

personal_amount = ttk.Label(personal_frame, text="Amount", font=column_font)
personal_amount.grid(row=1, column=1, padx=3)
# ------------------------------------------------------------------------ #
upkeep_lbl = ttk.Label(personal_frame, text="Upkeep")
upkeep_lbl.grid(row=2, column=0, padx=3, pady=3)

upkeep_entry = IntVar()
upkeep_entry = ttk.Entry(personal_frame, textvariable=upkeep_entry, width=10)
upkeep_entry.grid(row=2, column=1, padx=3, pady=3)

upkeep_btn = ttk.Button(personal_frame, text="Submit", command=lambda: upkeep(personal_header["text"],
                                                                              upkeep_lbl["text"],
                                                                              upkeep_entry.get()))
upkeep_btn.grid(row=2, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
edu_lbl = ttk.Label(personal_frame, text="Education")
edu_lbl.grid(row=3, column=0, padx=3, pady=3)

edu_entry = IntVar()
edu_entry = ttk.Entry(personal_frame, textvariable=edu_entry, width=10)
edu_entry.grid(row=3, column=1, padx=3, pady=3)

edu_btn = ttk.Button(personal_frame, text="Submit", command=lambda: edu(personal_header["text"],
                                                                        edu_lbl["text"],
                                                                        edu_entry.get()))
edu_btn.grid(row=3, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
clothing_lbl = ttk.Label(personal_frame, text="Clothing")
clothing_lbl.grid(row=4, column=0, padx=3, pady=3)

clothing_entry = IntVar()
clothing_entry = ttk.Entry(personal_frame, textvariable=clothing_entry, width=10)
clothing_entry.grid(row=4, column=1, padx=3, pady=3)

clothing_btn = ttk.Button(personal_frame, text="Submit", command=lambda: clothing(personal_header["text"],
                                                                                  clothing_lbl["text"],
                                                                                  clothing_entry.get()))
clothing_btn.grid(row=4, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
person_misc_lbl = ttk.Label(personal_frame, text="Miscellaneous")
person_misc_lbl.grid(row=5, column=0, padx=3, pady=3)

person_misc_entry = IntVar()
person_misc_entry = ttk.Entry(personal_frame, textvariable=person_misc_entry, width=10)
person_misc_entry.grid(row=5, column=1, padx=3, pady=3)

person_misc_btn = ttk.Button(personal_frame, text="Submit", command=lambda: person_misc(personal_header["text"],
                                                                                        person_misc_lbl["text"],
                                                                                        person_misc_entry.get()))
person_misc_btn.grid(row=5, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
person_subscr_lbl = ttk.Label(personal_frame, text="Taxes")
person_subscr_lbl.grid(row=6, column=0, padx=3, pady=3)

person_subscr_entry = IntVar()
person_subscr_entry = ttk.Entry(personal_frame, textvariable=person_subscr_entry, width=10)
person_subscr_entry.grid(row=6, column=1, padx=3, pady=3)

person_subscr_btn = ttk.Button(personal_frame, text="Submit", command=lambda: person_subscr(personal_header["text"],
                                                                                            person_subscr_lbl["text"],
                                                                                            person_subscr_entry.get()))
person_subscr_btn.grid(row=6, column=2, pady=3, padx=3)

# ***************** Giving ***************************** #
giving_header = ttk.Label(giving_frame, text="Giving", font=section_font, justify="center", background=heading_color)
giving_header.grid(row=0, column=0, columnspan=3)

giving_item = ttk.Label(giving_frame, text="Item", font=column_font)
giving_item.grid(row=1, column=0, padx=3)

giving_amount = ttk.Label(giving_frame, text="Amount", font=column_font)
giving_amount.grid(row=1, column=1, padx=3)
# ------------------------------------------------------------------------ #
tithes_lbl = ttk.Label(giving_frame, text="Tithes/Offering")
tithes_lbl.grid(row=2, column=0, padx=3, pady=3)

tithes_entry = IntVar()
tithes_entry = ttk.Entry(giving_frame, textvariable=tithes_entry, width=10)
tithes_entry.grid(row=2, column=1, padx=3, pady=3)

tithes_btn = ttk.Button(giving_frame, text="Submit", command=lambda: tithes(giving_header["text"],
                                                                            tithes_lbl["text"],
                                                                            tithes_entry.get()))
tithes_btn.grid(row=2, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
donations_lbl = ttk.Label(giving_frame, text="Donations")
donations_lbl.grid(row=3, column=0, padx=3, pady=3)

donations_entry = IntVar()
donations_entry = ttk.Entry(giving_frame, textvariable=donations_entry, width=10)
donations_entry.grid(row=3, column=1, padx=3, pady=3)

donations_btn = ttk.Button(giving_frame, text="Submit", command=lambda: donations(giving_header["text"],
                                                                                  donations_lbl["text"],
                                                                                  donations_entry.get()))
donations_btn.grid(row=3, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
others_lbl = ttk.Label(giving_frame, text="Other giving")
others_lbl.grid(row=4, column=0, padx=3, pady=3)

others_entry = IntVar()
others_entry = ttk.Entry(giving_frame, textvariable=others_entry, width=10)
others_entry.grid(row=4, column=1, padx=3, pady=3)

others_btn = ttk.Button(giving_frame, text="Submit", command=lambda: others(giving_header["text"],
                                                                            others_lbl["text"],
                                                                            others_entry.get()))
others_btn.grid(row=4, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
others_blank1 = ttk.Label(giving_frame, text="")
others_blank1.grid(row=5, column=0, padx=3, pady=3)
# ------------------------------------------------------------------------ #
others_blank2 = ttk.Label(giving_frame, text="")
others_blank2.grid(row=6, column=0, padx=3, pady=3)

# ***************** Family ***************************** #
family_header = ttk.Label(family_frame, text="Family", font=section_font, justify="center", background=heading_color)
family_header.grid(row=0, column=0, columnspan=3)

family_item = ttk.Label(family_frame, text="Item", font=column_font)
family_item.grid(row=1, column=0, padx=3)

family_amount = ttk.Label(family_frame, text="Amount", font=column_font)
family_amount.grid(row=1, column=1, padx=3)
# ------------------------------------------------------------------------ #
outing_lbl = ttk.Label(family_frame, text="Outing/Vacation")
outing_lbl.grid(row=2, column=0, padx=3, pady=3)

outing_entry = IntVar()
outing_entry = ttk.Entry(family_frame, textvariable=outing_entry, width=10)
outing_entry.grid(row=2, column=1, padx=3, pady=3)

outing_btn = ttk.Button(family_frame, text="Submit", command=lambda: outing(family_header["text"],
                                                                            outing_lbl["text"],
                                                                            outing_entry.get()))
outing_btn.grid(row=2, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
fam_clothing_lbl = ttk.Label(family_frame, text="Clothing")
fam_clothing_lbl.grid(row=3, column=0, padx=3, pady=3)

fam_clothing_entry = IntVar()
fam_clothing_entry = ttk.Entry(family_frame, textvariable=fam_clothing_entry, width=10)
fam_clothing_entry.grid(row=3, column=1, padx=3, pady=3)

fam_clothing_btn = ttk.Button(family_frame, text="Submit", command=lambda: fam_clothing(family_header["text"],
                                                                                        fam_clothing_lbl["text"],
                                                                                        fam_clothing_entry.get()))
fam_clothing_btn.grid(row=3, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
fam_gifts_lbl = ttk.Label(family_frame, text="Gifts")
fam_gifts_lbl.grid(row=4, column=0, padx=3, pady=3)

fam_gifts_entry = IntVar()
fam_gifts_entry = ttk.Entry(family_frame, textvariable=fam_gifts_entry, width=10)
fam_gifts_entry.grid(row=4, column=1, padx=3, pady=3)

fam_gifts_btn = ttk.Button(family_frame, text="Submit", command=lambda: fam_gifts(family_header["text"],
                                                                                  fam_gifts_lbl["text"],
                                                                                  fam_gifts_entry.get()))
fam_gifts_btn.grid(row=4, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
school_lbl = ttk.Label(family_frame, text="School")
school_lbl.grid(row=5, column=0, padx=3, pady=3)

school_entry = IntVar()
school_entry = ttk.Entry(family_frame, textvariable=school_entry, width=10)
school_entry.grid(row=5, column=1, padx=3, pady=3)

school_btn = ttk.Button(family_frame, text="Submit", command=lambda: school(family_header["text"],
                                                                            school_lbl["text"],
                                                                            school_entry.get()))
school_btn.grid(row=5, column=2, pady=3, padx=3)
# ------------------------------------------------------------------------ #
fam_misc_lbl = ttk.Label(family_frame, text="Miscellaneous")
fam_misc_lbl.grid(row=6, column=0, padx=3, pady=3)

fam_misc_entry = IntVar()
fam_misc_entry = ttk.Entry(family_frame, textvariable=fam_misc_entry, width=10)
fam_misc_entry.grid(row=6, column=1, padx=3, pady=3)

fam_misc_btn = ttk.Button(family_frame, text="Submit", command=lambda: fam_misc(family_header["text"],
                                                                                fam_misc_lbl["text"],
                                                                                fam_misc_entry.get()))
fam_misc_btn.grid(row=6, column=2, pady=3, padx=3)

root.mainloop()
