from team_checker import TeamChecker
from fixed_image import FixedImage
from screen import ScreenCapture
import time
class WaitSingleAction:
    def name(self):
        return "waitsingle"

    def buddy(self):
        return -1

    def timeout(self):
        return 1800

    def handle(self, account):
        while TeamChecker().members() >= 0:
            entry_time = time.time()
            while (time.time() < entry_time + 300):
                time.sleep(3)
                ScreenCapture().capture(bbox=[0, 0, 1, 1])

