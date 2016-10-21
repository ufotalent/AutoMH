from future_task_manager import FutureTaskManager
from fixed_image import FixedImage
from screen import ScreenCapture
import time
class KeJuXiangShiAction:
    def name(self):
        return "kejuxiangshi"

    def buddy(self):
        return -1

    def timeout(self):
        return 600

    def handle(self, account):
        #if (not FutureTaskManager().get_task('kejuxiangshi', 1)):
        #    return
        time.sleep(5)
        while FixedImage().test('KJXSComplete') > 5:
            ScreenCapture().click(500, 400)
            time.sleep(3)
        FixedImage().dismiss('CloseKJXS')


