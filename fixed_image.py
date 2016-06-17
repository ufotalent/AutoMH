import json, traceback
import PIL
from screen import ScreenCapture
import imageutil
class FixedImage(object):
    _instance = None
    data_dir = 'fixed_image/'
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
            info.location = item['location']
            self.data[item['name']] = info

    def test(self, name, screen = None):
        im = None
        if screen == None:
            im = ScreenCapture().capture(self.data[name].location)
        else:
            b = self.data[name].location
            im = screen.crop([b[0], b[1], b[0] + b[2], b[1] + b[3]])
        dis = imageutil.diff_image(im, self.data[name].image)
        print 'FixedImage distance:', name, dis
        
        return dis

    def get(self, name):
        return self.data[name]


class Info:
    pass
