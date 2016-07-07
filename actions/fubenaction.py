from team_checker import TeamChecker
from future_task_manager import FutureTaskManager
from button_manager import ButtonManager
from screen import ScreenCapture
from fixed_image import FixedImage
import time
class FuBenAction:
    def name(self):
        return 'fuben'

    def buddy(self):
        return 0

    def timeout(self):
        return 3600

    def handle(self, account):
        if TeamChecker().members() < 3:
            return
        while True:
            if not FutureTaskManager().get_task('shengsibu') and not FutureTaskManager().get_task('hunshimowang') and not FutureTaskManager().get_task('tianpengxiafan'):
                return
            time.sleep(15)
            if not ButtonManager().test_and_click('xzfb'):
                time.sleep(3)
                continue
            time.sleep(3)
            
            is_valid_fuben = False
            for i in range(3):
                if FixedImage().test('PuTongFuBenName%d' % (i + 1)) < 5:
                    is_valid_fuben = True
                    break
            if not is_valid_fuben:
                if FixedImage().test('CloseFuBen') < 5:
                    ScreenCapture().click(880, 110)
                    time.sleep(3)
                    return

            ScreenCapture().click(350, 620)

            while FixedImage().test('Changan') > 5:
                if FixedImage().test('ButtonIndicator') < 5:
                    ScreenCapture().click(750, 540)
                    time.sleep(30)
                    continue
                ScreenCapture().click(850, 200)
                time.sleep(3)
            break
