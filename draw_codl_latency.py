import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib


def read_number(s):
    if isinstance(s, str):
        return float(s[:s.find("(")])
    else:
        return s

matplotlib.rcParams.update({'font.size': 20})
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.style.use("tableau-colorblind10")

width = 10
plt.figure(figsize=(width, 5))
ylim = 50
plt.ylim(0, ylim)
plt.ylabel("Latency (ms)")

colors = ["lightcoral", "lightsalmon", "peachpuff", "skyblue", "orange", "pink", "turquoise"]
hatches = ["", "\\", "/", "|", "-", "x", "."]
bar_width = 0.25
bar_spacing = 2

start = 0
all_xticks = []
all_xlabels = []

device_index = {"CPU": 0, "GPU": 1, "CoDL": 2, "Stretch": 3}

platform_dict = {
    "mi9": "Xiaomi 9",
    "pixel6": "Pixel 6",
    "mi11": "Xiaomi 11 Pro",
}

for platform in ["mi9", "mi11"]:
    if platform != "mi9":
        plt.axvline(start - 2 * bar_width, color="gray", linestyle="--")

    df = pd.read_csv("codl_{}.csv".format(platform))
    xlabels = [label for label in df.iloc[:, 0].to_numpy()]
    devices = df.keys().to_list()[1:]

    n_models = df.shape[0]
    total_width = (len(devices) + bar_spacing) * bar_width
    xbr = np.arange(start, start + total_width * n_models, total_width)
    for i, (device, lats) in enumerate(df.iteritems()):
        if i == 0:
            continue
        lats = [read_number(lat) for lat in lats]
        for lat, x in zip(lats, xbr):
            if lat > ylim:
                plt.text(x, ylim + 1, "{:.3f}".format(lat), horizontalalignment="center")
        index = device_index[device]
        plt.bar(xbr, lats, color=colors[index], hatch=hatches[index], width=bar_width, label=device, edgecolor="grey")
        xbr = xbr + bar_width
    
    plt.text(start + total_width * n_models / 2, -15, platform_dict[platform], horizontalalignment="center", fontsize="20")    

    xbr = np.arange(start, start + total_width * n_models, total_width)
    xticks = xbr + (n_models - 1) / 2 * bar_width
    all_xticks = np.concatenate((all_xticks, xticks))
    all_xlabels = np.concatenate((all_xlabels, xlabels))
    start += total_width * n_models


plt.xticks(all_xticks, all_xlabels)

handles, labels = plt.gca().get_legend_handles_labels()
handles, labels = handles[:4], labels[:4]
plt.legend(handles, labels, bbox_to_anchor=(0, 1.05, 1, 0.105), ncol=7, fancybox=True, mode="expand")

plt.tight_layout()

plt.savefig('codl_latency.png')
plt.savefig('codl_latency.pdf')

