import matplotlib.pyplot as plt
import numpy as np

# image = plt.imread('city.png')
# plt.imshow(image)

x = np.arange(6)
y = np.arange(3)
X, Y = np.meshgrid(x, y)
# C = np.array([[0.01,0.02,0.03,0.04],[0.05,0.06,0.07,0.08]])
C = np.array([[0.0,0.1,0.2,0.3,0.4],[0.5,0.6,0.7,0.8,0.9]])
# C = np.random.rand(len(x)-1, len(y)-1)
print C
plt.subplot(111)
plt.pcolormesh(X,Y,C)
plt.axis('off')
plt.show()
