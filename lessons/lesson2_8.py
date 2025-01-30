import sqlite3

# A4 бумага
db = sqlite3.connect("UsersGrades.db")
# Это наша рука с ручкой
cursor = db.cursor()


def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (20) NOT NULL,
            age INTEGER NOT NULL,
            hoby TEXT
        )
                   """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            gradeid INTEGER PRIMARY KEY AUTOINCREMENT,
            userid INTEGER,
            subject VARCHAR (100) NOT NULL,
            grade INTEGER NOT NULL,
            FOREIGN KEY (userid) REFERENCES users(userid)
        )
                   """)
    db.commit()
    print("Таблицы созданы или обновлены")


create_tables()


def add_user(name, age, hoby):
    cursor.execute(
        'INSERT INTO users(name, age, hoby) VALUES (?,?,?)',
        (name, age, hoby)
    )
    db.commit()
    print(f"Добавили {name}")


# add_user("Ardager", 23, "спать")
# add_user("Loli", 23, "спать")
# add_user("John", 23, "спать")
# add_user("Mike", 23, "спать")


def add_grade_for_user(user_id, subject, grade):
    cursor.execute(
        'INSERT INTO grades(userid, subject, grade) VALUES (?,?,?)',
        (user_id, subject, grade)
    )
    db.commit()
    print(f"Добавили {subject} пользователю с id {user_id}")


add_grade_for_user(2, "Матем", 5)
add_grade_for_user(2, "Иностранный", 4)
add_grade_for_user(2, "Физика", 3)
add_grade_for_user(2, "ИЗО", 2)
add_grade_for_user(2, "ООП", 1)

