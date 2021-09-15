from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
from finance_database import retrieve_user_info

root = Tk()
root.title("Interprimos Wealth Management Solution")


def ask_question():
    """Generate a form for user to validate his/her identity using challenge questions"""
    id_name = username_entry.get()
    a = retrieve_user_info(id_name)
    # a = retrieve_user_info()
    print(id_name)
    print(a)


app_name = "Password reset"
title_font = Font(family="Helvetica", size=10, weight="bold", slant="italic")

main_frame = ttk.Frame(root, padding=10, width=950, height=350)
main_frame.grid(row=0, column=0)

app_label = ttk.Label(main_frame, text=app_name, font=title_font, wraplength=280, anchor="center", padding=10)
app_label.grid(row=0, column=0, columnspan=2)

username_label = ttk.Label(main_frame, text="Enter Username ")
username_label.grid(row=1, column=0)

username = StringVar()
username_entry = ttk.Entry(main_frame, textvariable=username, width=20, justify="left")
username_entry.grid(row=1, column=1)
username_entry.focus()


blank = ttk.Label(main_frame, text=" ")
blank.grid(row=2, column=0)

blank = ttk.Label(main_frame, text=" ")
blank.grid(row=2, column=1)

submit_button = ttk.Button(main_frame, text="Submit", command=ask_question)
submit_button.grid(row=3, column=1, columnspan=2)
















root.mainloop()