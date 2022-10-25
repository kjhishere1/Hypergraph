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
		["평면 크기", "원점", "X축", "Y축", "X축 눈금", "Y축 눈금", "X값 증가량"],
		[
			f"{cfg['size']['width']}x{cfg['size']['height']}",
			"✅" if cfg['origin'] else "❌",
			"✅" if cfg['xaxis'] else "❌",
			"✅" if cfg['yaxis'] else "❌",
			str(cfg['xcon']),
			str(cfg['ycon']),
			str(cfg['step'])
		]
	)
)
c.print('Ctrl + D를 눌러서 나가기', style="bold red")

def draw(func):
	global hg
	hg._move(hg.xMax, func(int(hg.xMax)))
	for x in track(hg.xList):
		try:
			y = func(x)
		except ZeroDivisionError as e:
			x = hg.xList[hg.xList.index(x) + 1]
			y = func(x)
			hg._move(x, y)
		else:
			hg.turtle.goto(x, y)
		yield x


hg = HG(cfg['size']['width'], cfg['size']['height'], None, cfg['step'])
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
		func = eval("lambda x: " + cere, util.env)
		if type(func(1)) == int:
			for _ in draw(func): pass
		elif type(func(1)) == float:
			for _ in draw(func): pass
		else:
			raise TypeError("함수의 값은 유리수로 정해져야합니다.")
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