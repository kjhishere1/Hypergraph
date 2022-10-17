import os
import turtle

import util
from hypergraph import Hypergraph as HG

util.pip_install('rich')
from rich.console import Console


width, height = 512, 512
Origin = True
Xaxis = True
Yaxis = True
Xcon = 80
Ycon = 80
Step = 3

print(util.logo)
c = Console()
c.print(
	util.makeTable(
		["평면 크기", "원점", "X축", "Y축", "X축 눈금", "Y축 눈금", "X값 증가량"],
		[f"{width}x{height}", "✅" if Origin else "❌", "✅" if Xaxis else "❌", "✅" if Yaxis else "❌", str(Xcon), str(Ycon), str(Step)]
	)
)
print('Shift + D를 눌러서 나가기')


def draw(func, step):
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

while True:
	cere = input(">: f(x)=")
	if cere == '':
		exit()
	func = eval("lambda x: " + cere)
	draw(func, Step)
