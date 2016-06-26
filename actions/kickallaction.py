from team_checker import TeamChecker
class KickAllAction:
    def name(self):
        return "kickall"
    def buddy(self):
        return 0
    def handle(self, account):
        TeamChecker().kick_all()
        
