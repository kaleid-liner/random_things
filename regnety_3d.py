import pandas as pd
import matplotlib.pyplot as plt


fig = plt.figure()
ax_3d = fig.add_subplot(projection='3d')

def plot_space(df):
    plt.scatter(df["flops"], df["latency"], df["energy"])


def plot_3d(df):
    ax_3d.scatter(df["flops"], df["latency"], df["energy"])


df1 = pd.read_csv("~/regnety-search-exhaustive/engeff.csv")
df2 = pd.read_csv("~/regnety-search-exhaustive/org.csv")

plot_3d(df1)
plot_3d(df2)

ax_3d.view_init(elev=10, azim=11)

plt.savefig("pareto.png")
