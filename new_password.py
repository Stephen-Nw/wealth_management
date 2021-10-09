from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
from finance_database import retrieve_user_info, update_user_password
from random import choice
import werkzeug.security


def password_reset_details():
    root = Tk()
    root.title("Interprimos Wealth Management Solution")

    validate_question_asked = []
    validation_answer = []

    def ask_question():
        """Generate a form for user to validate his/her identity using challenge questions"""
        id_name = username_entry.get()
        user_db_info = retrieve_user_info(id_name)
        if not user_db_info:
            messagebox.showwarning(title="Oops!!", message="That user does not exist.")
            root.destroy()
        user_db_list = list(user_db_info[0])
        user_dict = {user_db_list[i]: user_db_list[i + 1] for i in range(0, len(user_db_list), 2)}

        key_list = list(user_dict.keys())
        challenge_questions = key_list[1:]
        user = key_list[0]
        print(f"User is {user}")

        random_question = choice(challenge_questions)
        validate_question_asked.append(random_question)
        validation_answer.append(user_dict[random_question])

        submit_button.destroy()
        username_entry.destroy()
        username_label.destroy()

        validate_user_question = ttk.Label(main_frame, text=random_question, padding=5)
        validate_user_question.grid(row=1, column=0)

        validate_user_password = StringVar()
        validate_user_password = ttk.Entry(main_frame, textvariable=validate_user_password, width=20, justify="left")
        validate_user_password.grid(row=2, column=0)
        validate_user_password.focus()

        blank1 = ttk.Label(main_frame, text=" ")
        blank1.grid(row=3, column=0)

        print(f"question = {validate_question_asked[0]}")
        print(f"answer = {validation_answer[0]}")

        reset_password = ttk.Button(main_frame, text="Submit",
                                    command=lambda: password_reset(validate_user_password.get(),
                                                                   validate_user_question,
                                                                   validate_user_password,
                                                                   blank1, reset_password, user))
        reset_password.grid(row=4, column=0)

    def password_reset(user_response, q_label, pw_label, blank_label, submit_btn, user):
        """Generate form for user to enter new password"""
        print(f"My response is {user_response}")
        print(f"Validate question is {validate_question_asked[0]}")
        print(f"validate answer is {validation_answer[0]}")
        if user_response != validation_answer[0]:
            messagebox.showwarning(title="Oops!!", message="That is incorrect!!")
        else:
            q_label.destroy()
            pw_label.destroy()
            blank_label.destroy()
            submit_btn.destroy()

            new_password_label = ttk.Label(main_frame, text="New Password")
            new_password_label.grid(row=1, column=0)

            new_password = StringVar()
            new_password = ttk.Entry(main_frame, textvariable=new_password, width=20, justify="left", show="*")
            new_password.grid(row=1, column=1)
            new_password.focus()

            blk1a = ttk.Label(main_frame, text=" ")
            blk1a.grid(row=2, column=0)

            blk1b = ttk.Label(main_frame, text=" ")
            blk1b.grid(row=2, column=1)

            reenter_password_label = ttk.Label(main_frame, text="Reenter Password")
            reenter_password_label.grid(row=3, column=0)

            reenter_password = StringVar()
            reenter_password = ttk.Entry(main_frame, textvariable=reenter_password, width=20, justify="left", show="*")
            reenter_password.grid(row=3, column=1)

            blk2a = ttk.Label(main_frame, text=" ")
            blk2a.grid(row=4, column=0)

            blk2b = ttk.Label(main_frame, text=" ")
            blk2b.grid(row=4, column=1)

            update_password = ttk.Button(main_frame, text="Submit",
                                         command=lambda: update_db(new_password.get(), reenter_password.get(), user))
            update_password.grid(row=5, column=0, columnspan=2)

    def update_db(pw1, pw2, user):
        """Update database with new user password"""
        if pw1 != pw2:
            messagebox.showwarning(title="Oops!!", message="Passwords do not match!!")
        else:
            updated_password = werkzeug.security.generate_password_hash(pw1,
                                                                        method='pbkdf2:sha256', salt_length=8)
            update_user_password(user, updated_password)

    app_name = "Password reset"
    title_font = Font(family="Helvetica", size=10, weight="bold", slant="italic")

    main_frame = ttk.Frame(root, padding=10, width=950, height=350)
    main_frame.grid(row=0, column=0)

    app_label = ttk.Label(main_frame, text=app_name, font=title_font, wraplength=280, anchor="center", padding=5)
    app_label.grid(row=0, column=0, columnspan=2)

    username_label = ttk.Label(main_frame, text="Enter Username ")
    username_label.grid(row=1, column=0)

    username = StringVar()
    username_entry = ttk.Entry(main_frame, textvariable=username, width=20, justify="left")
    username_entry.grid(row=1, column=1)
    username_entry.focus()
    username_entry.bind("<Return>", lambda event: ask_question())

    blank = ttk.Label(main_frame, text=" ")
    blank.grid(row=2, column=0)

    blank = ttk.Label(main_frame, text=" ")
    blank.grid(row=2, column=1)

    submit_button = ttk.Button(main_frame, text="Submit", command=ask_question)
    submit_button.grid(row=3, column=1, columnspan=2)

    root.mainloop()
