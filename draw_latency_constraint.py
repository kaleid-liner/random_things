import matplotlib.pyplot as plt


x = [4.52, 8.23, 10.3, 13.3]

y = [69.42, 72.81, 72.92, 74.35]

fig, ax = plt.subplots(figsize=(10, 5))

ax.set_xlabel('Latency (ms)', fontsize=25)
ax.set_ylabel('Top-1 Acc. (%)', fontsize=25)

ax.tick_params('y', labelsize=20)
ax.tick_params('x', labelsize=20)

ax.plot(x, y, marker='v', linestyle='dashed', color='black', label='Stretch')
ax.scatter([11.8], [72.39], label='Original', color='black', marker='*', s=200)
ax.set_xlim([3, 15])
ax.legend(fontsize=20)
plt.tight_layout()
plt.savefig('latency_constraint.pdf')
