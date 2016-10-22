from future_task_manager import FutureTaskManager
from text_image import TextImage
from screen import ScreenCapture
from button_manager import ButtonManager
from team_checker import TeamChecker
import time
class FengYaoAction:
    def name(self):
        return 'fengyao'

    def buddy(self):
        return 0

    def timeout(self):
        return 7200

    def handle(self, account):
        if (not account.single_fengyao) and TeamChecker().members() < 3:
            return
        while (FutureTaskManager().get_task('fengyao')):
            time.sleep(10)
            while True:
                pos = TextImage().find('fengyaotag', [100, 170, 650, 400])
                if pos is None:
                    continue
                ScreenCapture().click(pos[0] + 45, pos[1] - 70)
                wait_time = 15
                entry_time = time.time()
                while (time.time() < entry_time + wait_time):
                    if ButtonManager().test_and_click('jrzd'):
                        time.sleep(90)
                        break;
                break
