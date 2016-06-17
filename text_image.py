import json, time
import PIL
from screen import ScreenCapture
import imageutil


class TextImage(object):
    _instance = None
    data_dir = 'text_image/'
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
            info.color = item['color']
            self.data[item['name']] = info

            

    def find(self, name, bbox, screen = None):
        # return absolute position
        im = None
        if screen == None:
            im = ScreenCapture().capture(bbox)
        else:
            b = bbox
            im = screen.crop([b[0], b[1], b[0] + b[2], b[1] + b[3]])
        info = self.data[name]
        size = info.image.size

        maxdis = 0
        pos = None
        for dx in range(bbox[2] - size[0] + 1):
            for dy in range(bbox[3] - size[1] + 1):
                tbc = im.crop((dx, dy, dx + size[0], dy + size[1]))
                dis = imageutil.diff_image_with_color(tbc, info.image, info.color)
                if (dis > maxdis):
                    maxdis = dis
                    pos = (dx, dy)
                    print pos, maxdis
        if (maxdis > 0.5):
            return (pos[0] + bbox[0], pos[1] + bbox[1])
        else:
            return None

    def get(self, name):
        return self.data[name]


class Info:
    pass

