from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import sqlite3
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from home_page import home

db = sqlite3.connect("finance-db")
cursor = db.cursor()


# cursor.execute(
#     "CREATE TABLE user (username varchar(250) NOT NULL UNIQUE,"
#     "password varchar(250) NOT NULL UNIQUE,"
#     "question_one varchar(250),"
#     "answer_one varchar(250),"
#     "question_two varchar(250),"
#     "answer_two varchar(250),"
#     "question_three varchar(250),"
#     "answer_three varchar(250))"
# )

# cursor.execute(
#     "CREATE TABLE expense (date varchar(250),"
#     "category varchar(250),"
#     "item varchar(250),"
#     "amount int)"
# )

# cursor.execute(
#     "CREATE TABLE income (date varchar(250),"
#     "category varchar(250),"
#     "amount int)"
# )

# cursor.execute(
#     "CREATE TABLE savings (date varchar(250),"
#     "deposit int,"
#     "withdraw int)"
# )
#
# cursor.execute(
#     "CREATE TABLE investments (date varchar(250),"
#     "deposit int,"
#     "withdraw int)"
# )


def add_new_expense(dt, cat, itm, amt):
    """Add new expense to expense table"""
    cursor.execute("INSERT INTO expense VALUES (:date, :category, :item, :amount)",
                   {"date": dt, "category": cat, "item": itm, "amount": amt})
    db.commit()


def add_new_user(name, pword, q1, a1, q2, a2, q3, a3):
    """Add new user to user table"""
    cursor.execute("INSERT INTO user VALUES (:user, :password, :question_one, :answer_one, :question_two, "
                   ":answer_two, :question_three, :answer_three)", {"user": name, "password": pword, "question_one": q1,
                                                                    "answer_one": a1,
                                                                    "question_two": q2, "answer_two": a2,
                                                                    "question_three": q3, "answer_three": a3})
    db.commit()


def retrieve_user_info(name):
    """Retrieve specific user information from user table using username"""
    cursor.execute("SELECT * FROM user WHERE username=?", (name,))
    user_info = cursor.fetchall()
    return user_info


def update_user_password(name, p_word):
    """Update specific user password in user table"""
    cursor.execute("UPDATE user SET password = ? WHERE username = ?", (p_word, name))
    db.commit()


def add_new_income(dt, cat, amt):
    """Add new income to income table"""
    cursor.execute("INSERT INTO income VALUES (:date, :category, :amount)",
                   {"date": dt, "category": cat, "amount": amt})
    db.commit()


def update_savings(dt, dep, wdraw):
    """Add to deposits column"""
    cursor.execute("INSERT INTO savings VALUES (:date, :deposit, :withdraw)",
                   {"date": dt, "deposit": dep, "withdraw": wdraw})
    db.commit()


def update_investments(dt, dep, wdraw):
    """Add to deposits column"""
    cursor.execute("INSERT INTO investments VALUES (:date, :deposit, :withdraw)",
                   {"date": dt, "deposit": dep, "withdraw": wdraw})
    db.commit()


