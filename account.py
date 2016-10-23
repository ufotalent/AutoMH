from actions.actions import get_action
import json
class Account:
    def __init__(self, j):
        self.user = j['user']
        self.actions = [get_action(name) for name in j['actions']]
        if 'enabled' in j:
            self.enabled = j['enabled']
        else:
            self.enabled = True
        if 'item_policy' in j:
            self.item_policy = j['item_policy']
        else:
            self.item_policy = {}
        if 'mijing_custom' in j:
            self.mijing_custom = j['mijing_custom']
        else:
            self.mijing_custom = []
        if 'single_fengyao' in j:
            self.single_fengyao = True
        else:
            self.single_fengyao = False
        self.json = j

class AccountManager:
    def __init__(self):
        j = json.load(open('account.json'))
        self.accounts = [Account(item) for item in j]

    def get_accounts(self):
        return self.accounts
