import time, imageutil, sys
from problem_set import ProblemSet
from screen import ScreenCapture
from fixed_image import FixedImage
from future_task_manager import FutureTaskManager
class SanJieQiYuanAction:
    def __init__(self):
        self.problem_set = ProblemSet('sanjieqiyuan')

    def name(self):
        return "sanjieqiyuan"

    def buddy(self):
        return 0

    def timeout(self):
        return 1200

    def handle(self, account):
        if (not FutureTaskManager().get_task('sanjieqiyuan', 1)):
            return
        time.sleep(5)
        while True:
            if (FixedImage().test('SJQYComplete') < 5):
                ScreenCapture().click(950, 100)
                time.sleep(3)
                return
            time.sleep(5)
            px = 490
            if FixedImage().test('SJQYColon') < 5:
                px = px + 11
            p = ScreenCapture().capture([px, 140, 450, 40])
            a = self.problem_set.query(p)
            done = False
            if (len(a) > 0):
                print 'get %d answers' % len(a)
                for x in range(3):
                    for offset in range(0, 9):
                        now = ScreenCapture().capture([offset % 3 - 1 + 375 + 194 * x, offset / 3 - 1 + 340, 164, 40])
                        for aa in a:
                            print imageutil.diff_image(now, aa)
                            if imageutil.diff_image(now, aa) < 5:
                                ScreenCapture().click(450 + 194 * x, 340)
                                done = True
                                break
                        if done:
                            break
                    if done:
                        break
            if not done:
                print 'will guess'
                hint = int(time.time()) % 3
                candidate = ScreenCapture().capture([375 + hint * 194, 340, 164, 40])
                ScreenCapture().click(450 + 194 * hint, 340)
                time.sleep(1)
                pixel = ScreenCapture().capture([514 + hint * 194, 424, 1, 1]).getpixel((0, 0))
                if (pixel[2] < 10):
                    print 'guess currect!'
                    if not '--slave' in sys.argv:
                        self.problem_set.add(p, candidate)
