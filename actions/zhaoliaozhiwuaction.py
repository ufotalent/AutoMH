from future_task_manager import FutureTaskManager
from fixed_image import FixedImage
from screen import ScreenCapture
import time
class ZhaoLiaoZhiWuAction:
    def name(self):
        return "zhaoliaozhiwu"

    def buddy(self):
        return -1

    def timeout(self):
        return 600

    def handle(self, account):
        if (not FutureTaskManager().get_task('zhaoliaozhiwu')):
            return
        ScreenCapture().sleep(30)
        ScreenCapture().click(800, 700)
        ScreenCapture().sleep(5)
        ScreenCapture().click(730, 470)
        ScreenCapture().sleep(5)
        ScreenCapture().click(640, 450)
        ScreenCapture().sleep(5)
        FixedImage().dismiss('CloseDali')
