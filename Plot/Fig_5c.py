#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

init_number = 3
colors = plt.cm.cool(np.linspace(0, 1, init_number))

gap = 0.01
T = np.arange(0, 1 + gap, gap, dtype=np.float32)

def load_and_process_data(path):
    surv_prob = np.load(f"{path}/swap/surv_prob.npy", allow_pickle=True)
    dop = np.load(f"{path}/swap/dop.npy", allow_pickle=True)
    dop = (dop - np.min(dop)) / (np.max(dop) - np.min(dop))
    return gaussian_filter1d(surv_prob, 1), gaussian_filter1d(dop, 1)

ratios = [5000, 20000, 50000]
data = {r: load_and_process_data(f"../KA_model/ratio_{r}") for r in ratios}

fig, ax1 = plt.subplots(figsize=(4.2, 3), dpi=300, facecolor='w', edgecolor='k')

for i, r in enumerate(ratios):
    ax1.plot(T, data[r][0], color=colors[i], alpha=0.3, linestyle='dotted', label=rf'$P_{{amo,{r}}}$')

ax2 = ax1.twinx()

for i, r in enumerate(ratios):
    ax2.plot(T, data[r][1], color=colors[i], label=rf'$\mathcal{{D}}_{{d,{r}}}$')

ax1.set_ylabel(r"$P_{amo}$", labelpad=10)
ax2.set_ylabel(r"$\mathcal{D}_d$", labelpad=10)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()

fig.legend(lines1 + lines2, labels1 + labels2, loc="center left", bbox_to_anchor=(0.9, 0.5))

ax1.set_xlabel(r"$\chi_B$")
ax1.set_xlim(0, 1)
ax1.set_ylim(-0.05, 1.05)

plt.tight_layout(rect=[0, 0, 0.9, 1])
plt.savefig("../Figure/Fig_5c.png", dpi=300, bbox_inches='tight')
plt.show()
