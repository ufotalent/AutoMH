import os, sys, time
from screen import ScreenCapture
x = 650 + int(sys.argv[2]) * 80
y = 250 + int(sys.argv[1]) * 80
while True:
    ScreenCapture().click(x, y)
    time.sleep(1)
    ScreenCapture().click(450, 600)
    time.sleep(1)

