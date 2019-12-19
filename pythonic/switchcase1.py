'''
@Author: your name
@Date: 2019-12-10 20:49:55
@LastEditTime: 2019-12-10 21:08:30
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\pythonic\switchcase.py
'''
switcher = {
    1:'Sunday',
    2:'Tuesday',
    3:'Wensday',
}


day = 6;
dayname = switcher.get(day, 'Unknown')
print(dayname)