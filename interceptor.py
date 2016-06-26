import time
class Interceptor:
    def can_handle(self, screen):
        pass
    def handle(self):
        pass
    def name(self):
        raise Exception("interceptor has no name")

class FuLiInterceptor(Interceptor):
    def can_handle(self, screen):
        from fixed_image import FixedImage
        return FixedImage().test('WindowFuLi', screen) < 5

    def handle(self):
        from screen import ScreenCapture
        from fixed_image import FixedImage
        img = ScreenCapture().capture(bbox=[300, 250, 550, 400])
        cnt = 0
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if img.getpixel((x, y)) == (233, 217, 195):
                    cnt = cnt + 1
                    if cnt > 10:
                        ScreenCapture().click(300 + x, 250 + y + 10)
                        time.sleep(3)
                        ScreenCapture().click(900, 130)
                        time.sleep(3)
                        if FixedImage().test('CloseFuLi') < 20:
                            ScreenCapture().click(900, 130)
                            time.sleep(3)
                        return
                else:
                    cnt = 0
        time.sleep(3)
        ScreenCapture().click(900, 130)
        time.sleep(3)

    def name(self):
        return "FuLiInterceptor"

class OfflineInterceptor(Interceptor):
    def can_handle(self, screen):
        from fixed_image import FixedImage
        return FixedImage().test('Offline', screen) < 5

    def handle(self):
        from screen import ScreenCapture
        ScreenCapture().click(600, 440)

    def name(self):
        return "OfflineInterceptor"

class ConversationInterceptor(Interceptor):
    def can_handle(self, screen):
        from fixed_image import FixedImage
        return FixedImage().test('ButtonIndicator', screen) > 10 and FixedImage().test('ConversationFrame', screen) < 10

    def handle(self):
        from screen import ScreenCapture
        ScreenCapture().click(300, 630)

    def name(self):
        return "ConversationInterceptor"

class SJQYInterceptor(Interceptor):
    def can_handle(self, screen):
        from fixed_image import FixedImage
        return FixedImage().test('SJQYPopup', screen) < 5 or FixedImage().test('KJXSPopup', screen) < 5

    def handle(self):
        from screen import ScreenCapture
        ScreenCapture().click(380, 445)

    def name(self):
        return "SJQYInterceptor"
interceptors = [
        FuLiInterceptor(),
        OfflineInterceptor(),
        ConversationInterceptor(),
        SJQYInterceptor()
        ]
