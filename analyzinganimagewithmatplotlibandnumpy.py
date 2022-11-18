import numpy as np
import matplotlib.pyplot as plt

a = plt.imread("images/profile.jpg")
# print(a)
print(np.shape(a))
print(type(a))
print(a.dtype)
plt.imshow(a)
# plt.show()
