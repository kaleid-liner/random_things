import pandas as pd
import matplotlib.pyplot as plt


def smooth(scalars, weight: float):  # Weight between 0 and 1
    last = scalars[0]  # First value in the plot (first timestep)
    smoothed = list()
    for point in scalars:
        smoothed_val = last * weight + (1 - weight) * point  # Calculate smoothed value
        smoothed.append(smoothed_val)                        # Save it
        last = smoothed_val                                  # Anchor the last smoothed value
        
    return smoothed


plt.style.use("tableau-colorblind10")
df = pd.read_csv("/home/eka/gemm-analysis/dwconv.csv")

def plot(df, ax):
    ax1 = ax.twinx()
    ax2 = ax.twinx()
    ax2.spines.right.set_position(("axes", 1.2))
    ax.set_xlabel("N Blocks")

    handles = []

    colors = ["tab:red", "tab:green", "tab:blue"]

    for feat, ax_, color in zip(["Runtime", "Energy", "Power"], [ax, ax1, ax2], colors):
        feats = smooth(df[feat].to_list(), 0)
        handle, = ax_.plot(df.index, feats, label=feat, color=color)
        handles.append(handle)
        ax_.set_ylabel(feat)
        ax_.set_ylim(bottom=0)

    ax.legend(handles=handles)
    ax.set_xticks(ticks=df.index, labels=df["N Blocks"])


groups = [3, 2, 3, 3, 2, 3]
start = 0
for i, group in enumerate(groups):
    fig, ax = plt.subplots()
    fig.subplots_adjust(right=0.75)

    plot(df.iloc[start:start+group], ax)
    plt.savefig("gemm-analysis-{}.png".format(i))
    plt.clf()
    start += group
