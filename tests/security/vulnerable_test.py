import os
import subprocess
import sqlite3


def command_injection(user_input):
    subprocess.call(user_input, shell=True)


def insecure_os_command(user_input):
    os.system(user_input)


def sql_injection(username):
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return conn.execute(query).fetchall()