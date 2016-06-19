import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import time
from login import Login
from screen import ScreenCapture
from fixed_image import FixedImage
from text_image import TextImage
from future_task_manager import FutureTaskManager
from item_manager import ItemManager
from actions.mijingaction import MiJingAction
from actions.yunbiaoaction import YunBiaoAction
from actions.cleanupaction import CleanUpAction
from account import AccountManager

#print TextImage().find('shimen', [810, 150, 45, 250])
#FutureTaskManager().get_task('mijingxiangyao')

#i = ItemManager()
#i.calibrate()
#for p in range(3):
#    for y in range(4):
#        for x in range(5):
#            print i.get_item_name(y, x)
#    i.next_page()

#ScreenCapture().double_click(550, 400)
account = AccountManager().get_accounts()[1]
MiJingAction().handle(account)

