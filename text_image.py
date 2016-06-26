import json, time
import PIL
from PIL import Image
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
            info.color = item['color']
            info.image = PIL.Image.open(self.data_dir + item['file'])
            info.image = imageutil.bitmap_image_with_color(info.image, info.color)
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
        im = imageutil.bitmap_image_with_color(im, info.color)

        hist = [[0 for x in range(im.size[1] + 1)] for y in range(im.size[0] + 1)]
        for dx in range(im.size[0]):
            hist.append([0])
            for dy in range(im.size[1]):
                pixel = im.getpixel((dx, dy))
                hist[dx + 1][dy + 1] = hist[dx][dy + 1] + hist[dx + 1][dy] - hist[dx][dy]
                if pixel > 0:
                    hist[dx + 1][dy + 1] = hist[dx + 1][dy + 1] + 1
        maxdis = 0
        pos = None
        #debug = [0 for x in range((bbox[2] - size[0] + 1) * (bbox[3] - size[1] + 1))]
        for dx in range(bbox[2] - size[0] + 1):
            for dy in range(bbox[3] - size[1] + 1):
                cnt = hist[dx + size[0]][dy + size[1]] - hist[dx][dy + size[1]] - hist[dx + size[0]][dy] + hist[dx][dy]
                if (cnt < 50):
                    continue
                #debug[dy * (bbox[2] - size[0] + 1) + dx] = 255
                tbc = im.crop((dx, dy, dx + size[0], dy + size[1]))
                dis = imageutil.diff_bitmap(tbc, info.image)
                if (dis > maxdis):
                    maxdis = dis
                    pos = (dx, dy)
                    print pos, maxdis
        #img_debug = Image.new('L', (bbox[2] - size[0] + 1, bbox[3] - size[1] + 1))
        #img_debug.putdata(debug)
        #img_debug.show()
        if (maxdis > 0.5):
            return (pos[0] + bbox[0], pos[1] + bbox[1])
        else:
            return None

    def get(self, name):
        return self.data[name]


class Info:
    pass

