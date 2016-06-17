from actions.actions import get_action
import json
class Account:
    def __init__(self, j):
        self.user = j['user']
        self.actions = [get_action(name) for name in j['actions']]

class AccountManager:
    def __init__(self):
        j = json.load(open('account.json'))
        self.accounts = [Account(item) for item in j]

    def get_accounts(self):
        return self.accounts
