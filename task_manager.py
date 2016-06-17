from fixed_image import FixedImage
from screen import ScreenCapture
from text_image import TextImage
class TaskManager:
    def get_task(self, name):
        img = ScreenCapture().capture()
        if FixedImage().test('TaskSimbol', img) > 5:
            return -1
        pos = TextImage().find(name, [810, 150, 45, 250], img)
        if (pos is None):
            return 0
        ScreenCapture().click(pos[0] + 10, pos[1] + 10)
        return 1

