from shimenaction import ShiMenAction
from baotuaction import BaoTuAction
from mijingaction import MiJingAction
from yunbiaoaction import YunBiaoAction
from cleanupaction import CleanUpAction
actions = [ShiMenAction(), BaoTuAction(), MiJingAction(), YunBiaoAction(), CleanUpAction()]
actionsdict = {action.name() : action  for  action in actions}
def get_action(name):
    return actionsdict[name]
