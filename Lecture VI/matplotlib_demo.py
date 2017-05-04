import matplotlib.pyplot as plt
import numpy as np

fig, ax_lst = plt.subplots(1, 2, sharex=True, sharey=True)

x = np.linspace(-5, 5, 100)
y1 = np.power(x, 2.)
y2 = np.power(x-3, 3.)

ax_lst[0].plot(x, y1)
ax_lst[1].plot(x, y2)
fig.savefig('demo.png')
