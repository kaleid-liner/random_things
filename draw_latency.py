import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-whitegrid")
plt.figure(figsize=(10, 5))

r34 = [21.801, 36.756, 19.543, 14.678, 11.789, 9.541]
r50 = [30.021, 34.917, 26.438, 19.542, 17.804, 14.201]
rgx16 = [27.820, 45.843, 27.917, 19.749, 16.534, 13.712]
rgx4 = [37.946, 75.389, 44.872, 29.713, 24.436, 20.302]

xlabels = ["ResNet34", "ResNet50", "RegNetX-1.6GF", "RegNetX-4GF"]
devices = ["cpu", "gpu", "dsp", "cpu+gpu", "cpu+dsp", "cpu+gpu+dsp"]

xbr = np.arange(0, 8, 2)
colors = ["C0", "C1", "C2", "C3", "C4", "C5"]
bar_width = 0.25
for i, br in enumerate(zip(devices, r34, r50, rgx16, rgx4)):
    br = list(br)
    print(xbr)
    plt.bar(xbr, br[1:], color=colors[i], width=bar_width, label=br[0])
    xbr = xbr + bar_width

plt.xticks(np.arange(0, 8, 2) + 3 * bar_width, xlabels)

plt.legend()
plt.savefig('all_latency.png')
