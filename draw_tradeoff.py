import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

x = [14.866, 17.804, 21.081, 33.222]
y = [74, 76.2, 76.8, 78.2]

original = (26.438, 76.7)
plt.style.use("grayscale")

matplotlib.rcParams.update({'font.size': 20})
plt.figure(figsize=(8, 5))

plt.plot(x, y, "o--")

plt.xlabel("Latency (ms)")
plt.ylabel("Top-1 Acc. (%)")

plt.scatter(*original, marker="*")

plt.tight_layout()
plt.savefig("supernet_tradeoff.png")
plt.savefig("supernet_tradeoff.pdf")
