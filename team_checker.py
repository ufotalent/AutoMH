from fixed_image import FixedImage
from screen import ScreenCapture
import time
class TeamChecker:
    def open(self):
        while FixedImage().test('WindowDW') > 5:
            ScreenCapture().click(940, 110)
            time.sleep(5)

    def members(self):
        self.open()
        if (FixedImage().test('CreateTeam') < 5):
            self.close()
            return -1
        members = 1
        for i in range(4):
            if (FixedImage().test('TeamMember%d' % (i + 1)) < 5):
                members = members + 1
        self.close()
        return members

    def kick_all(self):
        self.open()
        for i in range(4):
            ScreenCapture().click(300, 400)
            time.sleep(3)
            ScreenCapture().click(580, 580)
            time.sleep(3)
        if (FixedImage().test('CreateTeam') > 5):
            ScreenCapture().click(150, 640)
            time.sleep(3)
        self.close()

    def close(self):
        FixedImage().dismiss('CloseTeam') 
        time.sleep(3)
        if (FixedImage().test('TaskSimbol') > 5):
            ScreenCapture().click(830, 110)
        time.sleep(3)


