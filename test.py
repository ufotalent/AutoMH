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
from actions.fengyaoaction import FengYaoAction
from actions.fubenaction import FuBenAction
from actions.sanjieqiyuanaction import SanJieQiYuanAction
from account import AccountManager
from menu_manager import MenuManager
from team_checker import TeamChecker

#print TextImage().find('shimen', [810, 150, 45, 250])
#FutureTaskManager().get_task('mijingxiangyao')

#i = ItemManager()
#i.calibrate()
#for p in range(3):
#    for y in range(4):
#        for x in range(5):
#            print i.get_item_name(y, x)
#    i.next_page()

#FutureTaskManager().get_task('sanjieqiyuan', 1)
SanJieQiYuanAction().handle(None)
#account = AccountManager().get_accounts()[0]
#FuBenAction().handle(account)
#FutureTaskManager().get_task('zhuaguirenwu')
#print TeamChecker().members()
#TeamChecker().kick_all()
#while True:
#    ScreenCapture().click(900, 300)
#    time.sleep(1)
#    ScreenCapture().click(450, 600)
#    time.sleep(1)

#MenuManager().open_menu(4)
#FuBenAction().handle(None)

#TextImage().find('fengyaotag', [0, 0, 1024, 768])
