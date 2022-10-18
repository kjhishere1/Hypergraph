import os
import pip
import json
from importlib.util import find_spec

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

""".rstrip()

logo_c = r"""
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

""".rstrip()

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
    typed = ast.literal_eval(value)
    return type(typed) == type_type

def GetCfgPath(cfg_path):
    PATH = os.path.join(os.getenv('APPDATA'), cfg_path)
    CFG = os.path.join(PATH, r"config.json")
    if os.path.exists(PATH):
        return CFG
    else:
        os.mkdir(PATH)
        with open(CFG, 'w', encoding="UTF-8") as file:
            file.write('{}')
        return CFG

def CfgChecker():
    with open(GetCfgPath('hypergraph'), 'r', encoding="UTF-8") as file:
        cfg = file.read()
        cfg = json.loads(cfg)
    for key, value in enumerate(cfg):
        ...