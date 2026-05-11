from functools import reduce
import operator
from pycheevos.core.value import MemoryExpression


from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.models.rich_presence import RichPresence
import csv
import json

if __name__=="__main__":
    player: MemoryExpression = dword(0x1000) >> dword(0x4) >> dword(0x1c)
    hp: MemoryExpression = player >> dword(0x10)

    # print(reduce(operator.add, [
    #     dword(100 + i * 4) * i for i in range(10)
    # ]))

    # Operator "/" not supported for types "MemoryExpression" and "ConstantValue"
    # print(measured(hp / value(2)))

    # Before:   2*I:0xX1000_I:0xX0004_I:0xX001c_M:0xX0010 (Invalid condition)
    # Expected: I:0xX1000_I:0xX0004_I:0xX001c_M:0xX0010*2
    # print(measured(hp * value(2)))