def financial_overview():
    """Create a bar chart summary of income and expenses for current year"""
    root = Tk()
    root.title("Overview")
    main_frame = ttk.Frame(root, padding=10, width=950, height=350)
    main_frame.grid(row=0, column=0)

    def return_main():
        """Return user to main page"""
        root.destroy()
        home()

    def exit_fxn():
        """Return user to login page"""
        root.destroy()
        from main import main_page
        main_page()

    # ***************Read sql for income and expense into dataframe *****************
    expense_df = pd.read_sql_query("SELECT * from expense", db)
    income_df = pd.read_sql_query("SELECT * from income", db)

    # **********Convert date to panda timestamp***********
    expense_df.date = pd.to_datetime(expense_df.date)  # or expense_df['date']
    income_df.date = pd.to_datetime(income_df.date)

    # **************** Create new columns 'year' and add to the dataframe ********
    expense_df['year'] = pd.DatetimeIndex(expense_df['date']).year
    income_df['year'] = pd.DatetimeIndex(income_df['date']).year

    # ********** Convert month from number to name using dt.month_name() function**********
    expense_df['month_name'] = expense_df.date.dt.month_name(locale='English')
    expense_df = expense_df.sort_values("date")

    income_df['month_name'] = income_df.date.dt.month_name(locale='English')
    income_df = income_df.sort_values("date")
    # print(income_df)

    # *********** Subset new dataframe for current year only ******************
    current_timestamp = dt.datetime.now()
    current_year = dt.datetime.strftime(current_timestamp, "%Y")
    is_current_year_expense = expense_df['year'] == int(current_year)  # Boolean that evaluates for  current year
    current_year_expense_df = expense_df[is_current_year_expense]

    is_current_year_income = income_df['year'] == int(current_year)
    current_year_income_df = income_df[is_current_year_income]

    # ********** Group DataFrame by month and convert to panda series**********
    expense_sum = current_year_expense_df.groupby("month_name")["amount"].sum()  # Panda series
    income_sum = current_year_income_df.groupby("month_name")["amount"].sum()

    # ********** Convert Panda Series to Dataframe**********
    total_expense_df = pd.DataFrame({"Month": expense_sum.index, "Expense": expense_sum.values})
    total_income_df = pd.DataFrame({"Month": income_sum.index, "Income": income_sum.values})

    # ************* Sort DataFrame by month ********************
    sort_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                  'October', 'November', 'December']
    total_expense_df.index = pd.CategoricalIndex(total_expense_df['Month'], categories=sort_order, ordered=True)
    total_expense_df = total_expense_df.sort_index().reset_index(drop=True)

    total_income_df.index = pd.CategoricalIndex(total_income_df['Month'], categories=sort_order, ordered=True)
    total_income_df = total_income_df.sort_index().reset_index(drop=True)

    # ************** Merge income and expense dataframes ************************
    combined_df = pd.merge(total_expense_df, total_income_df, how="outer")
    # print(combined_df)

    # ************** Create bar charts ************************

    labels = combined_df['Month']
    expense_column = combined_df['Expense']
    income_column = combined_df['Income']

    label_list = []
    expense_list = []
    income_list = []

    for item in labels:
        label_list.append(item)

    for item in expense_column:
        expense_list.append(item)

    for item in income_column:
        income_list.append(item)

    x = np.arange(len(label_list))  # label locations on chart
    width = 0.35  # width of bars

    fig, ax = plt.subplots()
    inc = ax.bar(x - width / 2, income_list, width, label='Income')
    exp = ax.bar(x + width / 2, expense_list, width, label='Expenses')

    ax.set_ylabel("Amount($)")
    ax.set_title("Financial Summary")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(inc, padding=2)
    ax.bar_label(exp, padding=2)

    fig.tight_layout()

    # ******************** Embed bar chart tkinter GUI **********************************
    canvas = FigureCanvasTkAgg(fig, master=main_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5)

    return_main_btn = ttk.Button(main_frame, text="Return to main page", command=return_main)
    return_main_btn.grid(row=1, column=0, padx=5, pady=5)

    exit_fxn_btn = ttk.Button(main_frame, text="Exit", command=exit_fxn)
    exit_fxn_btn.grid(row=2, column=0)

    # plt.show()
    plt.close()
    root.mainloop()


