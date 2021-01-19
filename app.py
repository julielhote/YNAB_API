from libs.ynab import YouNeedABudgetGET, YouNeedABudgetPOST
import json


HEADERS = {
    'accept': 'application/json',
    'Authorization': 'Bearer 6150d8165069c6696367b7c03fa24b141ced75ffe55e9b251c16969bcc7efb4e',
}

USER_INPUT = """ Enter:
- 'acc' to get a list of your accounts
- ('aacc' to add an account)
- 'lp' to get a list of all past payees
- 'lt' to list all transactions
- ('ct' to create a transaction)
- 'q' to quit
SELECT: """


def menu():
    user_input = input(USER_INPUT)
    while user_input != 'q':
        if user_input == 'acc':
            accounts_id_list()
        elif user_input == "aacc":
            add_account()
        elif user_input == 'lp':
            payees_id()
        elif user_input == 'lt':
            list_transactions()
        elif user_input == 'ct':
            create_transaction()
        else:
            print("Unknown command!")

        user_input = input(USER_INPUT)


# needs to be adjusted if more then one budget
def budget_id():
    list_budgets_ed = "/budgets"
    list_budgets = json.dumps(YouNeedABudgetGET(HEADERS, list_budgets_ed).latest())
    list_budgets_json = json.loads(list_budgets)
    # print(list_budgets_json['data']['budgets'][0]['id'])
    return list_budgets_json['data']['budgets'][0]['id']


def accounts_id_list():
    list_accounts_ed = f"/budgets/{budget_id()}/accounts"
    list_accounts = json.dumps(YouNeedABudgetGET(HEADERS, list_accounts_ed).latest())
    list_accounts_json = json.loads(list_accounts)

    length = len(list_accounts_json['data']['accounts'])
    for i in range(length):
        print(f"Account: {list_accounts_json['data']['accounts'][i]['name']} "
              f"ID: {list_accounts_json['data']['accounts'][i]['id']} "
              f"Balance: {list_accounts_json['data']['accounts'][i]['balance']/1000}")
    return None


def add_account():
    list_accounts_ed = f"/budgets/{budget_id()}/accounts"

    name = input("Enter the name of the account: ")
    type = input("Enter the type of the account: ")
    balance = input("Enter the current balance of the account: ")
    data = {
            "account": {
                "name": f"{name}",
                "type": f"{type}",
                "balance": balance
            }
     }
    create_transaction_url = YouNeedABudgetPOST(HEADERS, list_accounts_ed, data).latest()
    print(create_transaction_url)
    return None


def category_group_id_list():
    list_categories_ed = f"/budgets/{budget_id()}/categories"
    list_categories = json.dumps(YouNeedABudgetGET(HEADERS, list_categories_ed).latest())
    list_categories_json = json.loads(list_categories)

    print(list_categories_json)

    length = len(list_categories_json['data']['category_groups'])
    for i in range(length):
        print(f"Category + ID: {list_categories_json['data']['category_groups'][i]['name']} "
              f"{list_categories_json['data']['category_groups'][i]['id']}")
    return None


def payees_id():
    list_payees_ed = f"/budgets/{budget_id()}/payees"
    list_payees = json.dumps(YouNeedABudgetGET(HEADERS,list_payees_ed).latest())
    list_payees_json = json.loads(list_payees)

    length = len(list_payees_json['data']['payees'])
    for i in range(length):
        print(f"Payee: {list_payees_json['data']['payees'][i]['name']} "
              f"ID: {list_payees_json['data']['payees'][i]['id']}")
    return None


def list_transactions():
    list_transactions_ed = f"/budgets/{budget_id()}/transactions"
    list_transactions = json.dumps(YouNeedABudgetGET(HEADERS, list_transactions_ed).latest())
    list_transactions_json = json.loads(list_transactions)

    length = len(list_transactions_json['data']['transactions'])
    for i in range(length):
        print(f"ID: {list_transactions_json['data']['transactions'][i]['id']} "
              f"Date: {list_transactions_json['data']['transactions'][i]['date']} "
              f"Amount: {list_transactions_json['data']['transactions'][i]['amount']/1000} "
              f"Payee: {list_transactions_json['data']['transactions'][i]['payee_name']} "
              f"Approved: {list_transactions_json['data']['transactions'][i]['approved']}")
    return None


def create_transaction():
    list_transactions_ed = f"/budgets/{budget_id()}/transactions"

    accounts_id_list()
    account_id = input("Enter the account id: ")
    date = input("Enter the date of the transaction: ")
    amount = input("Enter the amount: ")
    payees_id()
    payee_id = input("Enter the payee's id: ")
    payee_name = input("Enter the payee's name: ")
    category_group_id_list()
    category_id = input("Enter the category id: ")

    data = {
              "transaction": {
                "account_id": f"{account_id}",
                "date": f"{date}",
                "amount": amount,
                "payee_id": f"{payee_id}",
                "payee_name": f"{payee_name}",
                "category_group_id_list": f"{category_id}",
                "memo": " ",
                "cleared": "cleared",
                "approved": True,
                }
    }
    create_transaction_url = YouNeedABudgetPOST(HEADERS, list_transactions_ed, data).latest()
    print(create_transaction_url)
    return None


menu()
