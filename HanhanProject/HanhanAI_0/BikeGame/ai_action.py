'''
创建人：周智圆
创建时间：2019.8.21
最后一次修改时间：2019.8.23
'''

#AI操作函数
#action[left,right,spacebar,]:1表示执行，0表示不执行
from win32con import *
from HanhanAI_0.Interaction.keyboard_forgame import *

def game_ai_action(action):
    if action[0]==1:
        print(gl.HANDLE,"执行了0000000000000000000000000000000000000000000000000000000000")
        key_tap(VK_LEFT)
    elif action[1]==1:
        print(gl.HANDLE,"执行了111111111111111111111111111111111111111111111111111111111")
        key_tap(VK_RIGHT)
    elif action[2]==1:
        print(gl.HANDLE,"执行了222222222222222222222222222222222222222222222222222222222")
        key_tap(VK_SPACE)
    elif action[3]==1:
        print(gl.HANDLE,"执行了333333333333333333333333333333333333333333333333333333333")
