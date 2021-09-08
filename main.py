from tkinter import *
from tkinter import ttk
from tkinter.font import Font

app_name = "Interprimos Wealth Management Solution"

root = Tk()
root.title("Interprimos Wealth Management Solution")
main_frame = ttk.Frame(root, padding=10, width=950, height=350)
main_frame.grid(row=0, column=0)

# ==============FONTS ================================= #
title_font = Font(family="Helvetica", size=15, weight="bold", slant="italic")


# =============UI DESIGN ============================== #

# ***********Login Page*******************************
app_label = ttk.Label(main_frame, text=app_name, font=title_font, wraplength=350, anchor="center")
app_label.grid(row=0, column=0, columnspan=2)

username_label = ttk.Label(main_frame, text="Username")
username_label.grid(row=1, column=0)

username = StringVar()
username_entry = ttk.Entry(main_frame, textvariable=username, width=30, justify="left")
username_entry.grid(row=1, column=1)

blank1 = ttk.Label(main_frame, text=" ")
blank1.grid(row=2, column=0)

blank2 = ttk.Label(main_frame, text=" ")
blank2.grid(row=2, column=1)

password_label = ttk.Label(main_frame, text="Password")
password_label.grid(row=3, column=0)

password = StringVar()
password_entry = ttk.Entry(main_frame, textvariable=password, width=30, justify="left")
password_entry.grid(row=3, column=1)




root.mainloop()




