from future_task_manager import FutureTaskManager
from button_manager import ButtonManager
from fixed_image import FixedImage
from screen import ScreenCapture
import time

class JingJiChangAction:
    def name(self):
        return "jingjichang"

    def buddy(self):
        return 2

    def timeout(self):
        return 3600

    def handle(self, account):
        while True:
            if not FutureTaskManager().get_task('jingjichang', 1) and not FutureTaskManager().get_task('hunluanjingjichang', 1):
                return
            done = False
            for i in range(10):
                if ButtonManager().test_and_click('swqsc'):
                    done = True
                    break
                else:
                    time.sleep(5)
            if done:
                break
        time.sleep(30)

        while FixedImage().test('ChanganCheng') > 5:
            FixedImage().dismiss('JingjichangMiddle')
            time.sleep(5)
            ScreenCapture().click(570, 500)
            time.sleep(5)
            ScreenCapture().click(770, 500)
            time.sleep(5)
            if FixedImage().test('JingjichangStart') < 5:
                ScreenCapture().click(880, 600)
            time.sleep(5)
