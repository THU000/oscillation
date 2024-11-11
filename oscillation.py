import numpy as np
#无外力扰动 Euler-Cromer方法

# 初始化参数
x_0 = 1.0        # 初始位置
v_0 = 0.0        # 初始速度
omega_0 = 4.0    # 角频率
gamma = 0.5      # 阻尼系数
A_0 = 1.0          # 初始振幅 无外力扰动
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

# 打开文件准备写入结果
with open('output_1.txt', 'w') as f:
    f.write(f"{t} {x} {x_n} {E}\n")
    t+=dt
    while t < 50:
        # 理论计算 每一次改变初始条件，都要重新计算系数
        x = np.exp(-0.25*t)*(-0.082759*np.cos(3.99218*t)+0.2418521*np.sin(3.99218*t))+0.082759*np.cos(2.0*t)+0.00689655*np.sin(2.0*t)
        #x = np.exp(-0.25*t)*(1.0*np.cos(2.99*t)-0.58537*np.sin(2.99*t))+0.6667*np.sin(3.0*t)

        # 计算加速度
        a_n = -omega_0**2 * x_n - gamma * v_n + A_0*np.cos(omega*t)
        # 更新速度
        v_n += a_n * dt
        # 更新位置
        x_n += v_n * dt
        # 计算能量
        E = 0.5*(v_n**2 + omega_0**2 * x_n**2)
        # 写入时间、理论位置和数值解位置
        f.write(f"{t} {x} {x_n} {E}\n")
        # 更新时间
        t += dt
f.close()
# 模拟完成，结果已保存到文件
print("数据写入完成！")
