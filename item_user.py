from fixed_image import  FixedImage 
from screen import ScreenCapture
class ItemUser:
    def test_and_use(self):
        if FixedImage().test('UseItem') < 5:
            pos = FixedImage().get('UseItem').location
            ScreenCapture().click(pos[0] + pos[2] / 2, pos[1] + pos[3] / 2)
            return True
        return False

