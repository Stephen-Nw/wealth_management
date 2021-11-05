from tkinter import *
from tkinter import ttk
from tkinter.font import Font

root = Tk()
root.title("Reports")
main_frame = ttk.Frame(root, padding=10, width=950, height=350)
main_frame.grid(row=0, column=0)

label_font = Font(family="Helvetica", size=8, weight="bold")


# ************** FUNCTIONS *****************************
def yearly_summary():
    pass


def yearly_breakdown():
    pass


def monthly_report():
    pass


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
selected_year3.grid(row=2, column=1, padx=5, pady=5)

choose_month = StringVar()
choose_month.set("Month")
selected_month = ttk.Combobox(main_frame, textvariable=choose_month, values=month, state="readonly",
                              width=10, justify="center")
selected_month.grid(row=2, column=2, padx=5, pady=5)

month_button = ttk.Button(main_frame, text="Submit", command=monthly_report)
month_button.grid(row=2, column=3, padx=5, pady=5)

root.mainloop()
