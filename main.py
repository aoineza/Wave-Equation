import waveEquation
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    # Inital displacement
    return np.sin(2*np.pi*x)

def g(x):
    # Initial velocity of the wave
    return 2*np.pi*np.sin(2*np.pi*x)

W,T,X = waveEquation.waveEquation(1,5,1,20,500,f,g)

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(X[0],W[0])
plt.ylim([-1.5,1.5])
plt.xlim([0,1])
plt.xlabel("Position")
plt.ylabel("Displacement")
for w,t,x in zip(W[1:][:],T[1:][:],X[1:][:]):
    line1.set_ydata(w)
    plt.show()
    plt.pause(0.1)
    
