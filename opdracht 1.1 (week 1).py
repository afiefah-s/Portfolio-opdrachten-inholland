#import matplotlib.pyplot as plt

#v = [1, 2, 3, 4, 5]
#plt.plot(v, color="c", marker = '*', linestyle='dotted',
#linewidth=2, markersize=12)
#plt.title("Mijn eerste grafiek") # voeg een titel toe aan je figuur
#plt.xlabel("Index") # voeg een titel toe aan de x-as
#plt.ylabel("Waarde") # voeg een titel toe aan de y-as
#plt.show() # plot het figuur

import matplotlib.pyplot as plt


v = [1.1, 2.2, 3.3, 4.5, 5.5,9,10,20]
plt.plot(v, color="c", marker = '*', linestyle='dotted',
linewidth=2, markersize=12)
plt.title("Ijklijn")
plt.xlabel("Concentratie (mg/mL)")
plt.ylabel("Absorptie")
plt.show()
