import numpy as np
import matplotlib.pyplot as plt

gap = 0.01
T_min, T_max = 0.01, 2.4
sep = int(np.floor((T_max - T_min) / gap))
T = np.linspace(T_min, T_max, sep, dtype=np.float32)

path = '../LJ_system/graph_1000/results/sur_prob_thr_'
colors = plt.cm.cool(np.linspace(0, 1, 4))

time_steps = [100, 400, 800, 1000]
data = [np.load(f"{path}{t}.npy", allow_pickle=True) for t in time_steps]

fig, ax = plt.subplots(figsize=(3.1, 3), dpi=300)
markers = ['o', 'v', 's', 'D']
labels = [f'$n(q_6^{{*}})$ = {t}' for t in time_steps]

for i, (d, marker) in enumerate(zip(data, markers)):
    ax.plot(T, d, marker=marker, color=colors[i], fillstyle='none', markersize=6, label=labels[i])

ax.axvline(x=0.75, color='coral', alpha=0.5, linestyle='dashdot')
ax.set_xlim(0.6, 1.0)
ax.set_ylim(-0.1, 1.1)
ax.set_xlabel("$T$ [$\\epsilon/k_B$]", labelpad=10)
ax.set_ylabel("$P_{liq}$", labelpad=10)
ax.legend(loc='best', fontsize=8)
plt.tight_layout()
plt.savefig("../Figure/Fig_3a.png", dpi=300, bbox_inches='tight')
plt.show()
