from tkinter import *
from tkinter import ttk
from tkinter.font import Font


root = Tk()
app_name = "Interprimos Wealth\nManagement Solution"
title_font = Font(family="Helvetica", size=10, weight="bold", slant="italic")


def get_question1(event):
    print(challenge_question1.get())


def get_question2(event):
    print(challenge_question2.get())


def create_user():
    print("New User has been created!!!")


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

username_label = ttk.Label(main_frame, text="Enter Username")
username_label.grid(row=1, column=0)

username = StringVar()
username_entry = ttk.Entry(main_frame, textvariable=username, width=40, justify="left")
username_entry.grid(row=1, column=1)
username_entry.focus()

blank1a = ttk.Label(main_frame, text=" ")
blank1a.grid(row=2, column=0)

blank1b = ttk.Label(main_frame, text=" ")
blank1b.grid(row=2, column=1)

password_label = ttk.Label(main_frame, text="Enter Password")
password_label.grid(row=3, column=0)

password = StringVar()
password_entry = ttk.Entry(main_frame, textvariable=password, width=40, justify="left", show="*")
password_entry.grid(row=3, column=1)

blank2a = ttk.Label(main_frame, text=" ")
blank2a.grid(row=4, column=0)

blank2b = ttk.Label(main_frame, text=" ")
blank2b.grid(row=4, column=1)

password_reentry_label = ttk.Label(main_frame, text="Re-enter Password  ")
password_reentry_label.grid(row=5, column=0)

reenter_password = StringVar()
password_reentry = ttk.Entry(main_frame, textvariable=reenter_password, width=40, justify="left", show="*")
password_reentry.grid(row=5, column=1)

blank3a = ttk.Label(main_frame, text=" ")
blank3a.grid(row=6, column=0)

blank3b = ttk.Label(main_frame, text=" ")
blank3b.grid(row=6, column=1)

challenge_question1_label = ttk.Label(main_frame, text="Challenge Question")
challenge_question1_label.grid(row=7, column=0)

question1 = StringVar()
question1.set("Select one of the questions below")
challenge_question1 = ttk.Combobox(main_frame, textvariable=question1, values=challenge_questions, state="readonly",
                                   width=37)
challenge_question1.grid(row=7, column=1)
challenge_question1.bind("<<ComboboxSelected>>", get_question1)

blank4a = ttk.Label(main_frame, text=" ")
blank4a.grid(row=8, column=0)

blank4b = ttk.Label(main_frame, text=" ")
blank4b.grid(row=8, column=1)

answer_one_label = ttk.Label(main_frame, text="Challenge Answer",)
answer_one_label.grid(row=9, column=0)

challenge_answer1 = StringVar()
answer_one = ttk.Entry(main_frame, textvariable=challenge_answer1, width=40, justify="left")
answer_one.grid(row=9, column=1)

blank5a = ttk.Label(main_frame, text=" ")
blank5a.grid(row=10, column=0)

blank5b = ttk.Label(main_frame, text=" ")
blank5b.grid(row=10, column=1)

challenge_question2_label = ttk.Label(main_frame, text="Challenge Question  ")
challenge_question2_label.grid(row=11, column=0)

question2 = StringVar()
question2.set("Select one of the questions below")
challenge_question2 = ttk.Combobox(main_frame, textvariable=question2, values=challenge_questions, state="readonly",
                                   width=37)
challenge_question2.grid(row=11, column=1)
challenge_question2.bind("<<ComboboxSelected>>", get_question2)

blank6a = ttk.Label(main_frame, text=" ")
blank6a.grid(row=12, column=0)

blank6b = ttk.Label(main_frame, text=" ")
blank6b.grid(row=12, column=1)

answer_two_label = ttk.Label(main_frame, text="Challenge Answer",)
answer_two_label.grid(row=13, column=0)

challenge_answer2 = StringVar()
answer_two = ttk.Entry(main_frame, textvariable=challenge_answer2, width=40, justify="left")
answer_two.grid(row=13, column=1)

blank7a = ttk.Label(main_frame, text=" ")
blank7a.grid(row=14, column=0)

blank7b = ttk.Label(main_frame, text=" ")
blank7b.grid(row=14, column=1)

challenge_question3_label = ttk.Label(main_frame, text="Challenge Question  ")
challenge_question3_label.grid(row=15, column=0)

question3 = StringVar()
question3.set("Select one of the questions below")
challenge_question3 = ttk.Combobox(main_frame, textvariable=question3, values=challenge_questions, state="readonly",
                                   width=37)
challenge_question3.grid(row=15, column=1)
challenge_question3.bind("<<ComboboxSelected>>", get_question2)

blank8a = ttk.Label(main_frame, text=" ")
blank8a.grid(row=16, column=0)

blank8b = ttk.Label(main_frame, text=" ")
blank8b.grid(row=16, column=1)

answer_three_label = ttk.Label(main_frame, text="Challenge Answer",)
answer_three_label.grid(row=17, column=0)

challenge_answer3 = StringVar()
answer_three = ttk.Entry(main_frame, textvariable=challenge_answer3, width=40, justify="left")
answer_three.grid(row=17, column=1)

blank9a = ttk.Label(main_frame, text=" ")
blank9a.grid(row=18, column=0)

blank9b = ttk.Label(main_frame, text=" ")
blank9b.grid(row=18, column=1)

submit_button = ttk.Button(main_frame, text="Create User", command=create_user)
submit_button.grid(row=19, column=0, columnspan=2)







root.mainloop()