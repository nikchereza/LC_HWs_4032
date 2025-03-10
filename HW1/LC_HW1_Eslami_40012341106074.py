import numpy as np
import matplotlib.pyplot as plt

# ضرایب معادله
M_alpha = -8.790  # s^(-2)
M_q = -2.075  # s^(-1)
M_delta_E = -11.87  # s^(-2)

# پارامترهای شبیه‌سازی
h = 0.01  # گام زمانی
t_max = 5  # مدت زمان شبیه‌سازی
t = np.arange(0, t_max, h)  # بردار زمان

# مقادیر ورودی δ_E
delta_E_values = [-5, 0, 10]  # درجه

# شرایط اولیه
theta_0 = 0
theta_dot_0 = 0

# حل معادله برای هر مقدار δ_E
plt.figure(figsize=(10, 6))

for delta_E in delta_E_values:
    theta = np.zeros_like(t)
    theta_dot = np.zeros_like(t)
    
    # مقدار اولیه
    theta[0] = theta_0
    theta_dot[0] = theta_dot_0
    
    # روش اویلر
    for i in range(len(t) - 1):
        theta_ddot = M_alpha * theta[i] + M_q * theta_dot[i] + M_delta_E * np.radians(delta_E)
        theta_dot[i + 1] = theta_dot[i] + h * theta_ddot
        theta[i + 1] = theta[i] + h * theta_dot[i]
    
    # رسم نمودار
    plt.plot(t, theta, label=f'δ_E = {delta_E}°')

plt.xlabel('Time(Sec)')
plt.ylabel('Pitch Angle θ (Radian)')
plt.title('Sys response to different inputs')
plt.legend()
plt.grid()
plt.show()
