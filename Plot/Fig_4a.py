#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

gap = 0.01
T_min = 0.01
T_max = 2.4
sep = np.floor((T_max - T_min) / gap).astype(np.int16)
T = np.zeros(sep, dtype="float64")
T[0] = T_min
T[1] = T_min + gap
for i in range(2, sep):
    T[i] = T[i - 1] + gap
T = T.astype(np.float32)

t_values = [100, 400, 800, 1000]
markers = ['o', 'v', 'D', 's']
colors = ["cyan", "blue", "magenta", "purple"]
lines = []

fig = plt.figure(figsize=(4.2, 4), dpi=300, facecolor='w', edgecolor='k')

for i, (t, marker, color) in enumerate(zip(t_values, markers, colors)):
    data = np.load(f"../LJ_system/graph_1000/results/sur_prob_thr_{t}.npy", allow_pickle=True)
    line, = plt.plot(T, data, marker=marker, color=color, markersize=4, linestyle='-', linewidth=2, markerfacecolor=color, markeredgewidth=2)
    lines.append(line)

plt.legend(handles=lines, labels=[
    '$n(q_6^{*})$ = 100',
    '$n(q_6^{*})$ = 400',
    '$n(q_6^{*})$ = 800',
    '$n(q_6^{*})$ = 1000'
], loc='best', fontsize=10, frameon=True)

plt.axvline(x=0.75, color='coral', alpha=0.5, linestyle='dashdot')

plt.xlim(0.01, 0.4)
plt.xticks([0.01, 0.2, 0.4])

plt.xlabel("Final temperature T ($\epsilon/k_B$)")
plt.ylabel("Survival probability")
plt.tight_layout()
plt.savefig("../Figure/Fig_4a.png", dpi=300, bbox_inches='tight')
plt.show()
