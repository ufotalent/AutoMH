from future_task_manager import FutureTaskManager
from button_manager import ButtonManager
from screen import ScreenCapture
from fixed_image import FixedImage
from menu_manager import MenuManager
from item_manager import ItemManager
from item_user import ItemUser
import imageutil
import time
import sets
class CleanUpAction:
    def name(self):
        return "cleanup"

    def buddy(self):
        return -1

    def timeout(self):
        return 1800

    def do_pengren(self):
        MenuManager().open_menu(1)
        time.sleep(3)
        ScreenCapture().click(960, 340)
        time.sleep(5)
        ScreenCapture().click(150, 270)
        time.sleep(5)
        for i in range(30):
            ScreenCapture().click(700, 620)
            time.sleep(1)
        # Closing jineng actually
        FixedImage().dismiss('CloseBaoGuo')

    def handle(self, account):
        self.do_pengren()
        time.sleep(3)

        self.do_buji()
        time.sleep(3)

        items = ItemManager()
        items.open()
        self.do_checkitem(account, items, 'use')
        ScreenCapture().click(960, 340)

        items.reset()
        time.sleep(3)
        self.do_checkitem(account, items, 'store')
        time.sleep(3)
        items.close()

        time.sleep(3)
        self.do_sell()
        time.sleep(3)
        

        self.do_sell_gold()
        time.sleep(3)


    def do_buji(self):
        ScreenCapture().click(975, 50)
        time.sleep(3)
        ScreenCapture().click(960, 350)
        time.sleep(3)
        should_buy = False
        if FixedImage().test('HPFull') > 5:
            ScreenCapture().click(410, 380)
            should_buy = True
        elif FixedImage().test('MPFull') > 5:
            ScreenCapture().click(410, 605)
            should_buy = True
        time.sleep(3)
        if should_buy:
            ScreenCapture().click(780, 580)
            time.sleep(3)
            FixedImage().dismiss('CloseJiuDian') 
            time.sleep(3)
            ItemUser().test_and_use()
            time.sleep(3)
        else:
            FixedImage().dismiss('CloseBaoGuo')

    def do_sell(self):
        ScreenCapture().click(50, 200)
        time.sleep(3)
        ScreenCapture().click(970, 220)
        time.sleep(3)
        ScreenCapture().click(350, 150)
        time.sleep(3)
        while FixedImage().test('NothingToSell') > 5:
            ScreenCapture().click(120, 250)
            time.sleep(1)
            ScreenCapture().click(800, 650)
            time.sleep(1)
        FixedImage().dismiss('CloseBaoGuo')

    def do_sell_gold(self):
        ScreenCapture().click(50, 200)
        time.sleep(3)
        ScreenCapture().click(970, 370)
        time.sleep(3)
        ScreenCapture().click(350, 150)
        time.sleep(3)
        ploc = [[351, 478]]
        empty_img = FixedImage().get('BaitanEmpty').image
        for x in range(4, -1, -1):
            for y in range (3, -1, -1):
                print x, y
                img = ScreenCapture().capture([650 + y * 80, 250 + x * 80, 20, 20])
                if (imageutil.diff_image(img, empty_img) < 5):
                    continue
                slot = ScreenCapture().capture([370, 550, 20, 20])
                if (imageutil.diff_image(slot, empty_img) > 5):
                    continue
                ScreenCapture().click(650 + y * 80, 250 + x * 80)
                time.sleep(10)
                done = False
                for i in range(1):
                    name = 'PriceMinus%d' % i
                    if not FixedImage().has(name):
                        break
                    plusloc = [FixedImage().get(name).location[0],  FixedImage().get(name).location[1]]
                    plusloc[0] = plusloc[0] + 212
                    ScreenCapture().click(plusloc[0], plusloc[1])
                    if FixedImage().test(name) > 5: 
                        continue
                    for p in range(11):
                        FixedImage().click(name)
                        time.sleep(1)
                    for p in range(11):
                        pnow = ScreenCapture().capture([ploc[i][0], ploc[i][1], 100, 23])
                        match = 0
                        for c in range(4):
                            pcand = ScreenCapture().capture([705, 248 + c * 100, 100, 23])
                            if imageutil.diff_image(pnow, pcand) < 8:
                                match = match + 1
                        if match == 4:
                            FixedImage().click(name)
                            time.sleep(1)
                        if match > 0:
                            FixedImage().dismiss('Shangjia')
                            FixedImage().dismiss('ConfirmShangjia')
                            done = True
                            break
                        ScreenCapture().click(plusloc[0], plusloc[1])
                        time.sleep(3)
                    break
                if not done:
                    FixedImage().dismiss('CloseSell')
                    time.sleep(3)
        FixedImage().dismiss('CloseBaoGuo')

                            

        '''351, 478 -> 450, 500
        354, 490 || 708, 260
        380, 446 || 770, 259
        y offset 100'''

    def do_checkitem(self, account, items, expected_policy):
        for page in range(3):
            if not page == 0:
                items.next_page()
            for row in range(4):
                for col in range(5):
                    while True:
                        n = items.get_item_name(row, col)
                        if ( n == 'unknown'):
                            break
                        policy = items.get_default_policy(n)
                        if n in account.item_policy:
                            policy = account.item_policy[n]
                        print row, col, n, policy
                        if (policy == expected_policy):
                            pos = items.get_item_pos(row, col)
                            ScreenCapture().double_click(pos[0] + 30, pos[1] + 30)
                            time.sleep(8)
                            continue
                        break
