import numpy as np
import matplotlib.pyplot as plt

gap = 0.01
T_min, T_max = 0.01, 2.01
sep = int(np.floor((T_max - T_min) / gap))
T = np.linspace(T_min, T_max, sep, dtype=np.float32)

path = '../LJ_system/graph_10000/'
init_number = 10
colors = plt.cm.cool(np.linspace(0, 1, init_number))

measurements = {i: [] for i in range(10)}

for i in range(init_number):
    for j in range(10):
        filename = f"{path}simulation/md_{i}/answer/dop_bt_{j*50}_{(j+1)*50}.npy"
        measurements[j].append(np.load(filename, allow_pickle=True))

# Compute averages
measure_avg = {j: np.mean(measurements[j], axis=0)[:sep] for j in range(10)}

# Plot results
fig, ax = plt.subplots(figsize=(4.8, 3), dpi=300)
labels = [f'$(n_{j},n_{j+1})=({j*500},{(j+1)*500})$' for j in range(10)]

for j in range(10):
    ax.plot(T, measure_avg[j], color=colors[j], label=labels[j])

ax.set_xlim(0, 2)
ax.set_ylim(0, 1)
ax.set_xlabel("T [$\\epsilon/k_B$]", labelpad=10)
ax.set_ylabel("$\\mathcal{D}_d$", labelpad=10)
ax.legend(bbox_to_anchor=(1.04, 1.03), loc="upper left", fontsize=8)
plt.tight_layout()
plt.savefig("../Figure/Fig_8b.png", dpi=300, bbox_inches='tight')
plt.show()
