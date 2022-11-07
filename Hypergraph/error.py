class HGFunctionTypeError(Exception):
    def __init__(self, msg: str):
        if msg == None:
            msg = '함수의 타입이 잘못되었습니다.'
        super().__init__(msg)

class HGSyntaxError(Exception):
    def __init__(self, msg: str):
        if msg == None:
            msg = '함수에서 문법 오류가 발생했습니다.'
        super().__init__(msg)

class HGImaginaryNumberError(Exception):
    def __init__(self, msg: str):
        if msg == None:
            msg = '함수의 값이 허수가 될 수 없습니다.'
        super().__init__(msg) 

class HGUndefinedError(Exception):
    def __init__(self, msg: str):
        if msg == None:
            msg = '정의되지 않은 변수가 호출되었습니다.'
        super().__init__(msg)

class HGZeroDivisionError(Exception):
    def __init__(self, msg: str):
        if msg == None:
            msg = '분모가 0이 될 수 없습니다.'
        super().__init__(msg)

class HGOverflowError(Exception):
    def __init__(self, msg: str):
        if msg == None:
            msg = '숫자 값이 너무 큽니다.'
        super().__init__(msg) 

class HGException(Exception):
    def __init__(self, msg: str):
        if msg == None:
            msg = '알 수 없는 오류가 발생했습니다.'
        super().__init__(msg)