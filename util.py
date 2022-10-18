import os
import pip
import ast
import json

from importlib.util import find_spec


def pip_install(modules):
    ins = []
    if type(modules) == str:
        if not find_spec(modules):
            ins.append(modules)
    elif type(modules) == list:
        for module in modules:
            if not find_spec(module):
                ins.append(module)
    if ins != []:
        pip.main(['install', *ins])
        os.system('cls')


pip_install('rich')
from rich import box
from rich.table import Table


def makeTable(col: list, row: list):
    table = Table(show_header=True, header_style="bold")
    table.box = box.SIMPLE
    for text in col:
        table.add_column(text, justify="center", width=12)
    table.add_row(*row)
    return table


def TypeCheck(value: str, type_type):
    try:
        typed = ast.literal_eval(str(value))
        return type(typed) == type_type
    except Exception:
        return False


def GetCfgPath(cfg_path):
    PATH = os.path.join(os.getenv('APPDATA'), cfg_path)
    CFG = os.path.join(PATH, r"config.json")
    if os.path.exists(CFG):
        return CFG
    else:
        os.mkdir(PATH)
        with open(CFG, 'w', encoding="UTF-8") as file:
            file.write('{}')
        return CFG


def CfgChecker(cfg_path):
    with open(GetCfgPath(cfg_path), 'r', encoding="UTF-8") as file:
        cfg = file.read()
        cfg = json.loads(cfg)

    for key in cfg.keys():
        value = cfg[key]
        if len(cfg.keys()) != 7:
            raise ValueError("설정 파일의 값에 문제가 생겼습니다.")

        if key == "size":
            assert TypeCheck(value['width'], int) is True, "width값이 정수가 아닙니다."
            assert TypeCheck(value['height'], int) is True, "height값이 정수가 아닙니다."
        elif key == "origin":
            assert TypeCheck(value, bool) is True, "origin값이 Bool이 아닙니다."
        elif key == "xaxis":
            assert TypeCheck(value, bool) is True, "xaxis값이 Bool이 아닙니다."
        elif key == "yaxis":
            assert TypeCheck(value, bool) is True, "yaxis값이 Bool이 아닙니다."
        elif key == "xcon":
            assert TypeCheck(value, int) is True, "xcon값이 정수가 아닙니다."
        elif key == "ycon":
            assert TypeCheck(value, int) is True, "ycon값이 정수가 아닙니다."
        elif key == "step":
            assert TypeCheck(value, int) is True, "step값이 정수가 아닙니다."
        else:
            raise TypeError("정의되지 않은 값입니다.")
    return True


def GenCfg(cfg_path):
    if (width := input('좌표평면의 가로 크기를 적어주세요.\n(기본값: 512) >: ')) == '':
        print("기본값으로 설정합니다.")
        width = 512
    if (height := input('좌표평면의 세로 크기를 적어주세요.\n(기본값: 512) >: ')) == '':
        print("기본값으로 설정합니다.")
        height = 512
    if (origin := input('좌표평면에서 원점을 표시 할까요? (Y를 눌러 확인)\n(기본값: Y) >: ')) == '':
        print("기본값으로 설정합니다.")
        origin = 'Y'
    if (xaxis := input('좌표평면에서 X축을 표시 할까요? (Y를 눌러 확인)\n(기본값: Y) >: ')) == '':
        print("기본값으로 설정합니다.")
        xaxis = 'Y'
    if (yaxis := input('좌표평면에서 Y축을 표시 할까요? (Y를 눌러 확인)\n(기본값: Y) >: ')) == '':
        print("기본값으로 설정합니다.")
        yaxis = 'Y'
    if (xcon := input('좌표평면에서 X축 눈금의 단위는? (Y를 눌러 확인)\n(기본값: 200) >: ')) == '':
        print("기본값으로 설정합니다.")
        xcon = 200
    if (ycon := input('좌표평면에서 Y축 눈금의 단위는? (Y를 눌러 확인)\n(기본값: 200) >: ')) == '':
        print("기본값으로 설정합니다.")
        ycon = 200
    if (step := input('X의 정의역을 몇의 배수로 설정 하시겠습니까?\n(기본값: 3) >: ')) == '':
        print("기본값으로 설정합니다.")
        step = 3

    cfg = {}
    cfg["size"] = {
        "width": width if TypeCheck(width, int) else 512,
        "height": height if TypeCheck(height, int) else 512
    }
    cfg["origin"] = True if origin == 'Y' else False
    cfg["xaxis"] = True if xaxis == 'Y' else False
    cfg["yaxis"] = True if yaxis == 'Y' else False

    if TypeCheck(xcon, int):
        if int(xcon) >= 0:
            cfg["xcon"] = int(xcon)
        else:
            cfg["xcon"] = 200
    else:
        cfg["xcon"] = 200

    if TypeCheck(ycon, int):
        if int(ycon) >= 0:
            cfg["ycon"] = int(ycon)
        else:
            cfg["ycon"] = 200
    else:
        cfg["ycon"] = 200

    cfg["step"] = step if TypeCheck(step, int) else 3

    cfg = json.dumps(cfg)

    with open(GetCfgPath(cfg_path), 'w', encoding="UTF-8") as file:
        file.write(cfg)
    print('설정을 저장했습니다.')

logo = f"\n /$$   /$${' '*80}/$$\n| $$  | $${' '*79}| $$\n| $$  | $$ /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$   /$$$$$$ | $$$$$$$\n| $$$$$$$$| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$|____  $$ /$$__  $$| $$__  $$\n| $$__  $$| $$  | $$| $$  \ $$| $$$$$$$$| $$  \__/| $$  \ $$| $$  \__/ /$$$$$$$| $$  \ $$| $$  \ $$\n| $$  | $$| $$  | $$| $$  | $$| $$_____/| $$      | $$  | $$| $$      /$$__  $$| $$  | $$| $$  | $$\n| $$  | $$|  $$$$$$$| $$$$$$$/|  $$$$$$$| $$      |  $$$$$$$| $$     |  $$$$$$$| $$$$$$$/| $$  | $$\n|__/  |__/ \____  $$| $$____/  \_______/|__/       \____  $$|__/      \_______/| $$____/ |__/  |__/\n{' '*11}/$$  | $$| $${' '*27}/$$  \ $${' '*19}| $$\n{' '*10}|  $$$$$$/| $${' '*26}|  $$$$$$/{' '*19}| $$\n{' '*11}\______/ |__/{' '*27}\______/{' '*20}|__/"
logo_c = '\n'.join([*logo.split('\n')[:3], *[" "*5 + l for l in logo.split('\n')[3:9]], *[i.lstrip() for i in logo.split('\n')[9:]]])

env = {
    "locals": None,
    "globals": None,
    "__name__": None,
    "__file__": None,
    "__builtins__": None
}
errorPrint = lambda c, msg, e: c.print(f'{msg} [red][b]{e}[/b][/red]')