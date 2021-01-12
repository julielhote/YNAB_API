from libs.ynab import YouNeedABudget
from utils import database
import json


HEADERS = {
    'accept': 'application/json',
    'Authorization': 'Bearer 6150d8165069c6696367b7c03fa24b141ced75ffe55e9b251c16969bcc7efb4e',
}

USER_INPUT = """ Enter:
- 'add acc' to add an account: """


def menu():
    database.create_accounts_table()
    user_input = input(USER_INPUT)
    if user_input == 'add acc':
        prompt_add_account()
    else:
        print("Unknown command!")


def prompt_add_account():
    list_budgets_ed = "/budgets"
    list_budgets = json.dumps(YouNeedABudget(HEADERS, list_budgets_ed).latest())
    list_budgets_json = json.loads(list_budgets)

    get_all_accounts_ed = f"/budgets/{list_budgets_json['data']['budgets'][0]['id']}/accounts"
    get_all_accounts = json.dumps(YouNeedABudget(HEADERS, get_all_accounts_ed).latest())
    all_accounts_json = json.loads(get_all_accounts)

    length = len(all_accounts_json['data']['accounts'])
    for i in range(length):
        account_name = all_accounts_json['data']['accounts'][i]['name']
        account_type = all_accounts_json['data']['accounts'][i]['type']
        account_balance = all_accounts_json['data']['accounts'][i]['balance']
        database.add_account(account_name, account_type, account_balance)


menu()
