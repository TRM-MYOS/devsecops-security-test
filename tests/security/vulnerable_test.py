import sqlite3


def get_user(username):
    """Safely query a user using a parameterized SQL statement."""
    with sqlite3.connect("users.db") as conn:
        cursor = conn.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,),
        )
        return cursor.fetchall()


def main():
    username = "test_user"
    users = get_user(username)

    print(f"Users found: {len(users)}")


if __name__ == "__main__":
    main()