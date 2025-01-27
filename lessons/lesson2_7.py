import sqlite3

db = sqlite3.connect("Users.db")
cursor = db.cursor()

def create_table():
    cursor.execute("DROP TABLE IF EXISTS users")  # Удаляем таблицу, если она существует
    cursor.execute("""
        CREATE TABLE users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(20) NOT NULL,
            age INTEGER NOT NULL,
            hoby TEXT
        )
    """)
    db.commit()


create_table()

def add_user(name, age, hoby):
    cursor.execute(
        'INSERT INTO users(name, age, hoby) VALUES (?, ?, ?)',
        (name, age, hoby)
    )
    db.commit()
    print(f"Добавили {name}")


add_user("Ardager", 23, "спать")
add_user("Loli", 23, "спать")
add_user("John", 23, "спать")
add_user("Mike", 23, "спать")


def detail_view_user_by_id(user_id):
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    if user:
        print(f"Найден пользователь: ID={user[0]}, Name={user[1]}, Age={user[2]}, Hobby={user[3]}")
    else:
        print(f"Пользователь с ID {user_id} не найден.")


def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    if users:
        print("Список всех пользователей:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}, Hobby: {user[3]}")
    else:
        print("Список пользователей пуст.")


detail_view_user_by_id(3)
get_all_users()

db.close()
