# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dashed',marker = '*',ms=30, mec = 'hotpink', mfc = 'hotpink')
plt.show()