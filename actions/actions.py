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
from jingjichangaction import JingJiChangAction
from kejuxiangshiaction import KeJuXiangShiAction
from bangpaiaction import BangPaiAction
actions = [ShiMenAction(), BaoTuAction(), MiJingAction(), YunBiaoAction(), CleanUpAction(),
        ZhuaGuiAction(), KickAllAction(), FengYaoAction(), FuBenAction(), SanJieQiYuanAction(),
        WaitSingleAction(), JingJiChangAction(), KeJuXiangShiAction(), BangPaiAction()]
actionsdict = {action.name() : action  for  action in actions}
def get_action(name):
    return actionsdict[name]
