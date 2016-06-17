import json, requests, time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from screen import ScreenCapture
from fixed_image import FixedImage
class Login(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            print "Setting up login"
            class_._instance = object.__new__(class_, *args, **kwargs)
            class_._instance.setup()
        return class_._instance

    def email(self, target, title, content):
        server = smtplib.SMTP()
        server.connect(self.smtp_config['server'])
        server.login(self.smtp_config['username'], self.smtp_config['password']);
        msg = MIMEText(content, 'text');
        msg['Subject'] = Header(title)
        msg['from'] = self.smtp_config['username']
        msg['to'] = target
        server.sendmail(self.smtp_config['username'], target, msg.as_string());

    def setup(self):
        self.smtp_config = json.load(open("smtp.json"))

    def login(self, user):
        self.email("ufotalent@ufotalent.me",
                "Please login your user",
                "http://my.ufotalent.me/login/" + user)
        while FixedImage().test('ServerStatus') > 5:
            if FixedImage().test('WindowGG') < 5:
                ScreenCapture().click(500, 650)
            ScreenCapture().click(512, 384)
            prcode = ScreenCapture().capture(bbox=[380, 220, 250, 250])
            fn = 'prcode/%s.jpg' % user
            prcode.save(fn)
            try:
                requests.post('http://my.ufotalent.me/update/' + user,
                        files = {'image' : open(fn, 'rb')})
            except Exception as e:
                pass
            time.sleep(30)
        location = FixedImage().get('LoginButton').location
        ScreenCapture().click(location[0] + 50, location[1] + 50)
        while FixedImage().test('LogedInIndicator') > 5:
            time.sleep(5)

    def should_login(self):
        return FixedImage().test('QRFrame') < 5;

    def logout(self):
        while FixedImage().test('MenuPlus') > 5:
            time.sleep(5)
        ScreenCapture().click(980, 720);
        time.sleep(3)
        ScreenCapture().click(562, 715);
        time.sleep(3)
        ScreenCapture().click(320, 605);
        time.sleep(3)
        ScreenCapture().click(620, 455);
        #while FixedImage().test('QRFrame') > 5:
        #    time.sleep(5)

