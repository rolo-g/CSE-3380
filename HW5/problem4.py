# Rolando Rosales 1001850424 - probem4.py
import numpy as np
import random as rn
import matplotlib.pyplot as plt

def plotVectors(v, u, w):
   fig = plt.figure()
   ax = plt.axes(projection = '3d')
   ax.set_xlim([-10, 10])
   ax.set_ylim([-10, 10])
   ax.set_zlim([-10, 10])
   
   ax.quiver(0, 0, 0, v[0], v[1], v[2], color = 'red')
   ax.quiver(0, 0, 0, u[0], u[1], u[2], color = 'blue')
   ax.quiver(0, 0, 0, w[0], w[1], w[2], color = 'black')
   
   plt.show()

def main():
   v = [rn.randint(-10, 11), rn.randint(-10, 11), rn.randint(-10, 11)]
   u = [rn.randint(-10, 11), rn.randint(-10, 11), rn.randint(-10, 11)]
   c = np.dot(v, u) / np.dot(u, u)
   w = [c * u[0], c * u[1], c * u[2]]
   
   print("v =\n", v, "\nu =\n", u, "\nw =\n", w)

   plotVectors(v, u, w)

if __name__ == "__main__":
   main()

