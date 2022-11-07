from .error import HGException as Exception
from .error import HGFunctionTypeError as FunctionTypeError
from .error import HGImaginaryNumberError as ImaginaryNumberError
from .error import HGOverflowError as OverflowError
from .error import HGSyntaxError as SyntaxError
from .error import HGUndefinedError as UndefinedError
from .error import HGZeroDivisionError as ZeroDivisionError

from .hypergraph import Hypergraph
Range = Hypergraph._BetterRange
Parse = Hypergraph.Parse