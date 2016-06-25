from button_manager import ButtonManager
from screen import ScreenCapture
from task_manager import TaskManager
from fixed_image import FixedImage
from future_task_manager import FutureTaskManager
from team_checker import TeamChecker
import time, sys
class ZhuaGuiAction:
    def name(self):
        return "zhuagui"

    def buddy(self):
        return 0

    def handle(self, account):
        if TeamChecker().members() < 3:
            return
        zhuagui_times = int(account.json['zhuagui_times'])
        if (FutureTaskManager().get_task('zhuaguirenwu')):
            time.sleep(30)
            for t in range(zhuagui_times):
                if not ButtonManager().test_and_click('zgrw'):
                    time.sleep(5)
                    return
                time.sleep(3)
                ScreenCapture().click(380, 445)
                time.sleep(5)
                while True:
                    if FixedImage().test('ZhuaGuiComplete') < 5:
                        ScreenCapture().click(600, 440)
                        time.sleep(5)
                        break
                    TaskManager().get_task('zhuagui')
                    time.sleep(30)


