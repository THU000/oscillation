#精确确定临界gamma
import numpy as np
import math

# 初始化参数
x_0 = 1.0        # 初始位置
v_0 = 0.0        # 初始速度
omega_0 = 3.0    # 角频率
gamma = 5.0      # 阻尼系数
d_gamma = 0.0001    # 阻尼系数步长

A_0 = 0.0          # 初始振幅 无外力扰动
omega = 2.0      # 角频率
dt = 0.02        # 时间步长

# 初始化变量
t = 0.0
x_n = x_0
v_n = v_0
a_n = -8.0
#理论解初始值
x = 1.0
#初始能量
E = 0.5*(v_n**2 + omega_0**2 * x_n**2)

w_d = 0.5*math.sqrt(36-gamma**2)
signal = 0

while gamma < 6:
    while t < 10:
         # 理论计算 每一次改变初始条件，都要重新计算系数
        #x = np.exp(-0.25*t)*(-0.082759*np.cos(3.99218*t)+0.2418521*np.sin(3.99218*t))+0.082759*np.cos(2.0*t)+0.00689655*np.sin(2.0*t)
        x = np.exp(-0.5*gamma*t)*(np.cos(w_d*t)+0.5*gamma*np.sin(2.99*t)/w_d)

        # 计算加速度
        a_n = -omega_0**2 * x_n - gamma * v_n + A_0*np.cos(omega*t)
        # 更新速度
        v_n += a_n * dt
        # 更新位置
        x_n += v_n * dt
        if x_n < 0:
            x_n = x_0
            v_n = v_0
            a_n = -8.0
            t = 0.0
            gamma += d_gamma
            w_d = 0.5*math.sqrt(36-gamma**2)
            break
        
        # 更新时间
        t += dt
        if t >= 10:
            signal = 1
            break
    if signal != 0:
        print(gamma)
        break