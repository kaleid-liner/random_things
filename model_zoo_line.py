import pandas as pd


df = pd.read_csv('onnx_kernel_model_compare_batch_1.csv')
df = df[df['model'].str.contains('mobilenet|resnet|regnet_x|efficientnet|shufflenet')]
df = df.sort_values(by=['accuracy'])

model = df['model'].to_numpy()
acc = df['accuracy'].to_numpy()
energy = df['energy_model'].to_numpy()
latency = df['latency_model'].to_numpy()


import matplotlib.pyplot as plt

plt.style.use('ggplot')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

color = 'tab:red'
ax1.plot(model, energy, color=color)
ax1.set_ylabel('Energy (J)', color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticklabels(model, fontsize=8, rotation=45, ha='right')
ax1.set_title('Energy vs Accuracy')
ax1.xaxis.grid(False)
ax1.yaxis.grid(False)

color = 'tab:blue'
ax12 = ax1.twinx()
ax12.set_ylabel('Accuracy (%)', color=color)
ax12.plot(model, acc, color=color)
ax12.tick_params(axis='y', labelcolor=color)
ax12.xaxis.grid(False)
ax12.yaxis.grid(False)

df = df.sort_values(by=['latency_model'])

model = df['model'].to_numpy()
energy = df['energy_model'].to_numpy()
latency = df['latency_model'].to_numpy()

color = 'tab:red'
ax2.plot(model, energy, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_xticklabels(model, fontsize=8, rotation=45, ha='right')
ax2.set_title('Energy vs Latency')
ax2.xaxis.grid(False)
ax2.yaxis.grid(False)

color = 'tab:blue'
ax22 = ax2.twinx()
ax22.set_ylabel('Latency (ms)', color=color)
ax22.plot(model, latency, color=color)
ax22.tick_params(axis='y', labelcolor=color)
ax22.xaxis.grid(False)
ax22.yaxis.grid(False)

plt.tight_layout()
plt.savefig('model_zoo.pdf')
