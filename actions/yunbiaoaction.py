from future_task_manager import FutureTaskManager
from button_manager import ButtonManager
from screen import ScreenCapture
from fixed_image import FixedImage
import imageutil
import time
import sets
class YunBiaoAction:
    def name(self):
        return "yunbiao"

    def buddy(self):
        return 0

    def handle(self):
        while FutureTaskManager().get_task('yunbiao'):
            while not ButtonManager().test_and_click('ysptby'):
                time.sleep(3)
            time.sleep(3)
            ScreenCapture().click(600, 435)
            tick = 3
            while tick > 0:
                if (FixedImage().test('LogedInIndicator') < 5):
                    tick = tick - 1
                else:
                    tick = 3
                print 'yunbiao tick', tick
                time.sleep(5)
            ScreenCapture().click(512, 376)
            time.sleep(3)

