import os
import json
import turtle
import random

import util

from rich.console import Console
from rich.progress import track
from hypergraph import Hypergraph as HG

while True:
    try:
        cfg_check = util.CfgChecker('hypergraph')
        if cfg_check:
            Recfg = input("설정을 초기화 하고 재설정 하시겠습니까? (Y를 눌러 확인)\n>: ")
            if Recfg == 'Y':
                raise
            else:
                break
    except Exception:
        util.GenCfg('hypergraph')

with open(util.GetCfgPath('hypergraph'), 'r', encoding="UTF-8") as file:
    cfg = json.loads(file.read())


c = Console()
c.print(util.logo_c, justify="center")
c.print(
    util.makeTable(
        ["평면 크기", "원점", "X축", "Y축", "X축 눈금", "Y축 눈금", "X값 증가량", "비율"],
        [
            f"{cfg['size']['width']}x{cfg['size']['height']}",
            "✅" if cfg['origin'] else "❌",
            "✅" if cfg['xaxis'] else "❌",
            "✅" if cfg['yaxis'] else "❌",
            str(cfg['xcon']),
            str(cfg['ycon']),
            str(cfg['step']),
            f"1:{cfg['ratio']}px"
        ]
    )
)
c.print('Ctrl + D를 눌러서 나가기', style="bold red")


hg = HG(cfg['size']['width'], cfg['size']['height'], None, cfg['ratio'], cfg['step'])
if cfg['origin']:
    hg.originMark()
if cfg['xaxis']:
    hg.drawX()
if cfg['yaxis']:
    hg.drawY()
hg.contourX(cfg['xcon'])
hg.contourY(cfg['ycon'])


while True:
    cere = input(">: f(x)=").lower()
    if cere == '':
        exit()
    try:
        print(hg.Parse("lambda x: " + cere))
        func = eval(hg.Parse("lambda x: " + cere), util.env)
        ranX = random.randint(0, cfg['size']['width'])
        if type(func(ranX)) in [int, float, complex]:
            hg.function = func
            for x, y in hg._drawFunc(track):
                pass
        else:
            raise TypeError("함수의 값은 유리수여야합니다.")
    except SyntaxError as e:
        util.errorPrint(c, '수식 문법 오류가 있습니다.', e)
    except NameError as e:
        util.errorPrint(c, '정의되지 않은 변수입니다.', e)
    except TypeError as e:
        util.errorPrint(c, '수식 타입 오류가 있습니다.', e)
    except ZeroDivisionError as e:
        util.errorPrint(c, '분모는 0이 될 수 없습니다.', e)
    except OverflowError as e:
        util.errorPrint(c, '입력된 숫자가 너무 큽니다.', e)
    except Exception as e:
        util.errorPrint(c, '알 수 없는 오류가 발생했습니다.', e)