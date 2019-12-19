'''
@Author: your name
@Date: 2019-12-01 15:35:04
@LastEditTime: 2019-12-01 16:02:34
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\enum\enum1.py
'''
from enum import Enum
from enum import IntEnum

class VIP(Enum):
    YELLOW  = 1
    STRING  = 'string'
    GREEN   = 2
    BLACK   = 3
    RED     = 4

a = VIP.YELLOW
print(a)

class INTVIP(IntEnum):
    YELLOW  = 1
    # STRING  = 'string' # ValueError: invalid literal for int() with base 10: 'string'
    GREEN   = 2
    BLACK   = 3
    RED     = 4

a = INTVIP.YELLOW
print(a)