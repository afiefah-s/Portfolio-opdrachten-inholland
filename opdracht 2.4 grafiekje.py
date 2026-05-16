import matplotlib.pyplot as plt

x = 320
stap = 0

# Lijst voor concentraties
concentraties = [x]

while x >= 4.5:
    stap = stap + 1
    x = x / 2

    concentraties.append(x)

    print("Stap:", stap)
    print("Concentratie:", x)

# Grafiek maken
plt.plot(concentraties)

# Labels en titel
plt.xlabel("Stap")
plt.ylabel("Concentratie")
plt.title("Verdunning per stap")

# Plot tonen
plt.show()