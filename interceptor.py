import time, datetime
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

class InvitationInterceptor(Interceptor):
    def can_handle(self, screen):
        from fixed_image import FixedImage
        return FixedImage().test('AcceptInvitation', screen) < 5 

    def handle(self):
        from fixed_image import FixedImage
        from screen import ScreenCapture
        for i in range(100):
            name = 'InvitationWhitelist%d' % i
            if not FixedImage().has(name):
                break
            if FixedImage().test(name) < 5:
                FixedImage().dismiss('AcceptInvitation')
                raise RuntimeError('Accepted Invitation')
        print 'Rejected invitation'
        ScreenCapture().click(450, 440)
        time.sleep(3)

    def name(self):
        return "InvitationInterceptor"

class TeamRequestInterceptor(Interceptor):
    def can_handle(self, screen):
        from fixed_image import FixedImage
        return FixedImage().test('TeamRequest', screen) < 5 

    def handle(self):
        from fixed_image import FixedImage
        from screen import ScreenCapture
        ScreenCapture().click(600, 440)
        time.sleep(3)

    def name(self):
        return "TeamRequestInterceptor"

class OfflineInterceptor(Interceptor):
    def can_handle(self, screen):
        from fixed_image import FixedImage
        return FixedImage().test('Offline', screen) < 5 

    def handle(self):
        from screen import ScreenCapture
        from fixed_image import FixedImage
        if FixedImage().test('OfflineOKOnly') < 5:
            ScreenCapture().click(512, 440)
            time.sleep(60)
            raise RuntimeError('Offline')
        else:
            ScreenCapture().click(600, 440)

    def name(self):
        return "OfflineInterceptor"

class UnrecoverableOfflineInterceptor(Interceptor):
    def can_handle(self, screen):
        from fixed_image import FixedImage
        return FixedImage().test('Kicked', screen) < 5

    def handle(self):
        from screen import ScreenCapture
        from fixed_image import FixedImage
        ScreenCapture().click(500, 430)
        time.sleep(30)
        raise RuntimeError('Kicked')

    def name(self):
        return "UnrecoverableOfflineInterceptor"

class ConversationInterceptor(Interceptor):
    def can_handle(self, screen):
        from fixed_image import FixedImage
        return FixedImage().test('ButtonIndicator', screen) > 10 and FixedImage().test('ConversationFrame', screen) < 10

    def handle(self):
        from screen import ScreenCapture
        ScreenCapture().click(300, 630)

    def name(self):
        return "ConversationInterceptor"

class MonitorInterceptor(Interceptor):
    deadline = 10000000000
    def can_handle(self, screen):
        return time.time() > MonitorInterceptor.deadline

    def handle(self):
        MonitorInterceptor.deadline = 10000000000
        raise RuntimeError('Interrupt')
    
    def name(self):
        return 'MonitorInterceptor'


class SJQYInterceptor(Interceptor):
    def can_handle(self, screen):
        from fixed_image import FixedImage
        return FixedImage().test('SJQYPopup', screen) < 5 or FixedImage().test('KJXSPopup', screen) < 5

    def handle(self):
        from screen import ScreenCapture
        ScreenCapture().click(380, 445)

    def name(self):
        return "SJQYInterceptor"

class JiangshiInterceptor(Interceptor):
    def can_handle(self, screen):
        from fixed_image import FixedImage
        return FixedImage().test('CloseJiangshi', screen) < 5

    def handle(self):
        from fixed_image import FixedImage
        return FixedImage().dismiss('CloseJiangshi')

    def name(self):
        return "JiangShiInterceptor"

class JingjichangInterceptor(Interceptor):
    last_day = datetime.date.today() - datetime.timedelta(days = 1)
    def can_handle(self, screen):
        now = datetime.datetime.now()
        if (now.hour == 22 and now.minute < 40) or (now.hour == 21 and now.minute > 55):
            if JingjichangInterceptor.last_day != datetime.date.today():
                return True
        return False

    def handle(self):
        JingjichangInterceptor.last_day = datetime.date.today()
        raise RuntimeError('task jingjichang')

    def name(self):
        return 'JingjichangInterceptor'

interceptors = [
        FuLiInterceptor(),
        OfflineInterceptor(),
        UnrecoverableOfflineInterceptor(),
        ConversationInterceptor(),
        SJQYInterceptor(),
        MonitorInterceptor(),
        InvitationInterceptor(),
        TeamRequestInterceptor(),
        JingjichangInterceptor()
        ]
