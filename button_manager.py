import PIL
from screen import ScreenCapture
import imageutil
class ButtonManager(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
            class_._instance.setup()
        return class_._instance

    def setup(self):
        self.images = {}

    def test(self, name):
        if not name in self.images:
            self.images['name'] = PIL.Image.open('buttons/' + name + '.bmp')
        image = self.images['name']
        for y in range(105, 585, 60):
            dis = imageutil.diff_image(ScreenCapture().capture([750, y, 200, 40]), image)
            if dis < 5:
                return True

    def test_and_click(self, name):
        if not name in self.images:
            self.images['name'] = PIL.Image.open('buttons/' + name + '.bmp')
        image = self.images['name']
        for y in range(105, 585, 60):
            dis = imageutil.diff_image(ScreenCapture().capture([750, y, 200, 40]), image)
            if dis < 5:
                ScreenCapture().click(850, y + 20)
                return True
        return False
