import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from account import AccountManager
from buddy_manager import BuddyManager
from screen import ScreenCapture
from login import Login
from fixed_image import FixedImage
import time
am = AccountManager()
accounts = am.get_accounts()
current_user = None
#if not Login().should_login():
#    current_user = accounts[0].user
while True: 
    for account in accounts:
        if (len(sys.argv) > 1 and sys.argv[1] != account.user):
            continue
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
        current_user = account.user
        print 'User:',  account.user
        ScreenCapture().click(430, 30)
        time.sleep(3)
        ScreenCapture().click(100, 640)
        time.sleep(3)
        if FixedImage().test('CloseCommon') < 20:
            ScreenCapture().click(955, 110)
            time.sleep(3)
        for action in account.actions:
            print action.name()
            buddy.set(action.buddy())
            time.sleep(3)
            action.handle(account)
            time.sleep(3)
