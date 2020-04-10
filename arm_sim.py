#!/usr/bin/env python
# coding: utf-8

# In[5]:


# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual
import math
get_ipython().run_line_magic('matplotlib', 'inline')
# 逆運動学の計算
def arm_th(L, p1):
    x, y = p1
    l0, l1 = L
    norm = math.sqrt((x*x) + (y*y))
    th0 = math.atan2(y , x) + math.acos(((x * x) +(y * y)+(l0*l0)- (l1*l1)) / (2*l0*norm))
    th1 = -th0 + math.atan2((y-l0*math.sin(th0)),(x-l0*math.cos(th0)))
    return [th0, th1]

# 順運動学の計算
def arm_pos(L,the):
    l0,l1=L
    th0,th1=the
    x0 = l0 * math.cos(th0)
    y0 = l0 * math.sin(th0)
    # リンク2の手先
    x1 = x0 + l1 * math.cos(th0 + th1)
    y1 = y0 + l1 * math.sin(th0 + th1)
    return np.array([[0,0],[x0,y0],[x1,y1]])

def main():
    # リンク1, 2の長さ
    length = [1,1]
    # グラフ描画位置
    @interact(refPoint_x=(-(length[0]+length[1])/math.sqrt(2),(length[0]+length[1])/math.sqrt(2)),refPoint_y=(-(length[0]+length[1])/math.sqrt(2),(length[0]+length[1])/math.sqrt(2)))
    def draw(refPoint_x=1,refPoint_y=1):
        refPoint=[refPoint_x,refPoint_y]
        #px = #目標位置
        th = arm_th(length, refPoint)#必要角度,引数は4つ
        p = arm_pos(length, th)#アーム位置計算
        fig, ax = plt.subplots()
        plt.axis('equal')
        plt.subplots_adjust(left=0.1, bottom=0.15)
        plt.grid()#グラフ上の設定
        plt.xlim([-2.5, 2.5])
        plt.ylim([-2.5, 2.5])
        # グラフ描画
        graph, = plt.plot(p.T[0], p.T[1])
        graph.set_linestyle('-')
        graph.set_linewidth(10)
        graph.set_marker('o')
        graph.set_markerfacecolor('y')
        graph.set_markersize(15)
    
if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




