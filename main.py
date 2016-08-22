import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from account import AccountManager
from buddy_manager import BuddyManager
from screen import ScreenCapture
from login import Login
from fixed_image import FixedImage
from interceptor import MonitorInterceptor
import time
am = AccountManager()
accounts = am.get_accounts()
current_user = None
#if not Login().should_login():
#    current_user = accounts[0].user

def run_account(account):
    global current_user
    try:
        if (len(sys.argv) > 1 and not account.user in sys.argv):
            return True
        buddy = BuddyManager()
        if Login().should_login():
            print "login user:", account.user
            Login().login(account.user)
        else:
            if current_user != None and current_user != account.user:
                Login().logout()
                print "login user:", account.user
                Login().login(account.user)
            time.sleep(3)
        MonitorInterceptor.deadline = time.time() + 3600
        current_user = account.user
        print 'User:',  account.user
        ScreenCapture().reset()
        FixedImage().dismissAll()
        ScreenCapture().click(430, 30)
        time.sleep(3)
        ScreenCapture().click(100, 640)
        time.sleep(3)
        for x in range(10):
            ScreenCapture().click(850, 640)
            time.sleep(1)
        time.sleep(40)
        if FixedImage().test('CloseCommon') < 20:
            ScreenCapture().click(955, 110)
            time.sleep(3)

        for action in account.actions:
            print action.name()
            MonitorInterceptor.deadline = time.time() + 120
            if (action.buddy() >= 0):
                buddy.set(action.buddy())
            time.sleep(3)
            MonitorInterceptor.deadline = time.time() + action.timeout()
            action.handle(account)
            time.sleep(3)
            MonitorInterceptor.deadline = time.time() + 100000000
    except RuntimeError as e:
        MonitorInterceptor.deadline = time.time() + 100000000
        print e
        return False
    return True

while True: 
    for account in accounts:
        if not account.enabled:
            continue
        while not run_account(account):
            time.sleep(10)
