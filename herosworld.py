# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
4#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""

"""  这是一个 英雄无敌的游戏
 -加入了 随机的 吃苹果 踩雷事件 
 -dos屏幕下自动清除内容刷新
 -用pickle 模块保存游戏进度
 
"""

import random
import os      #
import pickle  #增加存档功能


print("welcome hero\'s worild !")
msg1 = """
     _____________
    │'a' for left │
    │'d' for right│
    │'r' for check│
    │'q' for quit │
    └-------------┘     
       """


msg2 = ', 你在地图上的当前位置(*)!'
player1 = {}
map1 =['#','#','#','#','#','#','#','#','#']
msg_map1=   ''    

# 输入名字后 初始化HP,point信息
name1 = input ("input your name: ")
if not name1:     name1 = 'player1'
player1['name'] = name1  
player1['HP'] = 100
player1['point']=random.randint(0,9)

# 游戏存档调取,如果有记录 重新初始化HP,point信息
alluser = []
if os.path.isfile('hero.sav'):
    with open('hero.sav','rb') as sav:   # 读档 rb 模式
        alluser = pickle.load(sav)
        for i in alluser:
            if i['name'] == name1:
                print(i)
                q = input("系统中有存档记录,是否读取(y/n) :")
                if q == 'y':
                    player1['HP']= i['HP']
                    player1['point'] = i['point']
                    alluser.remove(i)

 


def apple(HP):
    HP1 = 0
    HP1 = random.randint(0,9)
    HP += HP1
    print("捡到一个鸡腿 !!! \n 生命值增加了{0}: {1}".format(HP1,HP))
    input("请按回车继续")
    return HP

def bomb(HP):
    HP1 = 0
    HP1 = random.randint(1,20)*2
    HP -= HP1 
    print("被炸弹咋飞了你 ... T.T ,损失{0}生命值: {1} ".format(HP1,HP))
    input("请按回车继续")
    return HP
event0 = [apple,bomb]
event1 = 0


# check is there if has save file 
#sav= open("d:\\hero.sav",'r+')
#sav_temp = sav.load()
#print("读取档案:  ",sav_temp)


#print(type(player1))
#input()

while player1['HP'] > 0:
    os.system("cls\n")
    print(('%s' + msg2) % player1['name'])
    map1[player1['point']] = "*"
    print("当前生命值: {0}".format(player1['HP']),"\n\n\n")
    print("".join(map1)) 

    
    move = input("""
                 
     _____________
    │'a' for left │
    │'d' for right│
    │'r' for check│
    │'q' for quit │
    └-------------┘     
    
  hit key to control:    
      
      """)    
    if (move == 'a') and (player1['point'] > 0):
          event1 = random.randint(0,9)
          map1[player1['point']]= '#'
          player1['point'] -=1
          print("".join(map1))
          if player1['point'] == event1:
              player1['HP'] = random.choice(event0)(player1['HP'])
          
    elif (move=='d') and (player1['point']<8):
          event1 = random.randint(0,9)
          map1[player1['point']] = '#'
          player1['point'] += 1
          map1[player1['point']] = '*'
          if player1['point'] == event1:
              player1['HP'] = random.choice(event0)(player1['HP'])
              
    elif (move=='r'):

          print("""
    英雄当前状态: 
        昵称:  {0}
        生命:  {1}
        位置:  {2}
                """.format(player1['name'],player1['HP'],player1['point']))
          input()
         
    elif move=='q' :
         q1 = input('确定要退出江湖吗?(y/n):' )
         if q1 == 'y':
             print(player1)
             q2 = input('是否保存记录?(y/n):' )
             if q2 == 'y':
                 for i in alluser:  #存档之前清理记录
                     if i['name']== player1['name']:
                         alluser.remove(i)
                         
                 alluser.append(player1)
                 with open("hero.sav",'wb') as sav:
                     pickle.dump(alluser,sav)
                 print("保存记录成功!")
                 input("请按回车继续")
                 break
             else: 
                 break
         else:
#        os.system("cls\n")
#        print(msg1,'\n')
#        input()
            continue
    
      #炸弹,苹果



else:
    print("你挂了")        
print(player1)
input()








