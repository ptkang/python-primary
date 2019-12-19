'''
@Author: your name
@Date: 2019-12-01 15:35:04
@LastEditTime: 2019-12-01 15:54:03
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\enum\enum1.py
'''
from enum import Enum
#from enum import IntEnum

class VIP(Enum):
    YELLOW  = 1
    YELLOW_ALIAS  = 1
    GREEN   = 2
    BLACK   = 3
    RED     = 4

class VIP1(Enum):
    YELLOW  = 1
    YELLOW_ALIAS  = 1
    GREEN   = 2
    BLACK   = 3
    RED     = 4

a = VIP.YELLOW
print(a)
print(a.name)
print(a.value)
print(a == VIP.YELLOW)
print(a is VIP.YELLOW)
# print(a < VIP.GREEN)  #TypeError: '<' not supported between instances of 'VIP' and 'VIP'
print(a == VIP1.YELLOW)

for e in VIP:
    print(e)

#print(VIP.__dict__)
print('-'*20)

for e in VIP.__members__.items() :
    print(e)

print('-'*20)
for e in VIP.__members__ :
    print(e)