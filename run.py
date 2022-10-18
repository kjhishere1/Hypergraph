import os
import turtle

import util

from rich.console import Console
from rich.progress import track
from hypergraph import Hypergraph as HG

width, height = 512, 512
Origin = True
Xaxis = True
Yaxis = True
Xcon = 80
Ycon = 80
Step = 3

c = Console()
c.print(util.logo_c, justify="center")
c.print(
	util.makeTable(
		["평면 크기", "원점", "X축", "Y축", "X축 눈금", "Y축 눈금", "X값 증가량"],
		[f"{width}x{height}", "✅" if Origin else "❌", "✅" if Xaxis else "❌", "✅" if Yaxis else "❌", str(Xcon), str(Ycon), str(Step)]
	)
)
c.print('Ctrl + D를 눌러서 나가기', style="bold red")


def draw(hg, func, step):
	hg.step = step
	hg.function = func
	gr = iter(hg._drawFunc())
	for _ in track(hg.xList):
		next(gr)

hg = HG(width, height, None, Step)
if Origin:
	hg.originMark()
if Xaxis:
	hg.drawX()
if Yaxis:
	hg.drawY()
hg.contourX(Xcon)
hg.contourY(Ycon)

env = {}
env["locals"]   = None
env["globals"]  = None
env["__name__"] = None
env["__file__"] = None
env["__builtins__"] = None

errorPrint = lambda msg, e: c.print(f'{msg} [red][b]{e}[/b][/red]')

while True:
	cere = input(">: f(x)=")
	if cere == '':
		exit()
	try:
		func = eval("lambda x: " + cere, env)
		draw(hg, func, Step)
	except SyntaxError as e:
		errorPrint('수식 문법 오류가 있습니다.', e)
	except NameError as e:
		errorPrint('정의 되지 않은 변수를 사용 했습니다.', e)
	except TypeError as e:
		errorPrint('수식 문법 오류가 있습니다.', e)
	except ZeroDivisionError as e:
		errorPrint('분모가 0이 될 수 없습니다.', e)
	except OverflowError as e:
		errorPrint('숫자 값이 너무 큽니다.', e)
	except Exception as e:
		errorPrint('알 수 없는 오류가 발생했습니다.', e)