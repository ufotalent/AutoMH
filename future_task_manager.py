import time
from screen import ScreenCapture
from text_image import TextImage
from fixed_image import FixedImage
class FutureTaskManager:
    def get_task(self, name):
        # trigger interceptor
        ScreenCapture().capture(bbox=[0, 0, 1, 1])
        ScreenCapture().click(340, 40)
        time.sleep(3)
        ScreenCapture().click(100, 180)
        time.sleep(1)
        for x in range(3):
            pos = TextImage().find(name, [310, 150, 90, 300])
            if pos is None:
                pos = TextImage().find(name, [310 + 364, 150, 90, 300])
            if not pos is None:
                pixel = ScreenCapture().capture(bbox=[pos[0], pos[1], 1, 1]).getpixel((0, 0))
                if (abs(max(pixel) - min(pixel)) < 5):
                    print 'Already Completed Task:', name
                    if FixedImage().test('CloseHuoDong') < 5:
                        ScreenCapture().click(950, 100)
                    return False
                else:
                    ScreenCapture().click(pos[0] + 220, pos[1] + 30)
                    return True
            ScreenCapture().scroll(353, 469, 353, 250)
            time.sleep(3)
        if FixedImage().test('CloseHuoDong') < 5:
            ScreenCapture().click(950, 100)
        return False
