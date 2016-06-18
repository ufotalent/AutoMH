from screen import ScreenCapture
import time, json, PIL
import imageutil
from fixed_image import FixedImage
class ItemManager(object):
    _instance = None
    data_dir = 'item_image/'
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
            class_._instance.setup()
        return class_._instance

    def setup(self):
        self.data = {}
        manifest = json.load(open(self.data_dir + "manifest.json"))
        for item in manifest:
            info = Info()
            info.image = PIL.Image.open(self.data_dir + item['file'])
            info.policy = item['use']
            self.data[item['name']] = info

    def reset(self):
        ScreenCapture().click(850, 640)
        time.sleep(3)
        ScreenCapture().scroll(600, 300, 600, 600)
        ScreenCapture().scroll(600, 300, 600, 600)
        ScreenCapture().scroll(600, 300, 600, 600)
        time.sleep(3)
        self.calibrate()

    def open(self):
        ScreenCapture().click(975, 625)
        time.sleep(3)
        self.reset()

    def close(self):
        if FixedImage().test('CloseBaoGuo') < 5:
            ScreenCapture().click(930, 100)

    def calibrate(self):
        im = ScreenCapture().capture(bbox = [512, 202, 400, 400])
        self.offset = -1
        blank = False
        for y in range(400):
            cnt = 0
            for x in range(400):
                cnt += imageutil.diff_pixel(im.getpixel((x, y)), (222, 193, 155)) < 3
            if cnt > 200:
                blank = True
            else:
                if blank:
                    self.offset = y
                    return

    def get_item_pos(self, row, col):
        return (512 + 80 * col, 202 + self.offset + 80 * row)

    def get_item_image(self, row, col):
        pos = self.get_item_pos(row, col)
        return ScreenCapture().capture(bbox = [pos[0], pos[1], 80, 80])

    def get_item_name(self, row, col):
        im = self.get_item_image(row, col)
        for k in self.data:
            v = self.data[k]
            dis = imageutil.diff_image(v.image, im)
            if (dis < 20):
                return k
        return 'unknown'

    def next_page(self):
        a = self.get_item_pos(3, 1)
        b = self.get_item_pos(0, 1) 
        ScreenCapture().scroll(a[0], a[1] - 30, b[0], b[1])
        time.sleep(5)
        self.calibrate()

    def get_default_policy(self, name):
        return self.data[name].policy

class Info:
    pass
