import matplotlib.pyplot as plt

plt.style.use('ggplot')

name = ['ShuffleNetV2_x1', 'RegNet_x_8GF', 'RegNet_x_16GF', 'RegNet_x_32GF']

t4_lats = [0.0019648, 0.0086139, 0.0118481, 0.0232094]
v100_lats = [0.00200283, 0.00549258, 0.00744167, 0.01108162]

t4_energy = [0.096019, 0.601481, 0.824458, 1.61868]
v100_energy = [0.10925476, 0.6594112, 1.02714202, 1.91029155]

t4_power = [e / l for e, l in zip(t4_energy, t4_lats)]
v100_power = [e / l for e, l in zip(v100_energy, v100_lats)]

t4_lats = [l / t4_lats[0] for l in t4_lats]
v100_lats = [l / v100_lats[0] for l in v100_lats]

t4_energy = [l / t4_energy[0] for l in t4_energy]
v100_energy = [l / v100_energy[0] for l in v100_energy]

t4_power = [l / t4_power[0] for l in t4_power]
v100_power = [l / v100_power[0] for l in v100_power]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(name, t4_energy, marker='o', label='energy')
ax1.plot(name, t4_lats, marker='o', label='latency')
ax1.plot(name, t4_power, marker='o', label='power')
ax1.set_title('T4')

ax2.plot(name, v100_energy, marker='o', label='energy')
ax2.plot(name, v100_lats, marker='o', label='latency')
ax2.plot(name, v100_power, marker='o', label='power')
ax2.set_title('V100')
ax2.legend()
plt.tight_layout()

plt.savefig('t4_vs_v100.pdf')
