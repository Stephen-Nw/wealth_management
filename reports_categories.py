from tkinter import *
from tkinter import ttk
from tkinter.font import Font


def financial_summary():
    root = Tk()
    root.title("Yearly Summary")
    main_frame = ttk.Frame(root, padding=10, width=950, height=350)
    main_frame.grid(row=0, column=0)

    label_font = Font(family="Helvetica", size=8, weight="bold")

    heading_text = "Financial Summary"
    income_text = "Yearly Income"

    heading_label = ttk.Label(main_frame, text=heading_text, font=label_font, anchor="center", padding=5)
    heading_label.grid(row=0, column=0, columnspan=2, pady=5, padx=5)

    income_label = ttk.Label(main_frame, text=income_text, font=label_font, anchor="center", padding=5)
    income_label.grid(row=0, column=0, columnspan=2, pady=5, padx=5)

    income_amount = ttk.Label(main_frame, text="blank1", font=label_font, anchor="center", padding=5)
    income_amount.grid(row=0, column=0, columnspan=2, pady=5, padx=5)






    root.mainloop()