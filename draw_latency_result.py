import matplotlib.pyplot as plt
import numpy as np


cpu_lat = [47.23, 85.04, 14.94, 70.83, 37.15, 15.11]
gpu_lat = [12.62, 22.88, 11.80, 47.58, 21.53, 7.63]
pal_lat = [8.51, 14.52, 8.23, 32.86, 15.06, 6.52]

labels = ['ResNet32', 'ResNet56', 'ShuffleNetV2', 'ShuffleNetV2 (x2)', 'MobileNetV2', 'MobileNetV2 (0.5)']

x = np.arange(6)

width=0.25

fig, ax = plt.subplots(figsize=(15, 7))

bar1 = ax.bar(x - width, cpu_lat, width, label='Original (CPU)', color='dimgray', edgecolor='black')
bar2 = ax.bar(x, gpu_lat, width, label='Original (GPU)', color='darkgrey', edgecolor='black')
bar3 = ax.bar(x + width, pal_lat, width, label='Stretched (CPU + GPU)', fill=False)

ax.set_ylabel('Latency (ms)', fontsize=30)
ax.tick_params('y', labelsize=25)
ax.set_xticks(x, labels)
ax.set_xticklabels(labels, fontsize=30, rotation=15)
ax.legend(fontsize=25)

plt.tight_layout()
plt.savefig('cifar100_latency.pdf')
