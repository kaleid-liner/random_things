import pandas as pd
import matplotlib.pyplot as plt

import numpy as np


fig = plt.figure()
# ax_3d = fig.add_subplot(projection='3d')
ratio = 0.5


def plot_space(df, label):
    df["flops"] = df["flops"].to_numpy() / 1000000000
    df["flops_latency"] = df["flops"] / df["latency"]
    df = df.sort_values(by="flops_latency", ascending=False)
    df = df[:int(ratio*len(df))]
    flops = df["flops"]
    latency = df["latency"].to_numpy()
    energy = df["energy"].to_numpy()
    print(np.average(df["flops_latency"]))
    s = df["flops_latency"]
    s = (s - np.min(s)) / (np.max(s) - np.min(s)) * 100
    plt.scatter(flops, energy, s=s, label=label)


# def plot_3d(df):
#     ax_3d.scatter(df["latency"], df["energy"], df["flops"])


df1 = pd.read_csv("~/regnety-split-wa/engeff.csv")
df2 = pd.read_csv("~/regnety-split-wa/org.csv")

plot_space(df1, "Smaller Wa")
plot_space(df2, "Larger Wa")

plt.xlabel("GFLOPs")
plt.ylabel("Energy (J)")
plt.legend()
# ax_3d.view_init(elev=10, azim=11)

plt.savefig("split-wa-{}.png".format(ratio))