def financial_summary(chosen_year):
    """Calculate financial summary for selected year"""
    root = Tk()
    root.title("Yearly Summary")
    main_frame = ttk.Frame(root, padding=10, width=950, height=350)
    main_frame.grid(row=0, column=0)

    def go_back():
        """Return to home page"""
        root.destroy()
        from home_page import home
        home()

    # ****************************************************************************** #
    #                RETRIEVE DATA FROM DATABASE                                     #
    # ****************************************************************************** #
    expense_df = pd.read_sql_query("SELECT * from expense", db)
    income_df = pd.read_sql_query("SELECT * from income", db)
    savings_df = pd.read_sql_query("SELECT * from savings", db)
    investments_df = pd.read_sql_query("SELECT * from investments", db)

    #  **********Convert date to panda timestamp***********
    expense_df.date = pd.to_datetime(expense_df.date)
    income_df.date = pd.to_datetime(income_df.date)
    savings_df.date = pd.to_datetime(savings_df.date)
    investments_df.date = pd.to_datetime(investments_df.date)

    # **************** Create new columns 'year' and add to the dataframe ********
    expense_df['year'] = pd.DatetimeIndex(expense_df['date']).year
    income_df['year'] = pd.DatetimeIndex(income_df['date']).year
    savings_df['year'] = pd.DatetimeIndex(savings_df['date']).year
    investments_df['year'] = pd.DatetimeIndex(investments_df['date']).year

    # ********** Convert month from number to name using dt.month_name() function**********
    expense_df['month_name'] = expense_df.date.dt.month_name(locale='English')
    expense_df = expense_df.sort_values("date")

    income_df['month_name'] = income_df.date.dt.month_name(locale='English')
    income_df = income_df.sort_values("date")

    savings_df['month_name'] = savings_df.date.dt.month_name(locale='English')
    savings_df = savings_df.sort_values("date")

    investments_df['month_name'] = investments_df.date.dt.month_name(locale='English')
    investments_df = investments_df.sort_values("date")

    # ******************** Create df of year requested by user ***********************************
    requested_year = chosen_year
    # requested_year = 2021
    requested_year_expense = expense_df['year'] == requested_year
    requested_year_expense_df = expense_df[requested_year_expense]

    requested_year_income = income_df['year'] == requested_year
    requested_year_income_df = income_df[requested_year_income]

    requested_year_savings = savings_df['year'] == requested_year
    requested_year_savings_df = savings_df[requested_year_savings]

    requested_year_investments = investments_df['year'] == requested_year
    requested_year_investments_df = investments_df[requested_year_investments]

    income_sum = requested_year_income_df["amount"].sum()
    formatted_income = "$" + str(income_sum) + ".00"

    expense_sum = requested_year_expense_df["amount"].sum()
    formatted_expense = "$" + str(expense_sum) + ".00"

    savings_deposit = requested_year_savings_df["deposit"].sum()
    savings_withdraw = requested_year_savings_df["withdraw"].sum()
    savings_balance = savings_deposit - savings_withdraw
    formatted_savings = "$" + str(savings_balance) + ".00"

    investments_deposit = requested_year_investments_df["deposit"].sum()
    investments_withdraw = requested_year_investments_df["withdraw"].sum()
    investments_balance = investments_deposit - investments_withdraw
    formatted_investments = "$" + str(investments_balance) + ".00"

    # ****************************************************************************** #
    #          CREATE FINANCIAL SUMMARY STRUCTURE                                    #
    # ****************************************************************************** #

    heading_font = Font(family="Helvetica", size=10, weight="bold")
    label_font = Font(family="Helvetica", size=8, weight="bold")

    heading_text = f"{requested_year} Financial Summary"
    income_text = "Total Income"
    expense_text = "Total Expenses"
    savings_text = "Total Savings"
    investment_text = "Total Investments"

    heading_label = ttk.Label(main_frame, text=heading_text, font=heading_font, anchor="center", padding=5)
    heading_label.grid(row=0, column=0, columnspan=2, padx=5)

    income_label = ttk.Label(main_frame, text=income_text, font=label_font, justify="right")
    income_label.grid(row=1, column=0, pady=5)

    income_amount = ttk.Label(main_frame, text=formatted_income, relief="solid", padding=(5, 0, 5, 0))
    income_amount.grid(row=1, column=1, pady=5)

    expense_label = ttk.Label(main_frame, text=expense_text, font=label_font, justify="right")
    expense_label.grid(row=2, column=0, pady=5)

    expense_amount = ttk.Label(main_frame, text=formatted_expense, relief="solid", padding=(5, 0, 5, 0))
    expense_amount.grid(row=2, column=1)

    savings_label = ttk.Label(main_frame, text=savings_text, font=label_font, justify="right")
    savings_label.grid(row=3, column=0, pady=5)

    savings_amount = ttk.Label(main_frame, text=formatted_savings, relief="solid", padding=(5, 0, 5, 0))
    savings_amount.grid(row=3, column=1)

    investment_label = ttk.Label(main_frame, text=investment_text, font=label_font, justify="right")
    investment_label.grid(row=4, column=0, pady=5, padx=5)

    investment_amount = ttk.Label(main_frame, text=formatted_investments, relief="solid", padding=(5, 0, 5, 0))
    investment_amount.grid(row=4, column=1)

    back_btn = ttk.Button(main_frame, text="Back", command=go_back)
    back_btn.grid(row=5, column=0, columnspan=2, pady=5)

    root.mainloop()


