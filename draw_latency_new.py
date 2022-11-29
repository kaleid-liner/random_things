import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib


def read_number(s):
    if isinstance(s, str):
        return float(s[:s.find("(")])
    else:
        return s

matplotlib.rcParams.update({'font.size': 18})

plt.style.use("tableau-colorblind10")

width = 18
plt.figure(figsize=(width, 5))
ylim = 50
plt.ylim(0, ylim)

colors = ["lightcoral", "lightsalmon", "peachpuff", "skyblue", "orange", "pink", "turquoise"]
hatches = ["", "\\", "/", "|", "-", "x", "."]
bar_width = 0.25
bar_spacing = 2

start = 0
all_xticks = []
all_xlabels = []

device_index = {"cpu": 0, "gpu": 1, "dsp": 2, "cpu+gpu": 3, "cpu+dsp": 4, "gpu+dsp": 5, "cpu+gpu+dsp": 6}

model_name_dict = {
    "ResNet34": "R-34",
    "ResNet50": "R-50",
    "RegNetX-1.6GF": "RX-1.6",
    "RegNetX-4GF": "RX-4",
    "EfficientNet-L4": "EN-L4",
    "EfficientNet-B5": "EN-B5",
}

platform_dict = {
    "mi9": "Xiaomi 9",
    "pixel6": "Pixel 6",
    "mi11": "Xiaomi 11 Pro",
}

for platform in ["mi9", "pixel6", "mi11"]:
    if platform != "mi9":
        plt.axvline(start - 2 * bar_width, color="gray", linestyle="--")

    df = pd.read_csv("stretch_{}.csv".format(platform))
    xlabels = [model_name_dict[label] for label in df.iloc[:, 0].to_numpy()]
    devices = df.keys().to_list()[1:]
    devices = [d.upper() for d in devices]

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
        plt.bar(xbr, lats, color=colors[index], hatch=hatches[index], width=bar_width, label=device.upper(), edgecolor="grey")
        xbr = xbr + bar_width
    
    plt.text(start + total_width * n_models / 2, -15, platform_dict[platform], horizontalalignment="center", fontsize="20")    

    xbr = np.arange(start, start + total_width * n_models, total_width)
    xticks = xbr + (n_models - 1) / 2 * bar_width
    all_xticks = np.concatenate((all_xticks, xticks))
    all_xlabels = np.concatenate((all_xlabels, xlabels))
    start += total_width * n_models


plt.xticks(all_xticks, all_xlabels)

handles, labels = plt.gca().get_legend_handles_labels()
handles, labels = handles[:7], labels[:7]
plt.legend(handles, labels, bbox_to_anchor=(0, 1.05, 1, 0.105), ncol=7, fancybox=True, mode="expand")

plt.tight_layout()

plt.savefig('all_latency.pdf')

