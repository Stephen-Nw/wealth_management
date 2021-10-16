from tkinter import *
from tkinter import ttk
from tkinter.font import Font
# from expenses import expense_log


def home():
    """Home page after successful login"""
    app_name = "Make a Selection"

    root = Tk()
    root.title("Interprimos Wealth Management Solution")
    main_frame = ttk.Frame(root, padding=10, width=950, height=350)
    main_frame.grid(row=0, column=0)

    # =============BUTTON CONTROLS ============================== #
    def overview():
        pass

    def income():
        """Directs user to income page for user to document income"""
        from income import income_log
        root.destroy()
        income_log()

    def expense():
        """Directs user to expense page for user to document expenses"""
        from expenses import expense_log
        root.destroy()
        expense_log()

    def reports():
        pass

    def savings():
        pass

    def investment():
        pass

    def debt_to_income_ratio():
        pass

    def exit_fn():
        """Return user to login page"""
        root.destroy()
        from main import main_page
        main_page()

    # ==============FONTS ================================= #
    title_font = Font(family="Helvetica", size=10, weight="bold", slant="italic")

    # =============HOME PAGE DESIGN ============================== #
    app_label = ttk.Label(main_frame, text=app_name, font=title_font, wraplength=280, anchor="center", padding=10)
    app_label.grid(row=0, column=0, columnspan=2)

    overview_button = ttk.Button(main_frame, text="Overview", command=overview)
    overview_button.grid(row=1, column=0, pady=5, padx=5)

    income_button = ttk.Button(main_frame, text="Income", command=income)
    income_button.grid(row=1, column=1, pady=5, padx=5)

    expense_button = ttk.Button(main_frame, text="Expenses", command=expense)
    expense_button.grid(row=2, column=0, pady=5, padx=5)

    reports_button = ttk.Button(main_frame, text="Reports", command=reports)
    reports_button.grid(row=2, column=1, pady=5, padx=5)

    savings_button = ttk.Button(main_frame, text="Savings", command=savings)
    savings_button.grid(row=3, column=0, pady=5, padx=5)

    investment_button = ttk.Button(main_frame, text="Investment", command=investment)
    investment_button.grid(row=3, column=1, pady=5, padx=5)

    di_ratio_button = ttk.Button(main_frame, text="Debt-Income ratio", command=debt_to_income_ratio)
    di_ratio_button.grid(row=4, column=0, pady=5, columnspan=2, padx=5)

    exit_button = ttk.Button(main_frame, text="Exit", command=exit_fn)
    exit_button.grid(row=5, column=0, pady=5, columnspan=2, padx=5)

    root.mainloop()
