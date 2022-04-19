# Rolando Rosales 1001850424 - problem3.py

import numpy as np
import random as rn
import matplotlib.pyplot as plt

def computeLoss(v, u, rowSize):
   loss = [0, 0]
   #       L1 L2
   plotdata = np.empty([rowSize, 2])
   for x in range(0, rowSize):
      plotdata[x][0] = (abs(v[x] - u[x]))
      loss[0] = loss[0] + plotdata[x][0]
      
   for x in range(0, rowSize):
      plotdata[x][1] = pow((v[x] - u[x]), 2)
      loss[1] = loss[1] + plotdata[x][1]

   return loss, plotdata

def main():
   rowSize = rn.randint(5, 11)
   v = np.random.randint(-9, 10, (rowSize, 1))
   u = np.random.randint(-9, 10, (rowSize, 1))
   
   print('v =\n', v, '\n\nu =\n', u, '\n')
   
   loss, plotdata = computeLoss(v, u, rowSize)
   
   print("L1 =", loss[0], "\nL2 =", loss[1])
   
   print("\nPlot points (non-sorted):")
   for x in range(0, np.shape(plotdata)[0]):
      print("(", plotdata[x, 1], ",", plotdata[x, 0], ")")

   figurept = plt.scatter(plotdata[:, 1], plotdata[:, 0], c = "r", linewidth = 3)
   figureln = plt.plot(np.sort(plotdata[:, 1]), np.sort(plotdata[:, 0]), c = "r", linewidth = 3)
   plt.xlabel("L2")
   plt.ylabel("L1")
   plt.title("L1 vs. L2")

   plt.show()

if __name__ == "__main__":
    main()
