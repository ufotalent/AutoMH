import json, traceback, time
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
            info.image.load()
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

    def has(self, name):
        return name in self.data

    def get(self, name):
        return self.data[name]

    def click(self, name):
        loc = self.data[name].location
        ScreenCapture().click(loc[0] + loc[2] / 2, loc[1] + loc[3] / 2)

    def click_if(self, name, thres = 5):
        if self.test(name) < thres:
            loc = self.data[name].location
            ScreenCapture().click(loc[0] + loc[2]/2, loc[1] + loc[3]/2)

    def dismiss(self, name, thres = 5):
        res = False
        while self.test(name) < thres:
            res = True
            loc = self.data[name].location
            ScreenCapture().click(loc[0] + loc[2]/2, loc[1] + loc[3]/2)
            time.sleep(5)
        return res

    def dismissAll(self):
        while True:
            res = False
            for name in self.data:
                if name.startswith('Close'):
                    if self.dismiss(name):
                        res = True
            if not res:
                break

class Info:
    pass
