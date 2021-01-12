from .database_connection import DatabaseConnection

"""
Concerned with storing and retrieving information about your Budget
"""


def create_accounts_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS accounts(name text, type text, balance text)')


def add_account(name, type, balance):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'INSERT OR REPLACE INTO accounts VALUES(?,?,?)', (name, type, balance))


def delete_account(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'DELETE FROM accounts WHERE name = ?', name)