def yearly_financial_breakdown(chosen_year):
    """Calculate yearly breakdown for selected year"""
    root = Tk()
    root.title("Yearly Expense Breakdown")

    main_frame = ttk.Frame(root, padding=10, width=950, height=300)
    main_frame.grid(row=0, column=0)

    main_frame2 = ttk.Frame(root, padding=10, width=950, height=300)
    main_frame2.grid(row=0, column=1)

    main_frame3 = ttk.Frame(root, padding=10, width=950, height=300)
    main_frame3.grid(row=1, column=0)

    main_frame4 = ttk.Frame(root, padding=10, width=950, height=300)
    main_frame4.grid(row=1, column=1)

    # ****************************************************************************** #
    #                RETRIEVE DATA FROM DATABASE                                     #
    # ****************************************************************************** #

    # ============Expenses==========================
    expense_df = pd.read_sql_query("SELECT * from expense", db)
    expense_df.date = pd.to_datetime(expense_df.date)  # Convert date to Panda timestamp
    expense_df['year'] = pd.DatetimeIndex(expense_df['date']).year  # Create new Year column

    requested_year = chosen_year
    # requested_year = 2021
    requested_year_expense = expense_df['year'] == requested_year
    requested_year_expense_df = expense_df[requested_year_expense]  # Create df of user requested year

    expense_breakdown = requested_year_expense_df.groupby("category")["amount"].sum()  # Panda series
    expense_breakdown_df = pd.DataFrame(
        {"Category": expense_breakdown.index, "Amount": expense_breakdown.values})  # Convert series to dataframe
    # print(expense_breakdown_df)

    category_column = expense_breakdown_df['Category']
    amount_column = expense_breakdown_df['Amount']

    category_list = []
    category_amount = []

    for item in category_column:
        category_list.append(item)

    for item in amount_column:
        category_amount.append(item)

    # print(category_list)
    # print(category_amount)

    # ======Income================
    income_df = pd.read_sql_query("SELECT * from income", db)
    income_df.date = pd.to_datetime(income_df.date)  # Convert date to Panda timestamp
    income_df['year'] = pd.DatetimeIndex(income_df['date']).year  # Create new Year column

    # requested_year = 2021
    requested_year_income = income_df['year'] == requested_year
    requested_year_income_df = income_df[requested_year_income]  # Create df of user requested year

    income_breakdown = requested_year_income_df.groupby("category")["amount"].sum()  # Panda series
    income_breakdown_df = pd.DataFrame(
        {"Category": income_breakdown.index, "Amount": income_breakdown.values})  # Convert series to dataframe
    print(income_breakdown_df)

    income_column = income_breakdown_df['Category']
    amount_column = income_breakdown_df['Amount']

    income_list = []
    income_amount = []

    for item in income_column:
        income_list.append(item)

    for item in amount_column:
        income_amount.append(item)

    print(income_list)
    print(income_amount)

    # ****************************************************************************** #
    #                   CREATE EXPENSE PIE CHART                                     #
    # ****************************************************************************** #
    fig, ax = plt.subplots()
    ax.pie(category_amount, labels=category_list, shadow=False, startangle=90, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title(f"{requested_year} Expense Breakdown")

    canvas = FigureCanvasTkAgg(fig, master=main_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5)
    # plt.show()
    # plt.close()

    # ****************************************************************************** #
    #                   CREATE INCOME PIE CHART                                      #
    # ****************************************************************************** #
    fig1, ax1 = plt.subplots()
    ax1.pie(income_amount, labels=income_list, shadow=False, startangle=90, autopct='%1.1f%%')
    ax1.axis('equal')
    plt.title(f"{requested_year} Income Breakdown")

    canvas = FigureCanvasTkAgg(fig1, master=main_frame3)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5)
    # plt.show()
    # plt.close()

    # ****************************************************************************** #
    #             CREATE EXPENSE TABLE BREAKDOWN                                     #
    # ****************************************************************************** #
    heading_font = Font(family="Helvetica", size=10, weight="bold")
    label_font = Font(family="Helvetica", size=8, weight="bold")

    category_text = "Category"
    amount_text = "Amount"
    automobile_text = "Automobile"
    debt_text = "Debt"
    entertainment_text = "Entertainment"
    family_text = "Family"
    food_text = "Food"
    giving_text = "Giving"
    fitness_text = "Health/Fitness"
    housing_text = "Housing"
    personal_text = "Personal"
    utilities_text = "Utilities"

    expense_dictionary = dict(zip(category_list, category_amount))
    # print(expense_dictionary)

    try:
        expense_dictionary["Automobile"]
    except KeyError:
        formatted_automobile = "$" + str(0) + ".00"
    else:
        formatted_automobile = "$" + str(expense_dictionary["Automobile"]) + ".00"

    try:
        expense_dictionary["Debt"]
    except KeyError:
        formatted_debt = "$" + str(0) + ".00"
    else:
        formatted_debt = "$" + str(expense_dictionary["Debt"]) + ".00"

    try:
        expense_dictionary["Entertainment"]
    except KeyError:
        formatted_entertainment = "$" + str(0) + ".00"
    else:
        formatted_entertainment = "$" + str(expense_dictionary["Entertainment"]) + ".00"

    try:
        expense_dictionary["Family"]
    except KeyError:
        formatted_family = "$" + str(0) + ".00"
    else:
        formatted_family = "$" + str(expense_dictionary["Family"]) + ".00"

    try:
        expense_dictionary["Food"]
    except KeyError:
        formatted_food = "$" + str(0) + ".00"
    else:
        formatted_food = "$" + str(expense_dictionary["Food"]) + ".00"

    try:
        expense_dictionary["Health/Fitness"]
    except KeyError:
        formatted_fitness = "$" + str(0) + ".00"
    else:
        formatted_fitness = "$" + str(expense_dictionary["Health/Fitness"]) + ".00"

    try:
        expense_dictionary["Giving"]
    except KeyError:
        formatted_giving = "$" + str(0) + ".00"
    else:
        formatted_giving = "$" + str(expense_dictionary["Giving"]) + ".00"

    try:
        expense_dictionary["Housing"]
    except KeyError:
        formatted_housing = "$" + str(0) + ".00"
    else:
        formatted_housing = "$" + str(expense_dictionary["Housing"]) + ".00"

    try:
        expense_dictionary["Personal"]
    except KeyError:
        formatted_personal = "$" + str(0) + ".00"
    else:
        formatted_personal = "$" + str(expense_dictionary["Personal"]) + ".00"

    try:
        expense_dictionary["Utilities"]
    except KeyError:
        formatted_utilities = "$" + str(0) + ".00"
    else:
        formatted_utilities = "$" + str(expense_dictionary["Utilities"]) + ".00"

    category_label = ttk.Label(main_frame2, text=category_text, font=heading_font, anchor="center", padding=5)
    category_label.grid(row=0, column=0, padx=5)

    amount_label = ttk.Label(main_frame2, text=amount_text, font=heading_font, anchor="center", padding=5)
    amount_label.grid(row=0, column=1, padx=5)

    automobile_label = ttk.Label(main_frame2, text=automobile_text, font=label_font, justify="right")
    automobile_label.grid(row=1, column=0, pady=5)

    automobile_amount = ttk.Label(main_frame2, text=formatted_automobile, relief="solid", padding=(5, 0, 5, 0))
    automobile_amount.grid(row=1, column=1, pady=5)

    debt_label = ttk.Label(main_frame2, text=debt_text, font=label_font, justify="right")
    debt_label.grid(row=2, column=0, pady=5)

    debt_amount = ttk.Label(main_frame2, text=formatted_debt, relief="solid", padding=(5, 0, 5, 0))
    debt_amount.grid(row=2, column=1)

    entertainment_label = ttk.Label(main_frame2, text=entertainment_text, font=label_font, justify="right")
    entertainment_label.grid(row=3, column=0, pady=5)

    entertainment_amount = ttk.Label(main_frame2, text=formatted_entertainment, relief="solid", padding=(5, 0, 5, 0))
    entertainment_amount.grid(row=3, column=1)

    family_label = ttk.Label(main_frame2, text=family_text, font=label_font, justify="right")
    family_label.grid(row=4, column=0, pady=5, padx=5)

    family_amount = ttk.Label(main_frame2, text=formatted_family, relief="solid", padding=(5, 0, 5, 0))
    family_amount.grid(row=4, column=1)

    food_label = ttk.Label(main_frame2, text=food_text, font=label_font, justify="right")
    food_label.grid(row=5, column=0, pady=5)

    food_amount = ttk.Label(main_frame2, text=formatted_food, relief="solid", padding=(5, 0, 5, 0))
    food_amount.grid(row=5, column=1)

    giving_label = ttk.Label(main_frame2, text=giving_text, font=label_font, justify="right")
    giving_label.grid(row=6, column=0, pady=5)

    giving_amount = ttk.Label(main_frame2, text=formatted_giving, relief="solid", padding=(5, 0, 5, 0))
    giving_amount.grid(row=6, column=1)

    fitness_label = ttk.Label(main_frame2, text=fitness_text, font=label_font, justify="right")
    fitness_label.grid(row=7, column=0, pady=5, padx=5)

    fitness_amount = ttk.Label(main_frame2, text=formatted_fitness, relief="solid", padding=(5, 0, 5, 0))
    fitness_amount.grid(row=7, column=1)

    housing_label = ttk.Label(main_frame2, text=housing_text, font=label_font, justify="right")
    housing_label.grid(row=8, column=0, pady=5)

    housing_amount = ttk.Label(main_frame2, text=formatted_housing, relief="solid", padding=(5, 0, 5, 0))
    housing_amount.grid(row=8, column=1)

    personal_label = ttk.Label(main_frame2, text=personal_text, font=label_font, justify="right")
    personal_label.grid(row=9, column=0, pady=5)

    personal_amount = ttk.Label(main_frame2, text=formatted_personal, relief="solid", padding=(5, 0, 5, 0))
    personal_amount.grid(row=9, column=1)

    utilities_label = ttk.Label(main_frame2, text=utilities_text, font=label_font, justify="right")
    utilities_label.grid(row=10, column=0, pady=5, padx=5)

    utilities_amount = ttk.Label(main_frame2, text=formatted_utilities, relief="solid", padding=(5, 0, 5, 0))
    utilities_amount.grid(row=10, column=1)

    # ****************************************************************************** #
    #             CREATE INCOME TABLE BREAKDOWN                                      #
    # ****************************************************************************** #
    income_category_text = "Category"
    income_amount_text = "Amount"
    add_income_text = "Additional income"
    misc_income_text = "Miscellaneous"
    pry_income_text = "Primary income"
    sec_income_text = "Secondary income"
    spouse_income_text = "Spouse income"

    income_dictionary = dict(zip(income_list, income_amount))
    print(income_dictionary)

    # formatted_add_income = "$" + str(income_dictionary["Additional income"]) + ".00"
    # formatted_misc_income = "$" + str(income_dictionary["Miscellaneous"]) + ".00"
    # formatted_pry_income = "$" + str(income_dictionary["Primary income"]) + ".00"
    # formatted_sec_income = "$" + str(income_dictionary["Secondary income"]) + ".00"
    # formatted_spouse_income = "$" + str(income_dictionary["Spouse income"]) + ".00"

    try:
        income_dictionary["Additional income"]
    except KeyError:
        formatted_add_income = "$" + str(0) + ".00"
    else:
        formatted_add_income = "$" + str(income_dictionary["Additional income"]) + ".00"

    try:
        income_dictionary["Miscellaneous"]
    except KeyError:
        formatted_misc_income = "$" + str(0) + ".00"
    else:
        formatted_misc_income = "$" + str(income_dictionary["Miscellaneous"]) + ".00"

    try:
        income_dictionary["Primary income"]
    except KeyError:
        formatted_pry_income = "$" + str(0) + ".00"
    else:
        formatted_pry_income = "$" + str(income_dictionary["Primary income"]) + ".00"

    try:
        income_dictionary["Secondary income"]
    except KeyError:
        formatted_sec_income = "$" + str(0) + ".00"
    else:
        formatted_sec_income = "$" + str(income_dictionary["Secondary income"]) + ".00"

    try:
        income_dictionary["Spouse income"]
    except KeyError:
        formatted_spouse_income = "$" + str(0) + ".00"
    else:
        formatted_spouse_income = "$" + str(income_dictionary["Spouse income"]) + ".00"


    income_category_label = ttk.Label(main_frame4, text=income_category_text, font=heading_font, anchor="center", padding=5)
    income_category_label.grid(row=0, column=0, padx=5)

    income_amount_label = ttk.Label(main_frame4, text=income_amount_text, font=heading_font, anchor="center", padding=5)
    income_amount_label.grid(row=0, column=1, padx=5)

    add_income_label = ttk.Label(main_frame4, text=add_income_text, font=label_font, justify="right")
    add_income_label.grid(row=1, column=0, pady=5)

    add_income_amount = ttk.Label(main_frame4, text=formatted_add_income, relief="solid", padding=(5, 0, 5, 0))
    add_income_amount.grid(row=1, column=1, pady=5)

    misc_income_label = ttk.Label(main_frame4, text=misc_income_text, font=label_font, justify="right")
    misc_income_label.grid(row=2, column=0, pady=5)

    misc_income_amount = ttk.Label(main_frame4, text=formatted_misc_income, relief="solid", padding=(5, 0, 5, 0))
    misc_income_amount.grid(row=2, column=1)

    pry_income_label = ttk.Label(main_frame4, text=pry_income_text, font=label_font, justify="right")
    pry_income_label.grid(row=3, column=0, pady=5)

    pry_income_amount = ttk.Label(main_frame4, text=formatted_pry_income, relief="solid", padding=(5, 0, 5, 0))
    pry_income_amount.grid(row=3, column=1)

    sec_income_label = ttk.Label(main_frame4, text=sec_income_text, font=label_font, justify="right")
    sec_income_label.grid(row=4, column=0, pady=5, padx=5)

    sec_income_amount = ttk.Label(main_frame4, text=formatted_sec_income, relief="solid", padding=(5, 0, 5, 0))
    sec_income_amount.grid(row=4, column=1)

    spouse_income_label = ttk.Label(main_frame4, text=spouse_income_text, font=label_font, justify="right")
    spouse_income_label.grid(row=5, column=0, pady=5)

    spouse_income_amount = ttk.Label(main_frame4, text=formatted_spouse_income, relief="solid", padding=(5, 0, 5, 0))
    spouse_income_amount.grid(row=5, column=1)


    # back_btn = ttk.Button(main_frame, text="Back", command=go_back)
    # back_btn.grid(row=5, column=0, columnspan=2, pady=5)

    root.mainloop()


