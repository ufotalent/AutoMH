from button_manager import ButtonManager
from screen import ScreenCapture
from task_manager import TaskManager
from fixed_image import FixedImage
import time, sys
for i in range(int(sys.argv[1])):
    while not ButtonManager().test_and_click('zgrw'):
        time.sleep(5)
    ScreenCapture().click(380, 445)
    time.sleep(5)
    while True:
        if FixedImage().test('ZhuaGuiComplete') < 5:
            ScreenCapture().click(600, 440)
            time.sleep(5)
            break
        TaskManager().get_task('zhuagui')
        time.sleep(30)


