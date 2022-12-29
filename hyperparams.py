import pandas as pd


df = pd.read_csv('onnx_kernel_model_compare_batch_1.csv')
df = df[df['model'].str.contains('regnet_x')]
df = df.sort_values(by=['accuracy'])

model = df['model'].to_numpy()
acc = df['accuracy'].to_numpy()
energy = df['energy_model'].to_numpy()
latency = df['latency_model'].to_numpy()


import matplotlib.pyplot as plt

plt.style.use('ggplot')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 4))

color = 'tab:red'
ax1.plot(acc, energy, color=color)
ax1.set_xlabel('Accuracy (%)')
ax1.set_ylabel('Energy (J)', color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_title('RegNetX')
ax1.set_ylim([-0.1, 2.10])

color = 'tab:blue'
ax12 = ax1.twinx()
ax12.plot(acc, latency, color=color)
ax12.tick_params(axis='y', labelcolor=color)
ax12.xaxis.grid(False)
ax12.yaxis.grid(False)
ax12.set_ylim([-0.001, 0.021])

for i in range(len(model)):
    if i >= len(model) - 2:
        ax1.annotate(model[i], (acc[i] - 1.2, energy[i] + 0.002))
    else:
        ax12.annotate(model[i], (acc[i] - 0.2, latency[i] - 0.002))

df = pd.read_csv('onnx_kernel_model_compare_batch_1.csv')
df = df[df['model'].str.contains('resnet')]
df = df.sort_values(by=['accuracy'])

model = df['model'].to_numpy()
acc = df['accuracy'].to_numpy()
energy = df['energy_model'].to_numpy()
latency = df['latency_model'].to_numpy()

color = 'tab:red'
ax2.plot(acc, energy, color=color)
ax2.set_xlabel('Accuracy (%)')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_title('ResNet')
ax2.set_ylim([-0.1, 2.20])

color = 'tab:blue'
ax22 = ax2.twinx()
ax22.set_ylabel('Latency (ms)', color=color)
ax22.plot(acc, latency, color=color)
ax22.tick_params(axis='y', labelcolor=color)
ax22.xaxis.grid(False)
ax22.yaxis.grid(False)
ax22.set_ylim([-0.001, 0.022])

for i in range(len(model)):
    if i >= len(model) - 2:
        ax2.annotate(model[i], (acc[i] - 2, energy[i] + 0.002))
    else:
        ax22.annotate(model[i], (acc[i] - 0.2, latency[i] - 0.002))

plt.tight_layout()
plt.savefig('hyperparams.pdf')
