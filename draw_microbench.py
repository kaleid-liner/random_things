import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline


df = pd.read_csv("data/t512_e480.csv")

def smooth(x, y, n=100):
    start = 0
    splines = []
    lbc = rbc = None
    for mid in range(1, len(x)):
        if (
          mid + 1 >= len(x) or
          ((y[mid] - y[mid - 1]) * (y[mid + 1] - y[mid])) < 0
        ):
            rbc = [(1, 0)]
        else:
            rbc = None
        if (
          mid - 2 < 0 or
          ((y[mid - 1] - y[mid - 2]) * (y[mid] - y[mid - 1])) < 0
        ):
            lbc = [(1, 0)]
        else:
            lbc = None
        if lbc is None and rbc is None:
            lbc = [(1, 0)]
        spline = make_interp_spline(x[start:mid+1], y[start:mid+1], k=2, bc_type=(lbc, rbc))
        splines.append(spline)
        start = mid

    x_ = np.linspace(x.min(), x.max(), n)

    def spline(_x):
        idx = sum(1 if _x > v else 0 for v in x[1:])
        return splines[idx](_x)

    y_ = np.vectorize(spline)(x_)
    return x_, y_

plt.style.use("seaborn-whitegrid")
lats_, engys_ = smooth(lats, engys)
plt.figure(figsize=(4.5, 2.5))
plt.plot(lats_, engys_, "--", color="grey")
plt.scatter(lats, engys, color="tab:blue", label="OFA Original")
plt.scatter([0.4313786], [24.822], color="tab:green", marker="^", label="Best")
plt.xlabel("Latency")
plt.ylabel("Energy")
plt.tight_layout()
plt.legend()
plt.savefig("ofa_resnet_blocks_compare.png")
plt.savefig("ofa_resnet_blocks_compare.pdf")
