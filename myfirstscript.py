# Graph draw using python
import math
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi,2*np.pi,np.pi/100)
y = np.cos(x) * np.exp(x)

plt.plot(x,y)
plt.show()

z = np.cos(x)

plt.plot(x,z)
plt.show()
