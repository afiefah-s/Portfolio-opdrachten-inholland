#x=14

#while x < 100: #<= als tot en met 100
 #   print (x)

  #  x = x + 1

   # for i in range (101): evengetallen (0,101,2)
#    print (i)

v = [10, 20, 30, 40]
v[0]     # Geeft 10 (eerste element)
v[1:3]   # Geeft 20 en 30 (let op: eindindex is exclusief!)

import numpy as np
m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

m[0, 1]    # Geeft 2 (rij 0, kolom 1)
m[1, :]    # Hele tweede rij
m[:, 2]    # Hele derde kolom

s = "proteomics"
s[0]    # 'p'
s[4]    # 'e'
s[-1]   # 's' (laatste teken, via negatieve index)
s[2:6]  # 'oteo' (van index 2 t/m 5)

