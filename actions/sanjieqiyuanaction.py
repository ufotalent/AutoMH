import time, imageutil
from problem_set import ProblemSet
from screen import ScreenCapture
class SanJieQiYuanAction:
    def __init__(self):
        self.problem_set = ProblemSet('sanjieqiyuan')

    def name(self):
        return "sanjieqiyuan"

    def buddy(self):
        return 0

    def timeout(self):
        return 600

    def handle(self, account):
        while True:
            time.sleep(5)
            p = ScreenCapture().capture([490, 140, 450, 40])
            a = self.problem_set.query(p)
            if (not a is None):
                done = False
                for x in range(3):
                    now = ScreenCapture().capture([360 + 194 * x, 340, 194, 40])
                    if imageutil.diff_image(now, a) < 5:
                        ScreenCapture().click(450 + 194 * x, 340)
                        done = True
                        break
                if not done:
                    raise 'abc'
                    print 'can\'t find result!'
                    ScreenCapture().click(450 , 340)
            else:
                candidate = ScreenCapture().capture([360, 340, 194, 40])
                ScreenCapture().click(450, 340)
                time.sleep(1)
                pixel = ScreenCapture().capture([514, 424, 1, 1]).getpixel((0, 0))
                if (pixel[2] < 10):
                    print 'guess currect!'
                    self.problem_set.add(p, candidate)
