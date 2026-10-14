
""""
v = 5.0
s = 0.0
t = 0.0

dt = 0.1
t_slutt = 3.0

while t < t_slutt:
    s = s + v*dt 
    t = t + dt


print("t =", t, " s =", s, " v =", v)
"""

import matplotlib.pyplot as plt

v = 5.0
s = 0.0
t = 0.0
a = 2.0

dt = 0.01
t_slutt = 3.0
t_verdier = [t]
s_verdier = [s]

while t < t_slutt:
    v = v + a*dt
    s = s + v*dt 
    t = t + dt


    t_verdier.append(t)
    s_verdier.append(s)

print(t_verdier)
print(s_verdier)

plt.plot(t_verdier, s_verdier)
plt.title("Strekning som funksjon av tid")
plt.xlabel("t [s]")
plt.ylabel("s [m]")
plt.show()