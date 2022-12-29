import pandas as pd


model = ['RegNetX-1.6GF', 'RegNetX-3.2GF', 'RegNetX-4.0GF', 'RegNetX-6.4GF', 'RegNetX-8.0GF']
acc1 = [77.0, 78.3, 78.6, 79.2, 79.3]
acc2 = [77.1, 78.2, 78.2, 78.9, 79.0]


import matplotlib.pyplot as plt

plt.style.use('ggplot')

fig, ax = plt.subplots(1, 1, figsize=(10, 5))

color = 'tab:red'
ax.plot(model, acc1, color=color, label='From scratch')
color = 'tab:blue'
ax.plot(model, acc2, color=color, label='Elastic')
ax.set_ylabel('Accuracy (%)', color=color)

ax.legend()

plt.tight_layout()
plt.savefig('scratch_vs_elastic.pdf')
