import sqlite3
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

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
#     "deposit varchar(250),"
#     "withdraw varchar(250))"
# )

# cursor.execute(
#     "CREATE TABLE investments (date varchar(250),"
#     "deposit varchar(250),"
#     "withdraw varchar(250))"
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


def retrieve_expense():
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
    #
    # print(total_expense_df)
    # print("******************************************************")
    # print(total_income_df)
    # print("******************************************************")

    # ************** Merge income and expense dataframes ************************
    # merged_df_1 = pd.merge(total_expense_df, total_income_df, how="left")
    # print(merged_df_1)
    # print("******************************************************")

    combined_df = pd.merge(total_expense_df, total_income_df, how="outer")
    print(combined_df)

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

    # plt.bar(inc, inc)
    # plt.show()



# TODO 4: Create bar chart with income/expenses per year


retrieve_expense()
