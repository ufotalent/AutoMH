import time
from screen import ScreenCapture
from fixed_image import FixedImage
from menu_manager import MenuManager
class BuddyManager:
    def __init__(self):
        self.current = -1
    def set(self, index):
        if self.current == index:
            return
        self.current = index
        MenuManager().open_menu(0)
        time.sleep(3)
        ScreenCapture().click(554, 178 * (index + 1))
        time.sleep(3)
        if FixedImage().test('CloseCommon') < 5:
            ScreenCapture().click(955, 110)
