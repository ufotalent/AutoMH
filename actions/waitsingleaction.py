from team_checker import TeamChecker
import time
class WaitSingleAction:
    def name(self):
        return "waitsingle"

    def buddy(self):
        return -1

    def timeout(self):
        return 3600

    def handle(self, account):
        while TeamChecker().members() >= 0:
            time.sleep(300)

