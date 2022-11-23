import matplotlib.pyplot as plt


plt.style.use("ggplot")

x = [73.5, 74.2, 74.6]
y = [18.3, 22.1, 39.4]


plt.plot(x, y, "bo--")
plt.xlabel("Accuracy")
plt.ylabel("Latency")

plt.scatter([73.6], [50.9], color="r")
plt.savefig("Tradeoff.png")
