import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv("data/v100vs2080ti.csv")

colors = ["lightcoral", "lightsalmon", "skyblue", "orange", "pink", "turquoise"]
colors = ["slategray", "darkviolet", "teal", "darkgreen"]

v100_energy = df["Energy - V100"].to_numpy()
v100_latency = df["Latency - V100"].to_numpy() * 1000
g2080ti_energy = df["Energy - 2080ti"].to_numpy()
g2080ti_latency = df["Latency - 2080ti"].to_numpy() * 1000
accuracy = df["Accuracy"].to_numpy()
model = df["Model"].to_numpy()
xoffsets = [0.3, 0.3, -1]
sfactor = np.array([16, 16, 8, 8, 1, 1])


def draw(energy, latency, accuracy, model, name):
    plt.figure(figsize=(3.5, 2.5))
    plt.xlim(left=57, right=83)
    plt.ylim(bottom=0.5, top=12.5)
    s = (energy ** 2) * 300 * sfactor
    c = [colors[i // 2] for i in range(len(model))]

    plt.scatter(accuracy, latency, s=s, c=c, alpha=0.5, edgecolors=c)

    for k in range(len(model) // 2):
        i, j = 2 * k, 2 * k + 1
        xi, yi = accuracy[i], latency[i]
        xj, yj = accuracy[j], latency[j]
        xi = xi + xoffsets[k]
        xj = xj + xoffsets[k]
        yoffset = 0.4 * np.sign(yi - yj)
        yi = yi + yoffset
        yj = yj - yoffset
        halign = "left" if xoffsets[k] > 0 else "right"
        plt.annotate(model[i], xy=(xi, yi), horizontalalignment=halign, fontsize=12)
        plt.annotate(model[j], xy=(xj, yj), horizontalalignment=halign, fontsize=12)

    
    plt.xlabel("Accuracy")
    plt.ylabel("Latency")
    plt.tight_layout()
    plt.savefig("{}.png".format(name))
    plt.savefig("{}.pdf".format(name))

plt.style.use("seaborn-whitegrid")
draw(v100_energy, v100_latency, accuracy, model, "v100_v100")
plt.clf()
draw(g2080ti_energy, g2080ti_latency, accuracy, model, "v100_2080ti")
