from future_task_manager import FutureTaskManager
from button_manager import ButtonManager
from screen import ScreenCapture
from fixed_image import FixedImage
from menu_manager import MenuManager
from item_manager import ItemManager
from item_user import ItemUser
import imageutil, requests
import time
import sets
class BianShenKaAction:
    def name(self):
        return "bianshenka"

    def buddy(self):
        return -1

    def timeout(self):
        return 1800

    def handle(self, account):
        ScreenCapture().click(50, 200)
        ScreenCapture().sleep(5)
        ScreenCapture().click(970, 370)
        ScreenCapture().sleep(5)
        ScreenCapture().click(150, 150)
        ScreenCapture().sleep(5)
        for i in range(3):
            ScreenCapture().scroll(200, 560, 200, 100)
        ScreenCapture().sleep(3)
        fenlei = [[700, 400], [500, 500], [700, 500]]
        for i in range(3):
            ScreenCapture().click(150, 490)
            ScreenCapture().sleep(5)
            if FixedImage().test('BianShenKa') > 5:
                break
            ScreenCapture().click(fenlei[i][0], fenlei[i][1])
            ScreenCapture().sleep(5)
            for j in range(8):
                ScreenCapture().click(700, 150)
                ScreenCapture().sleep(1)
                ScreenCapture().scroll(700, 400, 700, 100)
                ScreenCapture().sleep(1)
                ScreenCapture().click(670 + (j % 2) * 100, 220 + (j / 2) * 70)
                ScreenCapture().sleep(10)
                if FixedImage().test('BaitanYiye') < 5:
                    self.report(i, j, 'YES')
                else:
                    self.report(i, j, 'NO')
        FixedImage().dismiss('CloseBaoGuo')

    def report(self, a, b, state):
        try:
            requests.get('http://my.ufotalent.me/bsk/%d/%d/%s' % (a, b, state))
        except Exception as e:
            print e

