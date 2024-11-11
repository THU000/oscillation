#此画图程序为本题第1至3问的位置和能量曲线
import numpy as np
import matplotlib.pyplot as plt

# 加载数据
data5 = np.loadtxt('gamma_5.txt')
data4 = np.loadtxt('gamma_4.txt')
data6 = np.loadtxt('gamma_6.txt')

# 提取时间、理论值x和数值解x_n
t = data5[:, 0]
#x = data[:, 1]
x_n_5 = data5[:, 2]
x_n_4 = data4[:, 2]
x_n_6 = data6[:, 2]
# E = data[:, 3]

# 绘图
plt.figure(figsize=(10, 6))

#画出能量曲线
# plt.plot(t, E, label='Energy', color='blue', linewidth=2)
# plt.xlabel('Time')
# plt.ylabel('Energy')
# plt.title('Energy of the Oscillator')



#画出余弦函数
#plt.plot(t, 0.25*np.cos(2.0 * t), label='cos(2.0*t) x(t)', color='black', linewidth=2)
#plt.plot(t, x, label='Theoretical Solution x(t)', color='green', linewidth=2)
plt.plot(t, x_n_4, label='gamma=4 x_n(t)', color='blue', linewidth=2)
plt.plot(t, x_n_5, label='gamma=5 x_n(t)', color='red', linewidth=2)
plt.plot(t, x_n_6, label='gamma=6 x_n(t)', color='green', linewidth=2)
plt.title('Different gamma')
plt.xlabel('Time (t)')
plt.ylabel('Position (x)')

plt.legend()
plt.grid()
plt.xlim(1.5, 3.0)
plt.ylim(-0.08, 0.1)
plt.show()
