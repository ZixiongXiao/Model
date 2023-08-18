# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:59:12 2023

@author: mikesyon

D'Alembert's formula for solving PDE: 
    Utt - c**2 Uxx = 0, U(x, 0) = f(x),
    Ut(x, 0) = g(x) = 0. 

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# In[18]: Core
class formula:
    """Output frame in each t"""
    def __init__(self, right_bound, left_bound, Nx, c):
        self.x = np.linspace(left_bound,right_bound,Nx)
        self.U = np.zeros(Nx)
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.Nx = Nx
        
    def g(self, x):
        """An example of initial deflection at time = 0"""
        if x < 1 and x > -1:
            return 1 - np.absolute(x)**2
        else:
            return 0
    
    def wave(self, x, t, c):
        """displacment with respect to time and 1D space"""
        return (1/2) * (self.g(x + c * t) + self.g(x - c * t))
    
# In[39]: Create the wave object
f = formula(100, -100, 200, 1)

# In[42]: Contiunously ploting
fig = plt.figure()
axis = plt.axes(xlim=(f.left_bound, f.right_bound), ylim=(-2, 2))
plt.title("d'Alembert's solution with initial displacement")
plt.xlabel('X', fontweight='bold')
plt.ylabel('U', fontweight='bold',rotation = 0)
ln, = axis.plot([], [])

def update(frame):
    for j in range(f.Nx):
        f.U[j] = f.wave(f.left_bound + j, frame, 1)

    ln.set_data(f.x, f.U)
    return ln,

animation = FuncAnimation(fig, update, interval=2e8, frames=100, blit=True, repeat=True)

# In[59]: Save the animation as a GIF using the animation.save() method
animation.save('dAlembertformula2.gif', writer='pillow', fps=15)



