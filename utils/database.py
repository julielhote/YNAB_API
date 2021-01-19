from .database_connection import DatabaseConnection

"""
Concerned with storing and retrieving information about your Budget
"""


def create_accounts_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS accounts(name text , type text, balance text)')


def add_account(name, type, balance):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'INSERT INTO accounts VALUES(?,?,?)', (name, type, balance))


def delete_account(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'DELETE FROM accounts WHERE name = ?', name)


def create_vacation_table():
    with DatabaseConnection('vacation_data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(""" CREATE TABLE IF NOT EXISTS vacation (location text PRIMARY KEY, date text,
        accommodation integer, food integer, fun integer, balance integer)
        """)


def fill_vacation_table(location, date, accommodation, food, fun, balance):
    with DatabaseConnection('vacation_data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'INSERT INTO vacation VALUES(?,?,?,?,?,?)', (location, date, accommodation, food, fun, balance))
