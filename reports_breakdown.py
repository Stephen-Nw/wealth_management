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


# ************* CONSTANTS *******************
summary_text = "Yearly Summary"
breakdown_text = "Yearly Breakdown"

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




root.mainloop()

