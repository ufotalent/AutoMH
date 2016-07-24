from shimenaction import ShiMenAction
from baotuaction import BaoTuAction
from mijingaction import MiJingAction
from yunbiaoaction import YunBiaoAction
from cleanupaction import CleanUpAction
from zhuaguiaction import ZhuaGuiAction
from kickallaction import KickAllAction
from fengyaoaction import FengYaoAction
from fubenaction import FuBenAction
from sanjieqiyuanaction import SanJieQiYuanAction
from waitsingleaction import WaitSingleAction
actions = [ShiMenAction(), BaoTuAction(), MiJingAction(), YunBiaoAction(), CleanUpAction(),
        ZhuaGuiAction(), KickAllAction(), FengYaoAction(), FuBenAction(), SanJieQiYuanAction(),
        WaitSingleAction()]
actionsdict = {action.name() : action  for  action in actions}
def get_action(name):
    return actionsdict[name]
