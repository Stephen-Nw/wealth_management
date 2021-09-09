from tkinter import *
from tkinter import ttk
from tkinter.font import Font


root = Tk()
app_name = "Interprimos Wealth\nManagement Solution"
title_font = Font(family="Helvetica", size=10, weight="bold", slant="italic")

challenge_questions = [
    "What is your mother's maiden name?",
    "What is the name of your first pet?",
    "What is your favorite movie?",
    "What was your first car?",
    "Who is your best friend's name?",
    "What is your favorite food?",
]

main_frame = ttk.Frame(root, padding=10, width=950, height=350)
main_frame.grid(row=0, column=0)

app_label = ttk.Label(main_frame, text=app_name, font=title_font, wraplength=280, anchor="center", padding=10)
app_label.grid(row=0, column=0, columnspan=2)

username_label = ttk.Label(main_frame, text="Username")
username_label.grid(row=1, column=0)

username = StringVar()
username_entry = ttk.Entry(main_frame, textvariable=username, width=40, justify="left")
username_entry.grid(row=1, column=1)
username_entry.focus()

blank1a = ttk.Label(main_frame, text=" ")
blank1a.grid(row=2, column=0)

blank1b = ttk.Label(main_frame, text=" ")
blank1b.grid(row=2, column=1)

password_label = ttk.Label(main_frame, text="Password")
password_label.grid(row=3, column=0)

password = StringVar()
password_entry = ttk.Entry(main_frame, textvariable=password, width=40, justify="left")
password_entry.grid(row=3, column=1)

blank2a = ttk.Label(main_frame, text=" ")
blank2a.grid(row=4, column=0)

blank2b = ttk.Label(main_frame, text=" ")
blank2b.grid(row=4, column=1)

password_reentry_label = ttk.Label(main_frame, text="Re-enter Password  ",)
password_reentry_label.grid(row=5, column=0)

reenter_password = StringVar()
password_reentry = ttk.Entry(main_frame, textvariable=reenter_password, width=40, justify="left")
password_reentry.grid(row=5, column=1)

blank3a = ttk.Label(main_frame, text=" ")
blank3a.grid(row=6, column=0)

blank3b = ttk.Label(main_frame, text=" ")
blank3b.grid(row=6, column=1)

challenge_question1_label = ttk.Label(main_frame, text="Challenge Question")
challenge_question1_label.grid(row=7, column=0)

question1 = StringVar()
question1.set("Select a question below")
challenge_question1 = ttk.Combobox(main_frame, textvariable=question1, values=challenge_questions, state="readonly", width=37)
challenge_question1.grid(row=7, column=1)




root.mainloop()