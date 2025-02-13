import numpy as np
import matplotlib.pyplot as plt

gap = 0.01
T_min = 0.01
T_max = 2.39 + gap
sep = np.floor((T_max - T_min) / gap).astype(np.int16)
T = np.zeros(sep, dtype="float64")
T[0] = T_min
T[1] = T_min + gap
for i in range(2, sep):
    T[i] = T[i - 1] + gap
T = T.astype(np.float32)
path = '../LJ_system/graph_1000/results/sur_prob_thr_'

colors = ["cyan", "blue", "purple", "magenta"]  # 颜色

t_values = [100, 400, 800, 1000]
markers = ['o', 'v', 's', 'D']  # 圆圈、倒三角、方形、菱形
lines = []  # 用于存储图例句柄

fig = plt.figure(figsize=(3.3, 3), dpi=300, facecolor='w', edgecolor='k')

for i, (t, marker, color) in enumerate(zip(t_values, markers, colors)):
    data = np.load(path + str(int(t)) + ".npy", allow_pickle=True)
    line, = plt.plot(T, data, marker=marker, color=color, fillstyle='none', markersize=6, linestyle='-')
    lines.append(line)

plt.legend(handles=lines, labels=[
    '$n(q_6^{*})$ = 100',
    '$n(q_6^{*})$ = 400',
    '$n(q_6^{*})$ = 800',
    '$n(q_6^{*})$ = 1000'
], loc='best', fontsize=8, frameon=True)

plt.axvline(x=0.75, color='coral', alpha=0.5, linestyle='dashdot')

plt.xlim(0.6, 1.0)
plt.ylim(-0.1, 1.1)
plt.xlabel("T [$\epsilon/k_B$]", labelpad=10)
plt.ylabel("P$_{liq}$", labelpad=10)
plt.tight_layout()
plt.savefig("../Figure/Fig_3b.png", dpi=300, bbox_inches='tight')
plt.show()
