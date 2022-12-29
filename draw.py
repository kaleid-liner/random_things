import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('./data/mobilenet-v1-op-latency-profiling(1).csv')

n = len(df['Op Type'])

x = np.arange(n)
labels = [str(i) for i in range(n)]

cpu_lat = df['CPU-Only'].to_numpy()
gpu_lat = df['GPU-Only'].to_numpy()

avg_sync = np.average(df['CPU+GPU (Sync, p=0.5)'].to_numpy())

width = 0.4
fig, ax = plt.subplots(figsize=(10, 5))

ax.axhline(avg_sync, linestyle=':', color='black')
ax.text(3, avg_sync + 0.05, 'Communication overhead', color='black', fontsize=25)

bar1 = ax.bar(x - width / 2, cpu_lat, width, label='CPU', fill=False)
bar2 = ax.bar(x + width / 2, gpu_lat, width, label='GPU', fill=False, hatch='///')

ax.set_ylabel('Latency (ms)', fontsize=25)
ax.set_xlabel('Layer index', fontsize=25)
ax.tick_params('y', labelsize=20)
ax.set_xticks(x, labels)
ax.set_xticklabels(labels, fontsize=20)
ax.legend(fontsize=20, loc='upper left')

plt.tight_layout()

plt.savefig('op_profiling.pdf')
