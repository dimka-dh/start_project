import sqlite3


def initiate_db():
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    """)
    connection.commit()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
    """)
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, description, price FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products


# Добавление примеров продуктов однократно!!
def add_products():
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    products = [
        ("Звездочка как в детстве", "знакомый запах", 100),
        ("Звездочка для тех кто постарше", "Соответственно и подороже", 300),
        ("Звездочка тройного действия", "Вроде настоящая въетнамская", 500),
        ("Уголек из АДА", "Никогда бы не подумали что так может обжигать", 1000),
    ]
    cursor.executemany("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", products)
    connection.commit()
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)
    """, (username, email, age))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM Users WHERE username = ?", (username,))
    result = cursor.fetchone()
    connection.close()
    return result is not None


def get_all_users():
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id, username, email, age, balance FROM Users")
    users = cursor.fetchall()
    connection.close()
    return users


if __name__ == "__main__":
    initiate_db()
    add_products()  # Запускайте только один раз
