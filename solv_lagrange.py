#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sympy as sp
import numpy as np

#JupyterNotebookを使っている場合数式を自然数表示
sp.init_printing()

#変数を設定
##時間,重力加速度
t,g=sp.symbols('t g')

## 一般化座標 角度
q0, q1 = sp.symbols('q_0 q_1', cls=sp.Function)
q=[q0(t), q0(t)+q1(t)]#

## リンク端~リンク重心の長さ
lg0, lg1 = sp.symbols('l_{g0} l_{g1}')
lg=[lg0,lg1]

## リンク端~リンク端の長さ(=2*lg)
l0,l1= sp.symbols('l_0 l_1')
l=[l0,l1]

##重心での重さ
m0, m1 = sp.symbols('m_0 m_1')
m=[m0,m1]

##慣性モーメント
I0, I1 = sp.symbols('I_0 I_1')
I=[I0,I1]

##粘性摩擦関数
d0, d1 = sp.symbols('d_0 d_1')
d=[d0,d1]

##重心位置x,yに関する条件
x0=lg[0]*sp.cos(q[0])
y0=lg[0]*sp.sin(q[0])
dx0=sp.diff(x0,t)
dy0=sp.diff(y0,t)
x1=l[0]*sp.cos(q[0])+lg[1]*sp.cos(q[1])
y1=l[0]*sp.sin(q[0])+lg[1]*sp.sin(q[1])
dx1=sp.diff(x1,t)
dy1=sp.diff(y1,t)

pos0 =[x0,y0]
pos1 =[x1,y1]
vel0 =[dx0,dy0]
vel1 =[dx1,dy1] 
pos =[pos0,pos1]
vel =[vel0,vel1]

# 運動エネルギーT,位置エネルギーU,損失エネルギーD
T=[]
U=[]
D=[]
for i in range(len(q)):
    T.append(sp.simplify(m[i]*(vel[i][0]**2+vel[i][1]**2)*(1/2)+(1/2)*I[i]*sp.diff(q[i],t)**2))
    #print('T_'+str(i)+'='+sp.latex(T[i]))
    U.append(sp.simplify(m[i]*g*pos[i][1]))
    #print('U_'+str(i)+'='+sp.latex(U[i]))
    if i==0:
        qi=q0(t)
    else:
        qi=q1(t)
    D.append(sp.simplify((d[0]*sp.diff(qi,t)**2)/2))
    #print('D_'+str(i)+'='+sp.latex(D[i]))

#オイラーラグランジュ方程式解く関数を定義
def EulerLagrange(q,T,U,D):
    print(q)
    T_dq=sp.simplify(sp.diff(T[0]+T[1],sp.diff(q,t)))
    T_tdq=sp.simplify(sp.diff(T_dq,t))
    T_q=sp.simplify(sp.diff(T[0]+T[1],q))
    U_q=sp.simplify(sp.diff(U[0]+U[1],q))
    D_dq=sp.simplify(sp.diff(D[0]+D[1],sp.diff(q,t)))
    res=sp.simplify(T_tdq-T_q+U_q+D_dq)
    #print('frac{\partial T}{\partial \dot{q}}='+sp.latex(T_dq))#latex表記 \fがおかしくなる。
    #print('frac{d}{dt}(frac{\partial T}{\partial \dot{q}})='+sp.latex(T_tdq))
    #print('frac{\partial T}{\partial q}='+sp.latex(T_q))
    #print('frac{\partial U}{\partial q}='+sp.latex(U_q))
    #print('frac{\partial D}{\partial \dot{q}}='+sp.latex(D_dq))
    return res

#運動方程式
f=[]
for i in range(len(q)):
    if i ==0:
        qi=q0
    else:
        qi=q1
    f.append(EulerLagrange(qi(t),T,U,D))
    print('f='+sp.latex(f[i]))


# In[ ]:




