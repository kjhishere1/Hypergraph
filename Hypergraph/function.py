import re
import ast

from math import sqrt


class Function:
    def __init__(self, function: str):
        self.function = function

    def styler(self, pattern, match, function):
        expression = self.function

        Exp = re.findall(pattern, expression)
        for N in Exp:
            N = eval(N)
            print(N)
            try:
                expression = expression.replace(match.format(N), f"{function(complex(N).real)}")
            except ValueError:
                expression = expression.replace(match.format(N), f"{function.__name__}({N})")

        if expression == self.function:
            return True
        else:
            self.function = expression
            return False

    def do(self):
        EXPS = [
            (r"(?<=\|)(.*?)(?=\|)", "|{}|", abs),
            (r"(?<=abs\()(.*?)(?=\))", "abs({})", abs),
            (r"(?<=sqrt\()(.*?)(?=\))", "sqrt({})", sqrt)
        ]

        while True:
            check = []
            for point in EXPS:
                check.append(
                    self.styler(*point)
                )
            
            if list(set(check)) == [True]:
                return self.function

print(Function('sqrt(abs(-10) + |-3.14|)').do())