import os
import pandas as pd
import matplotlib.pyplot as plt

# Naar de map gaan
os.chdir("/Users/afiefah/Documents/P12 Informatica")

# Controleren
print(os.getcwd())

# CSV openen
data = pd.read_csv("lm4.csv", sep=";")

# Scatterplots maken
plt.scatter(data["x1"], data["y"], label="x1", color="red")
plt.scatter(data["x2"], data["y"], label="x2", color="aqua")

# Labels en titel
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatterplot")

# Legenda
plt.legend()

# Plot tonen
plt.show()
