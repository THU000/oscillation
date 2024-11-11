#此画图程序为本题第1至3问的位置和能量曲线
import numpy as np
import matplotlib.pyplot as plt

# 加载数据
data = np.loadtxt('output_1.txt')

# 提取时间、理论值x和数值解x_n
t = data[:, 0]
x = data[:, 1]
x_n = data[:, 2]
E = data[:, 3]

# 绘图
plt.figure(figsize=(10, 6))

#画出能量曲线
plt.plot(t, E, label='Energy', color='blue', linewidth=2)
plt.xlabel('Time')
plt.ylabel('Energy')
plt.title('Energy of the Oscillator')

#画出余弦函数
# plt.plot(t, 0.25*np.cos(2.0 * t), label='cos(2.0*t) x(t)', color='black', linewidth=2)
# plt.plot(t, x, label='Theoretical Solution x(t)', color='green', linewidth=2)
# plt.plot(t, x_n, label='Numerical Solution x_n(t)', color='red', linestyle='--', linewidth=2)
# plt.title('Comparison of Theoretical and Numerical Solutions under Forced Perturbation')
# plt.xlabel('Time (t)')
# plt.ylabel('Position (x)')

plt.legend()
plt.grid()
plt.xlim(30, 40)
plt.ylim(0, 0.25)
plt.show()
