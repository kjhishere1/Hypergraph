import os
import turtle

import pip
from importlib import util
found = True if util.find_spec('rich') is not None else False
if not found:
    pip.main(['install', "rich"])
    os.system('cls')

from rich import box
from rich.progress import track
from rich.console import Console
from rich.table import Table

from hypergraph import Hypergraph as HG

logo = r"""
 /$$   /$$                                                                                /$$      
| $$  | $$                                                                               | $$      
| $$  | $$ /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$   /$$$$$$ | $$$$$$$ 
| $$$$$$$$| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$|____  $$ /$$__  $$| $$__  $$
| $$__  $$| $$  | $$| $$  \ $$| $$$$$$$$| $$  \__/| $$  \ $$| $$  \__/ /$$$$$$$| $$  \ $$| $$  \ $$
| $$  | $$| $$  | $$| $$  | $$| $$_____/| $$      | $$  | $$| $$      /$$__  $$| $$  | $$| $$  | $$
| $$  | $$|  $$$$$$$| $$$$$$$/|  $$$$$$$| $$      |  $$$$$$$| $$     |  $$$$$$$| $$$$$$$/| $$  | $$
|__/  |__/ \____  $$| $$____/  \_______/|__/       \____  $$|__/      \_______/| $$____/ |__/  |__/
           /$$  | $$| $$                           /$$  \ $$                   | $$                
          |  $$$$$$/| $$                          |  $$$$$$/                   | $$                
           \______/ |__/                           \______/                    |__/                

"""

width, height = 512, 512
Origin = True
Xaxis = True
Yaxis = True
Xcon = 80
Ycon = 80
Step = 3

console = Console()

table = Table(show_header=True, header_style="bold")
table.box = box.SIMPLE
col = ["평면 크기", "원점", "X축", "Y축", "X축 눈금", "Y축 눈금", "X값 증가량"]
for text in col:
	table.add_column(text, justify="center", width=12)
table.add_row(
	f"{width}x{height}",
	"✅" if Origin else "❌",
	"✅" if Xaxis else "❌",
	"✅" if Yaxis else "❌",
	str(Xcon),
	str(Ycon),
	str(Step)
)

def draw(func, step):
	hg.step = step
	hg.function = func
	gr = iter(hg._drawFunc())
	for _ in track(hg.xList):
		next(gr)

print(logo.rstrip())
console.print(table)
print('Shift + D를 눌러서 나가기')

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
