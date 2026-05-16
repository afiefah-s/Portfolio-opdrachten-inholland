import numpy as np
import matplotlib.pyplot as plt

# 1. Vector maken
x = np.array([12.5, 13.2, 15.0, 14.8, 16.1, 15.6, 14.0])

# 2. Laatste 3 metingen selecteren
y = x[-3:]

print(y)

# 3. Lijnplot maken
plt.plot(y)
plt.title("Laatste 3 metingen")
plt.xlabel("Meting")
plt.ylabel("Concentratie (µg/mL)")
plt.show()