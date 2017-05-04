import matplotlib.pyplot as plt
import numpy as np

fig, ax_lst = plt.subplots(1, 2, sharex=True, sharey=True)

x = np.arange(1, 6)
y1 = np.power(x, 3.)
y2 = np.power(x-3, 3.)

ax_lst[0].bar(x, y1)
ax_lst[1].bar(x, y2)
fig.savefig('demo_bar.png')
