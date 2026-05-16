import pandas as pd

import os #bestand importeren
print(os.getcwd()) #kijken waar het bestand gelezen wordt door Python
os.chdir("/Users/afiefah/Documents/P12 Informatica") #veranderen van pathway
print(os.getcwd()) #nieuwe pathway dat gelezen wordt door Python

#import pandas as pd

#data = pd.read_csv("gedempte_sinus.csv", delimiter=",")

#import pandas as pd
#import matplotlib.pyplot as plt

#df = pd.read_csv('gedempte_sinus.csv')

# lijnen met kleuren
#plt.plot(df['tijd'], color='red', label='tijd')
#plt.plot(df['waarde'], color='cyan', label='waarde')

# titel en labels
#plt.title('Gedempte sinus')
#plt.xlabel('x-as')
#plt.ylabel('y-as')

#plt.show()

#help(plt.plot)

import os
import pandas as pd
import matplotlib.pyplot as plt

print(os.getcwd())

os.chdir("/Users/afiefah/Documents/P12 Informatica")

df = pd.read_csv('gedempte_sinus.csv')

# één lijn: tijd vs waarde
plt.plot(
    df['tijd'],
    df['waarde'],
    color='maroon',
    marker='o',
    linestyle=':',
    linewidth=5)

plt.title('Gedempte sinus')
plt.xlabel('Tijd')
plt.ylabel('Waarde')

plt.grid(True)

plt.show()

help(plt.plot)