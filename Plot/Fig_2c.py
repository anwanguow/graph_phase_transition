#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

gap = 0.01
T_min = 0.01
T_max = 2.01
sep = np.floor((T_max - T_min) / gap).astype(np.int16)
T = np.zeros(sep, dtype="float64")
T[0] = T_min
T[1] = T_min + gap
for i in range(2, sep):
    T[i] = T[i - 1] + gap
T = T.astype(np.float32)

path = '../LJ_system/graph_1000/'
init_number = 10
colors = plt.cm.cool(np.linspace(0, 1, init_number))

measures = [np.zeros((init_number), dtype="object") for _ in range(10)]

for i in range(init_number):
    for j in range(10):
        file_name = path + f"simulation/md_{i}/answer/gap_s_bt_{j*100}_{(j+1)*100}.npy"
        measures[j][i] = np.load(file_name, allow_pickle=True)

measures_avg = [np.sum(measures[j]) / init_number for j in range(10)]
measures_avg = [measure[:sep] for measure in measures_avg]

fig = plt.figure(figsize=(4.6, 3), dpi=300, facecolor='w', edgecolor='k')

for i in range(10):
    plt.plot(T, measures_avg[i], color=colors[i], label=f"$ (n_{{{i}}}, n_{{{i+1}}})=({i*100},{(i+1)*100})$")

plt.legend(bbox_to_anchor=(1.04, 1.03), loc="upper left", fontsize=8)

plt.xlim(0.01, 2)
plt.ylim(0, 0.7)
plt.xticks([0.01, 0.75, 2])
plt.xlabel("$T$ [$\epsilon/k_B$]", labelpad=10)
plt.ylabel("$\mathcal{D}_d$", labelpad=10)

plt.axvline(x=0.75, color='coral', alpha=0.5, linestyle='dashdot')

plt.tight_layout()
plt.savefig("../Figure/Fig_2c.png", dpi=300, bbox_inches='tight')
plt.show()
