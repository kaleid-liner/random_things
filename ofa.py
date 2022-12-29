import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt


def func(x, a, w):
    return a * np.power(x, w)

plt.style.use('ggplot')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

resnet_acc = [75, 76.3, 77.1, 78.3, 79, 79.3, 79.7, 79.8]
resnet_energy = [0.170775, 0.20803, 0.263529, 0.278056, 0.361694, 0.348622, 0.381305, 0.414901]

myresnet_acc = [76.992, 77.408, 77.864, 78.064,]
myresnet_energy = [0.1891, 0.19895, 0.21504, 0.229377]

optimizedParameters, pcov = opt.curve_fit(func, resnet_acc, resnet_energy, maxfev=5000)

ax1.scatter(resnet_acc, resnet_energy, marker='o')
acc_fit = np.linspace(74.5, 80.5, 1000)
ax1.plot(acc_fit, func(acc_fit, *optimizedParameters), label='OFA')
ax1.scatter(myresnet_acc, myresnet_energy, label='Ours')
ax1.set_xlabel('Accuracy')
ax1.set_ylabel('Energy')
ax1.legend()
ax1.set_title('ResNet50')

mobilenet_acc = [80.1, 79.8, 78.7, 76.9, 74.9, 73.3, 71.4]
mobilenet_energy = [0.232697, 0.227364, 0.182639, 0.150702, 0.160458, 0.139766, 0.104103]

mymobilenet_acc = [75.268, 75.764, 75.922, 76.644]
mymobilenet_energy = [0.110985, 0.114934, 0.114324, 0.128567]

optimizedParameters, pcov = opt.curve_fit(func, mobilenet_acc, mobilenet_energy, maxfev=5000)

ax2.scatter(mobilenet_acc, mobilenet_energy, marker='o')
acc_fit = np.linspace(71, 80.5, 1000)
ax2.plot(acc_fit, func(acc_fit, *optimizedParameters), label='OFA')
ax2.scatter(mymobilenet_acc, mymobilenet_energy, label='Ours')
ax2.set_xlabel('Accuracy')
ax2.set_ylabel('Energy')
ax2.legend()
ax2.set_title('MobileNetV3')


plt.tight_layout()
plt.savefig('ofa.pdf')
