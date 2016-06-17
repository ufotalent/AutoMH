from screen import ScreenCapture
import sys

im = ScreenCapture().capture([
    int(sys.argv[1]), 
    int(sys.argv[2]), 
    int(sys.argv[3]), 
    int(sys.argv[4])])
if len(sys.argv) > 5:
    im.save(sys.argv[5])
else:
    im.show()
