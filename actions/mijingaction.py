from future_task_manager import FutureTaskManager
from button_manager import ButtonManager
from screen import ScreenCapture
import imageutil
import time
import sets
class MiJingAction:
    def name(self):
        return "mijing"

    def buddy(self):
        return 1

    def handle(self):
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
        wait_time = 1800
        while time.time() < entry_time + wait_time:
            if ButtonManager().test('jrzd'):
                break;
            ScreenCapture().click(800, 250)
            time.sleep(30)
        ScreenCapture().click(40, 40)
        time.sleep(5)
        ScreenCapture().click(40, 40)
        time.sleep(5)
        ScreenCapture().click(500, 400)
        time.sleep(10)
