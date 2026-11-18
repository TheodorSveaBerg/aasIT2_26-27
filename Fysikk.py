import matplotlib.pyplot as plt



m = 79
g = 9.81
k = 0.32


G = m*g

def a(v):
    L = k*v**2
    sum_F = G - L
    akselerasjonen = sum_F/m
    return akselerasjonen

s = 0
v = 0
t = 0

t_slutt = 40
dt = 0.1
t_verdier = [t]
s_verdier = [s]
v_verdier = [v]


while t < t_slutt:
    v = v + a(v)*dt
    s = s + v*dt
    t = t + dt
    t_verdier.append(t)
    s_verdier.append(s)
    v_verdier.append(v)

plt.plot(t_verdier, v_verdier)
plt.title("Hastighet som funksjon av tid")
plt.xlabel("t[s]")
plt.ylabel("v[m/s]")
plt.grid()
plt.show()

print(t, s, v)