def monthly_financial_breakdown():
    """Calculate expense breakdown for selected year and month"""
    root = Tk()
    root.title("Monthly Expense Breakdown")

    main_frame = ttk.Frame(root, padding=10, width=950, height=300)
    main_frame.grid(row=0, column=0)

    main_frame2 = ttk.Frame(root, padding=10, width=950, height=300)
    main_frame2.grid(row=0, column=1)

    # main_frame3 = ttk.Frame(root, padding=10, width=950, height=300)
    # main_frame3.grid(row=1, column=0)
    #
    # main_frame4 = ttk.Frame(root, padding=10, width=950, height=300)
    # main_frame4.grid(row=1, column=1)

    # ****************************************************************************** #
    #                RETRIEVE DATA FROM DATABASE                                     #
    # ****************************************************************************** #

    # ============Expenses==========================
    expense_df = pd.read_sql_query("SELECT * from expense", db)
    expense_df.date = pd.to_datetime(expense_df.date)  # Convert date to Panda timestamp
    expense_df['year'] = pd.DatetimeIndex(expense_df['date']).year  # Create new Year column
    expense_df['month'] = pd.DatetimeIndex(expense_df['date']).month_name()  # Create new Month column
    # print(expense_df)

    # requested_year = chosen_year
    requested_year = 2021
    requested_month = "November"
    requested_year_expense = expense_df['year'] == requested_year
    requested_year_expense_df = expense_df[requested_year_expense]  # Create df of user requested year
    # print(requested_year_expense_df)
    requested_month_expense = requested_year_expense_df['month'] == requested_month
    requested_month_expense_df = requested_year_expense_df[requested_month_expense]  # Create df of requested month
    # print(requested_month_expense_df)

    expense_breakdown = requested_month_expense_df.groupby("category")["amount"].sum()  # Panda series
    expense_breakdown_df = pd.DataFrame(
        {"Category": expense_breakdown.index, "Amount": expense_breakdown.values})  # Convert series to dataframe
    print(expense_breakdown_df)

    category_column = expense_breakdown_df['Category']
    amount_column = expense_breakdown_df['Amount']

    category_list = []
    category_amount = []

    for item in category_column:
        category_list.append(item)

    for item in amount_column:
        category_amount.append(item)

    # print(category_list)
    # print(category_amount)

    # ****************************************************************************** #
    #                   CREATE EXPENSE PIE CHART                                     #
    # ****************************************************************************** #
    # fig, ax = plt.subplots()
    # ax.pie(category_amount, labels=category_list, shadow=False, startangle=90, autopct='%1.1f%%')
    # ax.axis('equal')
    # plt.title(f"{requested_year} Expense Breakdown")
    #
    # canvas = FigureCanvasTkAgg(fig, master=main_frame)
    # canvas.draw()
    # canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5)
    # # plt.show()
    # # plt.close()

    exp_amount = expense_breakdown_df["Amount"]
    expense_amount = []

    exp_category = expense_breakdown_df["Category"]
    expense_category = []

    for item in exp_category:
        expense_category.append(item)

    for item in exp_amount:
        expense_amount.append(item)
    # print(expense_amount)

    x = np.arange(len(expense_amount))  # label locations on chart
    width = 0.35  # width of bars

    fig, ax = plt.subplots(figsize=(10, 5))
    exp = ax.bar(x, expense_amount, width, label='Expenses')

    ax.set_ylabel("Amount($)")
    ax.set_title("Monthly Summary")
    ax.set_xticks(x)
    ax.set_xticklabels(expense_category, rotation=45, fontsize=8)
    ax.legend()

    ax.bar_label(exp, padding=2)

    plt.show()

    fig.tight_layout()





    root.mainloop()
monthly_financial_breakdown()




# TODO 1 Add back button
# TODO 2 Work on 3rd report (mth/yr breakdown)
