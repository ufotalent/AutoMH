import sys
from item_manager import ItemManager

i = ItemManager()
i.calibrate()
im = i.get_item_image(int(sys.argv[1]), int(sys.argv[2]))
if len(sys.argv) > 3:
    im.save(sys.argv[3])
else:
    im.show()


