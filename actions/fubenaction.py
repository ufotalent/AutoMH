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
        self.do_handle(1, ['shengsibu', 'hunshimowang', 'tianpengxiafan'])
        # Turn this on later
        #self.do_handle(2, ['liangjieshan', 'chuqiqing', 'difusonggua', 'shuangchaling'])
    def do_handle(self, offset, tasks):
        while True:
            has_task = False
            for task in tasks:
                if FutureTaskManager().get_task(task):
                    has_task = True
                    break

            if not has_task:
                return
            time.sleep(15)
            if not ButtonManager().test_and_click('xzfb'):
                time.sleep(3)
                continue
            time.sleep(3)
            
            is_valid_fuben = False
            location = None
            for i in range(10086):
                img_name = 'PuTongFuBenName%d_%d' % (offset, (i + 1))
                if not FixedImage().has(img_name):
                    break
                if FixedImage().test(img_name) < 5:
                    is_valid_fuben = True
                    location = FixedImage().get(img_name).location
                    break
            if not is_valid_fuben:
                FixedImage().dismiss('CloseFuBen')
                return

            ScreenCapture().click(location[0] + location[2] / 2, 620)

            while FixedImage().test('ChanganCheng') > 5:
                if FixedImage().test('ButtonIndicator') < 5:
                    ScreenCapture().click(750, 540)
                    time.sleep(30)
                    continue
                ScreenCapture().click(850, 200)
                time.sleep(3)
            break
