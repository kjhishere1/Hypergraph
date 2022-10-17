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
c.print('Shift + D를 눌러서 나가기', style="bold red")


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

while True:
	cere = input(">: f(x)=")
	if cere == '':
		exit()
	func = eval("lambda x: " + cere)
	draw(hg, func, Step)
