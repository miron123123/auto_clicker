import sqlite3
from time import sleep

def thread_log_main_run():

    connection = sqlite3.connect('logs.db')
    cursor = connection.cursor()


    cursor.execute('''CREATE TABLE IF NOT EXISTS user_logs(
    id INTEGER PRIMARY KEY,
    time INTEGER,
     REAL
    )
                   ''')