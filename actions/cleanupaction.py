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
        return 1200

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
