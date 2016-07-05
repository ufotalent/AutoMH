from task_manager import TaskManager
from future_task_manager import FutureTaskManager
from button_manager import ButtonManager
from item_manager import ItemManager
from item_user import ItemUser
from screen import ScreenCapture
import time
class BaoTuAction:
    def name(self):
        return "baotu"

    def buddy(self):
        return 0

    def timeout(self):
        return 3600

    def handle(self, account):
        while True:
            res = TaskManager().get_task('baotu')
            if (res < 0 or res > 0):
                time.sleep(30)
                continue
            if not FutureTaskManager().get_task('baoturenwu'):
                break
            else:
                time.sleep(30)
                ButtonManager().test_and_click('ttwf')
                time.sleep(3)
        time.sleep(3)
        i = ItemManager()
        i.open()
        for page in range(3):
            if not page == 0:
                i.next_page()
            for y in range(4):
                if i.get_item_name(y, 0) == 'baotu':
                    pos = i.get_item_pos(y, 0)
                    ScreenCapture().double_click(pos[0] + 30, pos[1] + 30)

                    tick = 20
                    while tick > 0:
                        if ItemUser().test_and_use():
                            tick = 20
                        tick = tick - 1
                        print 'wabao tick:', tick
                        time.sleep(5)
                    return
            time.sleep(5)
        i.close()
