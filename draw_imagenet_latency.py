import matplotlib.pyplot as plt
import numpy as np


cpu_lat = [258.64, 343.22, 13.83, 21.98]
gpu_lat = [74.89, 91.73, 11.66, 9.92]
pal_lat = [50.51, 66.78, 7.45, 7.94]

labels = ['ResNet34', 'ResNet50', 'ShuffleNetV2', 'MobileNetV2']

x = np.arange(4)

width=0.25

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 7), sharex=True, gridspec_kw={'height_ratios': [1, 3]})

ax1.bar(x - width, cpu_lat, width, label='Original (CPU)', color='dimgray', edgecolor='black')
ax1.bar(x, gpu_lat, width, label='Original (GPU)', color='darkgrey', edgecolor='black')
ax1.bar(x + width, pal_lat, width, label='Stretched (CPU + GPU)', fill=False)

ax2.bar(x - width, cpu_lat, width, label='Original (CPU)', color='dimgray', edgecolor='black')
ax2.bar(x, gpu_lat, width, label='Original (GPU)', color='darkgrey', edgecolor='black')
ax2.bar(x + width, pal_lat, width, label='Stretched (CPU + GPU)', fill=False)

ax2.set_ylim(0, 101)
ax1.set_ylim(220, 360)
ax2.spines.top.set_visible(False)
ax1.spines.bottom.set_visible(False)
ax1.tick_params(labeltop=False)

ax1.axhline(220, color='black', linestyle='dashed')
ax2.axhline(101, color='black', linestyle='dashed')

ax1.xaxis.tick_top()
ax2.xaxis.tick_bottom()

ax2.set_ylabel('Latency (ms)', fontsize=30)
for ax in [ax1, ax2]:
    ax.tick_params('y', labelsize=25)
    ax.set_xticks(x, labels)
    ax.set_xticklabels(labels, fontsize=30)

ax2.legend(fontsize=30)

d = .5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=15,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

plt.tight_layout()
plt.savefig('imagenet_latency.pdf')