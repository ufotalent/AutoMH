from fixed_image import FixedImage
from screen import ScreenCapture
import time
class TeamChecker:
    def open(self):
        res = None
        while True:
            res = ScreenCapture().capture()
            if FixedImage().test('WindowDW', res) < 5:
                break
            ScreenCapture().click(940, 110)
            time.sleep(5)
        ScreenCapture().click(160, 160)
        time.sleep(3)
        return res

    def members(self):
        screen = self.open()
        if (FixedImage().test('CreateTeam', screen) < 5):
            self.close()
            return -1
        members = 1
        for i in range(4):
            if (FixedImage().test('TeamMember%d' % (i + 1), screen) < 5):
                members = members + 1
        if members == 1:
            while (FixedImage().test('CreateTeam') > 5):
                ScreenCapture().click(200, 640)
                time.sleep(3)
            members = -1
        self.close()
        return members

    def kick_all(self):
        r = self.open()
        if (FixedImage().test('Yijianhanhua', r) > 5):
            self.close()
            return
        for i in range(4):
            ScreenCapture().click(300, 400)
            time.sleep(3)
            ScreenCapture().click(580, 580)
            time.sleep(3)
        while (FixedImage().test('CreateTeam') > 5):
            ScreenCapture().click(200, 640)
            time.sleep(3)
        self.close()

    def close(self):
        FixedImage().dismiss('CloseTeam') 
        time.sleep(3)
        if (FixedImage().test('TaskSimbol') > 5):
            ScreenCapture().click(830, 110)
        time.sleep(3)


