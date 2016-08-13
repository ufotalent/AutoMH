from future_task_manager import FutureTaskManager
from button_manager import ButtonManager
from screen import ScreenCapture
from fixed_image import FixedImage
import imageutil
import time
import sets
class MiJingAction:
    def name(self):
        return "mijing"

    def buddy(self):
        return 1

    def timeout(self):
        return 3600

    def handle(self, account):
        if not FutureTaskManager().get_task('mijingxiangyao'):
            return 
        while not ButtonManager().test_and_click('mjxy'):
            time.sleep(3)
        time.sleep(5)
        last = ScreenCapture().capture([100, 200, 800, 450])
        avgx = 0
        avgy = 0
        cnt = 0
        while cnt < 50000:
            time.sleep(1)
            now = ScreenCapture().capture([100, 200, 800, 450])
            diff_points = imageutil.diff_points(now, last)
            last = now
            print 'diff points:', len(diff_points)
            if (len(diff_points) > 10000):
                continue
            for point in diff_points:
                avgx += point[0]
                avgy += point[1]
                cnt = cnt + 1
        ScreenCapture().click(100 + avgx / cnt, 200 + avgy / cnt)
        time.sleep(5)
        ScreenCapture().click(550, 520)

        entry_time = time.time()
        wait_time = 3600
        while time.time() < entry_time + wait_time:
            if ButtonManager().test('jrzd'):
                have = False
                for i in range(100):
                    name = 'MiJingWhitelist%d' % i
                    if not FixedImage().has(name):
                        break
                    if FixedImage().test(name) < 5:
                        have = True
                        break
                if have:
                    ButtonManager().test_and_click('jrzd')
                    time.sleep(30)
                    continue
                else:
                    break
            if FixedImage().test('Failure') < 10:
                ScreenCapture().click(512, 600)
                break;
            ScreenCapture().click(800, 250)
            time.sleep(30)
        ScreenCapture().click(40, 40)
        time.sleep(5)
        ScreenCapture().click(40, 40)
        time.sleep(5)
        ScreenCapture().click(500, 400)
        time.sleep(10)
