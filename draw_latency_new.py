import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def read_number(s):
    if isinstance(s, str):
        return float(s[:s.find("(")])
    else:
        return s


plt.style.use("seaborn-whitegrid")
width = 10
plt.figure(figsize=(width, 5))
ylim = 50
plt.ylim(0, ylim)

df = pd.read_csv("stretch_mi9.csv")

xlabels = df["Mi9"].to_numpy()
devices = df.keys().to_list()[1:]
devices = [d.upper() for d in devices]

n_models = df.shape[0]
xbr = np.arange(0, 2 * n_models, 2)
colors = ["C0", "C1", "C2", "C3", "C4", "C5", "C6"]
bar_width = 0.25
for i, (device, lats) in enumerate(df.iteritems()):
    if i == 0:
        continue
    lats = [read_number(lat) for lat in lats]
    for lat, x in zip(lats, xbr):
        if lat > ylim:
            plt.gcf().text(xbr / width, 0.95, str(int(lat)))
    plt.bar(xbr, lats, color=colors[i-1], width=bar_width, label=device.upper())
    xbr = xbr + bar_width

xbr = np.arange(0, 2 * n_models, 2)
plt.xticks(xbr + n_models / 2 * bar_width, xlabels)

plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.102), ncol=7, fancybox=True)
plt.subplots_adjust(top=0.9)
plt.savefig('all_latency.png')

plt.tight_layout()
