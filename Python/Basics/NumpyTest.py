import numpy as np
import matplotlib.pyplot as plot
a= np.array([4, 2, 3, 1])
print(a)
print(a[2])

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plot.subplot(1, 2, 1)
plot.plot(x, y)
plot.title("Test plot")
plot.xlabel("X-Axis")
plot.ylabel("Y-Axis")
plot.grid()
plot.subplot(1, 2, 2)
plot.plot(a)
plot.show()