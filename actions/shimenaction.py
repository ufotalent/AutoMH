import time
from text_image import TextImage
from task_manager import TaskManager
from fixed_image import FixedImage
from screen import ScreenCapture
from item_user import ItemUser
from button_manager import ButtonManager
class ShiMenAction:
    def name(self):
        return "shimen"

    def buddy(self):
        return 0

    def timeout(self):
        return 3600

    def handle(self, account):
        self.status = 'start'
        self.run()


    def run(self):
        while not self.status == 'stop':
            print 'shimen status:', self.status
            call = getattr(ShiMenAction, self.status)
            call(self)
            time.sleep(5)

    def start(self):
        for i in range(3):
            ret = TaskManager().get_task('shimen')
            if not ret == 0:
                self.status = 'wait'
                return
            time.sleep(3)
        self.status = 'stop'

    def wait(self):
        entry_time = time.time()
        wait_time = 5 
        while time.time() < entry_time + wait_time:
            if (FixedImage().test('WindowGMCW')) < 5:
                time.sleep(3)
                ScreenCapture().click(850, 650)
                time.sleep(3)
                self.status = 'start'
                return
            if (FixedImage().test('WindowBT')) < 5:
                ScreenCapture().click(400, 250)
                time.sleep(1)
                ScreenCapture().click(850, 650)
                time.sleep(3)
                self.status = 'start'
                return
            if (FixedImage().test('WindowRWCWXZ')) < 5:
                time.sleep(3)
                ScreenCapture().click(680, 580)
                time.sleep(3)
                self.status = 'start'
                return
            if (FixedImage().test('WindowRWWPXZ')) < 5:
                time.sleep(3)
                ScreenCapture().click(780, 580)
                time.sleep(3)
                self.status = 'start'
                return
            if (FixedImage().test('WindowYD')) < 5:
                time.sleep(3)
                ScreenCapture().click(780, 580)
                time.sleep(3)
                self.status = 'start'
                return
            if (FixedImage().test('WindowBQP')) < 5:
                time.sleep(3)
                ScreenCapture().click(780, 580)
                time.sleep(3)
                self.status = 'start'
                return
            if ItemUser().test_and_use():
                time.sleep(3)
                self.status = 'start'
                return
            if (ButtonManager().test_and_click('smrw')):
                time.sleep(3)
                self.status = 'start'
                return
            time.sleep(3)
        self.status = 'start'
