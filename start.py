import time
import GameControl
import keyboard

# skills1=['子弹爆炸','连发+','分裂子弹四射']
# skills2=['冰爆伤害','冰系缩减','连环冰暴','破裂小冰弹']
# skills3=['干冰弹连发']
# skills3=['热能爆炸']
runFlag=True

from enum import Enum

class GameMode(Enum):
    e刷关卡 = 1
    e快速消耗体力 = 2

# 设置当前游戏模式
current_mode = GameMode.e快速消耗体力


def stop_program():
    print("暂停程序...")
    global runFlag
    runFlag = False

keyboard.add_hotkey('ctrl+q', stop_program)

count = 1;

while(runFlag):  
    backFlag=False
    print("❤❤❤第%d次循环开始❤❤❤" % count)
    count = count+1

    GameControl.SkipGift()
    GameControl.StartGame()

    if(current_mode==GameMode.e刷关卡):
        while(backFlag==False and runFlag):
            if(GameControl.Elite()==1):
                continue

            backFlag=GameControl.Reback()

            if(backFlag): 
                time.sleep(2)
                break
            else:
                GameControl.SelectSkill()
    
    elif(current_mode==GameMode.e快速消耗体力):     
        print("选技能")
        GameControl.SelectSkill()  #开始游戏后，可能需要选择一次技能      
        time.sleep(0.8)
        print("暂停")
        GameControl.Pause() #点击暂停
        time.sleep(0.3)
        print("点退出")
        GameControl.ExitFight()  #点击退出
        time.sleep(0.3)
        print("点返回")
        GameControl.Reback() #点击返回
        time.sleep(1)
            
            
                

 