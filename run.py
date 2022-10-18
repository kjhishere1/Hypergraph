import os
import json
import turtle

import util

from rich.console import Console
from rich.progress import track
from hypergraph import Hypergraph as HG

while True:
	try:
		cfg_check = util.CfgChecker('hypergraph')
		if cfg_check:
			Recfg = input("설정을 초기화 하고 재설정 하시겠습니까? (Y/N)\n>: ")
			if Recfg == 'Y':
				raise
	except Exception:
		util.GenCfg()


c = Console()
c.print(util.logo_c, justify="center")
c.print(
	util.makeTable(
		["평면 크기", "원점", "X축", "Y축", "X축 눈금", "Y축 눈금", "X값 증가량"],
		[f"{width}x{height}", "✅" if Origin else "❌", "✅" if Xaxis else "❌", "✅" if Yaxis else "❌", str(Xcon), str(Ycon), str(Step)]
	)
)
c.print('Ctrl + D를 눌러서 나가기', style="bold red")


hg = HG(width, height, None, Step)
if Origin:
	hg.originMark()
if Xaxis:
	hg.drawX()
if Yaxis:
	hg.drawY()
hg.contourX(Xcon)
hg.contourY(Ycon)

while True:
	cere = input(">: f(x)=")
	if cere == '':
		exit()
	try:
		func = eval("lambda x: " + cere, util.env)
		util.draw(hg, func, Step)
	except SyntaxError as e:
		util.errorPrint('수식 문법 오류가 있습니다.', e)
	except NameError as e:
		util.errorPrint('정의 되지 않은 변수를 사용 했습니다.', e)
	except TypeError as e:
		util.errorPrint('수식 문법 오류가 있습니다.', e)
	except ZeroDivisionError as e:
		util.errorPrint('분모가 0이 될 수 없습니다.', e)
	except OverflowError as e:
		util.errorPrint('숫자 값이 너무 큽니다.', e)
	except Exception as e:
		util.errorPrint('알 수 없는 오류가 발생했습니다.', e)