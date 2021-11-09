from tkinter import *
from tkinter import ttk
from tkinter.font import Font


def financial_summary():
    root = Tk()
    root.title("Yearly Summary")
    main_frame = ttk.Frame(root, padding=10, width=950, height=350)
    main_frame.grid(row=0, column=0)

    def go_back():
        pass

    heading_font = Font(family="Helvetica", size=10, weight="bold")
    label_font = Font(family="Helvetica", size=8, weight="bold")

    heading_text = "Financial Summary"
    income_text = "Yearly Income"
    expense_text = "Yearly Expenses"
    savings_text = "Yearly Savings"
    investment_text = "Yearly Investments"

    heading_label = ttk.Label(main_frame, text=heading_text, font=heading_font, anchor="center", padding=5)
    heading_label.grid(row=0, column=0, columnspan=2, padx=5)

    income_label = ttk.Label(main_frame, text=income_text, font=label_font)
    income_label.grid(row=1, column=0, pady=5, padx=5)

    income_amount = ttk.Label(main_frame, text="blank1", font=label_font)
    income_amount.grid(row=1, column=1, pady=5, padx=5)

    expense_label = ttk.Label(main_frame, text=expense_text, font=label_font)
    expense_label.grid(row=2, column=0, pady=5, padx=5)

    expense_amount = ttk.Label(main_frame, text="blank2", font=label_font)
    expense_amount.grid(row=2, column=1, padx=5)

    savings_label = ttk.Label(main_frame, text=savings_text, font=label_font)
    savings_label.grid(row=3, column=0, pady=5, padx=5)

    savings_amount = ttk.Label(main_frame, text="blank3", font=label_font)
    savings_amount.grid(row=3, column=1, padx=5)

    investment_label = ttk.Label(main_frame, text=investment_text, font=label_font)
    investment_label.grid(row=4, column=0, pady=5, padx=5)

    investment_amount = ttk.Label(main_frame, text="blank4", font=label_font)
    investment_amount.grid(row=4, column=1, padx=5)

    back_btn = ttk.Button(main_frame, text="Back", command=go_back)
    back_btn.grid(row=5, column=0, columnspan=2, pady=5)





    root.mainloop()

financial_summary()