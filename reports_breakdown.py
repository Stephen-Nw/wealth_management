from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from home_page import home
from tkinter import messagebox
from finance_database import financial_summary, yearly_financial_breakdown, monthly_financial_breakdown

root = Tk()
root.title("Reports")
main_frame = ttk.Frame(root, padding=10, width=950, height=350)
main_frame.grid(row=0, column=0)

exit_frame = ttk.Frame(root, width=950, height=350)
exit_frame.grid(row=1, column=0)

label_font = Font(family="Helvetica", size=8, weight="bold")


# ************** FUNCTIONS *****************************
def yearly_summary():
    """Display financial summary for chosen year"""
    try:
        chosen_year = int(choose_year1.get())
    except ValueError:
        messagebox.showerror(title="Error!!", message="Choose a Year!!")
    else:
        root.destroy()
        financial_summary(chosen_year)


def yearly_breakdown():
    """Display financial breakdown for chosen year"""
    try:
        chosen_year = int(choose_year2.get())
    except ValueError:
        messagebox.showerror(title="Error!!", message="Choose a Year!!")
    else:
        print(chosen_year)
        root.destroy()
        yearly_financial_breakdown(chosen_year)


def monthly_report():
    """Display financial breakdown for chosen month"""
    try:
        chosen_year = int(choose_year3.get())
    except ValueError:
        messagebox.showerror(title="Error!!", message="Choose a Year!!")
    else:
        print(chosen_year)
        chosen_month = choose_month.get()
        print(chosen_month)
        monthly_financial_breakdown(chosen_year, chosen_month)


def return_main():
    """Return user to main page"""
    root.destroy()
    home()


def exit_fxn():
    """Return user to login page"""
    root.destroy()
    from main import main_page
    main_page()


# ************* CONSTANTS *******************
summary_text = "Yearly Summary"
breakdown_text = "Yearly Breakdown"
monthly_text = "Monthly Reports"

year = []
for num in range(0, 11):
    year.append(2020 + num)

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
         "November", "December"]

# ************* Yearly Summary ******************
summary_label = ttk.Label(main_frame, text=summary_text, font=label_font, anchor="center", padding=5)
summary_label.grid(row=0, column=0)

choose_year1 = StringVar()
choose_year1.set("Year")
selected_year1 = ttk.Combobox(main_frame, textvariable=choose_year1, values=year, state="readonly",
                              width=5, justify="center")
selected_year1.grid(row=0, column=1, padx=5)

summary_button = ttk.Button(main_frame, text="Submit", command=yearly_summary)
summary_button.grid(row=0, column=2, padx=5)

# ************* Yearly breakdown ******************
breakdown_label = ttk.Label(main_frame, text=breakdown_text, font=label_font, anchor="center", padding=5)
breakdown_label.grid(row=1, column=0, pady=5)

choose_year2 = StringVar()
choose_year2.set("Year")
selected_year2 = ttk.Combobox(main_frame, textvariable=choose_year2, values=year, state="readonly",
                              width=5, justify="center")
selected_year2.grid(row=1, column=1, padx=5, pady=5)

breakdown_button = ttk.Button(main_frame, text="Submit", command=yearly_breakdown)
breakdown_button.grid(row=1, column=2, padx=5, pady=5)

# ************* Monthly report ******************
monthly_label = ttk.Label(main_frame, text=monthly_text, font=label_font, anchor="center", padding=5)
monthly_label.grid(row=2, column=0)

choose_year3 = StringVar()
choose_year3.set("Year")
selected_year3 = ttk.Combobox(main_frame, textvariable=choose_year3, values=year, state="readonly",
                              width=5, justify="center")
selected_year3.grid(row=2, column=1, padx=5)

choose_month = StringVar()
choose_month.set(month[0])
selected_month = ttk.Combobox(main_frame, textvariable=choose_month, values=month, state="readonly",
                              width=10, justify="center")
selected_month.grid(row=2, column=2, padx=5)

month_button = ttk.Button(main_frame, text="Submit", command=monthly_report)
month_button.grid(row=2, column=3, padx=5)

return_main_btn = ttk.Button(exit_frame, text="Return to main page", command=return_main)
return_main_btn.grid(row=0, column=0)

exit_fxn_btn = ttk.Button(exit_frame, text="Exit", command=exit_fxn)
exit_fxn_btn.grid(row=1, column=0, pady=5)

root.mainloop()
