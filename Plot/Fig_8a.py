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
path = '../LJ_system/graph_10000/'

for i in range(2, sep):
    T[i] = T[i - 1] + gap
T = T.astype(np.float32)

init_number = 10
colors = plt.cm.cool(np.linspace(0, 1, init_number + 1))

measures = [np.zeros((init_number), dtype="object") for _ in range(11)]

for i in range(init_number):
    for j in range(11):
        file_name = path + f"simulation/md_{i}/answer/sop_{j*50}.npy"
        measures[j][i] = np.load(file_name, allow_pickle=True)

measures_avg = [np.sum(measures[j]) / init_number for j in range(11)]
measures_avg = [measure[:sep] for measure in measures_avg]

fig = plt.figure(figsize=(4, 3), dpi=300, facecolor='w', edgecolor='k')

for i in range(11):
    plt.plot(T, measures_avg[i], color=colors[i], label=f"$n_{{{i}}}={i*500}$")

plt.legend(bbox_to_anchor=(1.04, 1.03), loc="upper left", fontsize=8)

plt.xlim(0, 2)
plt.ylim(0, 1.6)
plt.xlabel("$T$ [$\epsilon/k_B$]", labelpad=10)
plt.ylabel("$\mathcal{D}_s$", labelpad=10)

plt.tight_layout()
plt.savefig("../Figure/Fig_8a.png", dpi=300, bbox_inches='tight')
plt.show()
