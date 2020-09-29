# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:57:18 2020

@author: Administrator
"""
import random
def result(a,b,flag):
    if a=='石头' and b!='剪刀' :
        if b=='布' :
            return flag
        else:
            return 0
    elif a=='剪刀' and b!='布' :
        if b=='石头' :
            return flag
        else:
            return 0
    elif a=='布' and b!='石头' :
        if b=='剪刀' :
            return flag
        else:
            return 0
    else:
        return result(b,a,-1)
AI=['石头','剪刀','布']
for i in range(7):
    player=0
    computer=0
    rs=random.choice(AI)
    var=input("玩家出的是(石头\剪刀\布)：")
    print('电脑出的是(石头\剪刀\布)：'+rs)
    final=result(rs,var,1)
    if final==0:
        print("平局！")
    elif final==1:
        print('玩家胜利！')
        player+=1
    elif final==-1:
        print('电脑胜利！')
        computer+=1
    if(player==4):
        print("")
        print('玩家获得最终的胜利！')
        break
    if(computer==4):
        print("")
        print('电脑获得最终的胜利！')
        break
if(player<=3 and computer<=3):
    print("")
    print('最终的结果是平局！')
    
        