'''
@Author: your name
@Date: 2019-12-01 15:35:04
@LastEditTime: 2019-12-01 16:07:14
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\enum\enum1.py
'''
# 枚举为单例模式，即枚举不能被实例化的
# 23种设计模式: 单例模式

from enum import Enum
from enum import IntEnum,unique # unique为修饰器

@unique
class INTVIP(IntEnum):
    YELLOW  = 1
    # STRING  = 'string' # ValueError: invalid literal for int() with base 10: 'string'
    YELLOW_ALIAS   = 1 # ValueError: duplicate values found in <enum 'INTVIP'>: YELLOW_ALIAS -> YELLOW
    GREEN   = 2
    BLACK   = 3
    RED     = 4

a = INTVIP.YELLOW
print(a)