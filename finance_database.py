import sqlite3

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

def add_new_user(name, pword, q1, a1, q2, a2, q3, a3):
    cursor.execute("INSERT INTO user VALUES (:user, :password, :question_one, :answer_one, :question_two, "
                   ":answer_two, question_three, answer_three)", {"user": name, "password": pword, "question_one": q1,
                                                                  "answer_one": a1,
                                                                  "question_two": q2, "answer_two": a2,
                                                                  "question_three": q3, "answer_three": a3})
    db.commit()
