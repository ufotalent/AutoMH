import sys, os, time
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from button_manager import ButtonManager
from screen import ScreenCapture
from task_manager import TaskManager
from fixed_image import FixedImage
from actions.actions import get_action
for i in range(int(sys.argv[1])):
    while not ButtonManager().test_and_click('zgrw'):
        time.sleep(5)
    time.sleep(3)
    ScreenCapture().click(380, 445)
    time.sleep(5)
    while True:
        if FixedImage().test('ZhuaGuiComplete') < 5:
            ScreenCapture().click(600, 440)
            time.sleep(5)
            break
        TaskManager().get_task('zhuagui')
        time.sleep(30)

get_action('kickall').handle(None)
