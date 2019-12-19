'''
@Author: your name
@Date: 2019-12-10 20:49:55
@LastEditTime: 2019-12-10 21:05:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\pythonic\switchcase.py
'''
def get_sunday():
    return 'Sunday'

def get_tuesday():
    return 'Tuesday'

def get_wensday():
    return 'Wensday'

def get_default():
    return 'Unknown'

switcher = {
    1:get_sunday(),
    2:get_tuesday(),
    3:get_wensday()
}


day = 6;
dayname = switcher.get(day, get_default())
print(dayname)