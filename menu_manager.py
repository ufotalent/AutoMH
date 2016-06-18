from fixed_image import FixedImage
from screen import ScreenCapture
import time
class MenuManager:
    def open_menu(self, index):
        while FixedImage().test('MenuPlus') > 5:
            time.sleep(3)
        ScreenCapture().click(980, 720)
        time.sleep(3)
        ScreenCapture().click(882 - index * 80, 715)
