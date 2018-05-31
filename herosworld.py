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
 - 文件存档
 
"""

import random
import os



print("welcome hero\'s worild !")
msg1 = """
     _____________
    │'a' for left │
    │'d' for right│
    │'a' for check│
    └-------------┘     
       """


msg2 = ', you are here!'
player1 = {}
map1 =['#','#','#','#','#','#','#','#','#']
msg_map1=   ''    
name1 = input ("input your name: ")


def apple(HP):
    HP += 10
    print("You found an apple !!!")
    input()
    return HP

def bomb(HP):
    HP -= 10
    print("You found a boom ... T.T  ")
    input()
    return HP
event0 = [apple,bomb]

if not name1:     name1 = 'player1'
player1['name'] = name1   

# check is there if has save file 
#sav= open("d:\\hero.sav",'r+')
#sav_temp = sav.load()
#print("读取档案:  ",sav_temp)

player1['HP'] = 100
point_p1=random.randint(0,9)


while True:
    os.system("cls\n")
    print(('%s' + msg2) % player1['name'])
    map1[point_p1] = "*"
    print("".join(map1)) 
    
    move = input("""
                 
      'a' for left move
      'b' for right move
      'r' for check status
      hit key to control:    
      
      """)    
    if (move == 'a') and (point_p1 > 0):
          event1 = random.randint(0,9)
          map1[point_p1]= '#'
          point_p1 -=1
          print("".join(map1))
          
    elif (move=='d') and (point_p1<8):
          event1 = random.randint(0,9)
          map1[point_p1] = '#'
          point_p1 += 1
          map1[point_p1] = '*'

    elif (move=='r'):

          print("""英雄当前状态: " 
                姓名:  %s
                H  P:  %d
                """ % (player1['name'],player1['HP']))
          input()
         
    elif move=='q' :
         tuichu = input('are you confirm to quit?(y/n):' )
         if tuichu == 'y':
             sav=open("hero.sav",'w')
             
             sav.writelines(player1)
             sav.close()
             break
         else: 
             continue
    else:
        os.system("cls\n")
        print(msg1,'\n')
        input()
        continue
    
      #炸弹,苹果

    if point_p1 == event1:
        player1['HP'] = random.choice(event0)(player1['HP'])

        print("HP: %d" % player1['HP'])
        
print(player1)









