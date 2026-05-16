import numpy as np
import matplotlib.pyplot as plt

concentraties = [5, 10, 20, 40, 80, 160, 320]

# Lege lijst voor log10-waarden
log_waarden = []

# For-loop gebruiken
for i in range(0, len(concentraties)):
    log_waarde = np.log10(concentraties[i])
    log_waarden.append(log_waarde)

# Resultaten printen
print(log_waarden)

plt.plot(concentraties, log_waarden)

# Labels en titel
plt.xlabel("Concentraties")
plt.ylabel("log10(concentratie)")
plt.title("Concentraties tegen log10-waarden")

plt.show()
