from tkinter import *
from tkinter import ttk
from tkinter.font import Font


root = Tk()
root.title("Reports")
main_frame = ttk.Frame(root, padding=10, width=950, height=350)
main_frame.grid(row=0, column=0)

label_font = Font(family="Helvetica", size=10, weight="bold")


# ************** FUNCTIONS *****************************
def yearly_summary():
    pass


# ************* CONSTANTS *******************
summary_text = "Yearly Summary"

year = []
for num in range(0, 11):
    year.append(2020 + num)
# print(year)


# ************* Yearly Summary ******************
summary_label = ttk.Label(main_frame, text=summary_text, font=label_font, anchor="center", padding=10)
summary_label.grid(row=0, column=0, padx=5, pady=10)

choose_year = StringVar()
choose_year.set("Choose year")
selected_year = ttk.Combobox(main_frame, textvariable=choose_year, values=year, state="readonly", width=15)
selected_year.grid(row=0, column=1, padx=5, pady=10)

summary_button = ttk.Button(main_frame, text="Create User", command=yearly_summary)
summary_button.grid(row=0, column=2, padx=5, pady=10)




root.mainloop()

