from tkinter import *
from tkinter import ttk
from tkinter.font import Font

app_name = "Interprimos Wealth\nManagement Solution"

root = Tk()
root.title("Interprimos Wealth Management Solution")
main_frame = ttk.Frame(root, padding=10, width=950, height=350)
main_frame.grid(row=0, column=0)


# ==============FUNCTIONS =============================== #
def login():
    pass


def new_user_login(event):
    print("New User!!!")


def forgot_password_login(event):
    print("Forgot Password!!!!")


def change_new_user_color(event):
    new_user.config(foreground="purple")


def change_password_color(event):
    forgot_password.config(foreground="purple")


def restore_new_user_color(event):
    new_user.config(foreground="black")


def restore_password_color(event):
    forgot_password.config(foreground="black")


# ==============FONTS ================================= #
title_font = Font(family="Helvetica", size=10, weight="bold", slant="italic")
new_user_font = Font(family="Helvetica", size=8)
forgot_password_font = Font(family="Helvetica", size=8)


# =============UI DESIGN ============================== #

# ***********Login Page*******************************
app_label = ttk.Label(main_frame, text=app_name, font=title_font, wraplength=280, anchor="center", padding=10)
app_label.grid(row=0, column=0, columnspan=2)

username_label = ttk.Label(main_frame, text="Username")
username_label.grid(row=1, column=0)

username = StringVar()
username_entry = ttk.Entry(main_frame, textvariable=username, width=30, justify="left")
username_entry.grid(row=1, column=1)
username_entry.focus()

blank1 = ttk.Label(main_frame, text=" ")
blank1.grid(row=2, column=0)

blank2 = ttk.Label(main_frame, text=" ")
blank2.grid(row=2, column=1)

password_label = ttk.Label(main_frame, text="Password")
password_label.grid(row=3, column=0)

password = StringVar()
password_entry = ttk.Entry(main_frame, textvariable=password, width=30, justify="left")
password_entry.grid(row=3, column=1)

blank3 = ttk.Label(main_frame, text=" ")
blank3.grid(row=4, column=0)

blank3 = ttk.Label(main_frame, text=" ")
blank3.grid(row=4, column=1)

submit_button = ttk.Button(main_frame, text="Submit", command="login")
submit_button.grid(row=5, column=1)

new_user = Label(main_frame, text="New user", anchor='nw', font=new_user_font)
new_user.grid(row=6, column=0)
new_user.bind("<Button-1>", new_user_login)
new_user.bind("<Enter>", change_new_user_color)
new_user.bind("<Leave>", restore_new_user_color)

forgot_password = Label(main_frame, text="Forgot password", font=forgot_password_font)
forgot_password.grid(row=7, column=0)
forgot_password.bind("<Button-1>", forgot_password_login)
forgot_password.bind("<Enter>", change_password_color)
forgot_password.bind("<Leave>", restore_password_color)





root.mainloop()




