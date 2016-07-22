import imageutil, win32api, win32con, time
import PIL.ImageGrab as ImageGrab
from interceptor import interceptors
class ScreenCapture(object):
    _instance = None

    def uniform_vertical(self, screen, x, y):
        pixel = screen.getpixel((x, y))
        cnt = 1
        nowy = y - 1
        while nowy >= 0 and imageutil.diff_pixel(screen.getpixel((x, nowy)), pixel) < 1:
            nowy = nowy - 1
            cnt = cnt + 1
        nowy = y + 1
        while nowy < screen.size[1] and imageutil.diff_pixel(screen.getpixel((x, nowy)), pixel) < 1:
            nowy = nowy + 1
            cnt = cnt + 1
        return cnt > 700

    def uniform_horizonal(self, screen, x, y):
        pixel = screen.getpixel((x, y))
        cnt = 1
        nowx = x - 1
        while nowx >= 0 and imageutil.diff_pixel(screen.getpixel((nowx, y)), pixel) < 1:
            nowx = nowx - 1
            cnt = cnt + 1
        nowx = y + 1
        while nowx < screen.size[0] and imageutil.diff_pixel(screen.getpixel((nowx, y)), pixel) < 1:
            nowx = nowx + 1
            cnt = cnt + 1
        return cnt > 900
        
        
    def setup(self):
        print "setting up ScreenCapture"
        self.intercepting = False
        screen = ImageGrab.grab()
        self.top = 200
        self.left = 200
        self.last_time = 0
        self.last_screenshot = None
        self.frozen = False
        while not self.uniform_vertical(screen, self.left, 200):
            self.left = self.left - 1
        while not self.uniform_horizonal(screen, 200, self.top):
            self.top = self.top - 1
        print "Offset:", self.left, self.top

        

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
            class_._instance.setup()
        return class_._instance

    def capture(self, bbox = [0, 0, 1024, 768]):
        if (not self.frozen) and self.last_time + 1 < time.time():
            self.last_screenshot = ImageGrab.grab()
            self.last_time = time.time()
            handled = False
            for i in interceptors:
                if self.intercepting:
                    continue
                self.intercepting = True
                try:
                    can = i.can_handle(self.last_screenshot.crop([self.left, self.top, self.left + 1024, self.top + 768]))
                    if can:
                        i.handle()
                        handled = True
                finally:
                    self.intercepting = False
            if handled:
                self.last_screenshot = ImageGrab.grab()
                self.last_time = time.time()
        im = self.last_screenshot.crop([self.left + bbox[0], self.top + bbox[1], self.left + bbox[0] + bbox[2], self.top + bbox[1] + bbox[3]])
        return im

    def reset(self):
        for x in range(5):
            self.keyboard(27)
            time.sleep(3)
        ScreenCapture().click(4, 4)
        time.sleep(5)
        ScreenCapture().click(500, 400)
        time.sleep(5)

    def keyboard(self, vk):
        win32api.keybd_event(vk, vk, 0, 0)
        time.sleep(0.3)
        win32api.keybd_event(vk, vk, win32con.KEYEVENTF_KEYUP, 0)

    def click(self, x, y):
        x = x + self.left
        y = y + self.top
        win32api.SetCursorPos((x, y)) 
        time.sleep(0.3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    def double_click(self, x, y):
        x = x + self.left
        y = y + self.top
        win32api.SetCursorPos((x, y)) 
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    def scroll(self, fx, fy, tx, ty):
        win32api.SetCursorPos((self.left + fx, self.top + fy)) 
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.left + fx, self.top + fy, 0, 0)
        for step in range(10):
            s = 0.1 * step
            x = int(s * tx + (1 - s) * fx)
            y = int(s * ty + (1 - s) * fy)
            win32api.SetCursorPos((self.left + x, self.top + y))
            time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.left + tx, self.top + ty, 0, 0)

    def freeze(self):
        self.capture([0, 0, 1, 1])
        self.frozen = True

    def unfreeze(self):
        self.frozen = False
        
if __name__ == '__main__':
    ScreenCapture().capture()
