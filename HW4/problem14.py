# Rolando Rosales 1001850424 - problem14.py

import numpy as np
import sympy as sp
import scipy.linalg as linalg

"""
Since this is a nxn matrix, I took the inverse of B, and multiplied it with x_B to find x
"""

def solveVector(B, x_B):
   x1, x2, x3 = sp.symbols("x1, x2, x3")
   
   x = x = sp.linsolve((sp.Matrix(linalg.inv(B)), sp.Matrix(x_B)), (x1, x2, x3))
   
   return x

def main():
   B = np.array([[0, -4, 6],
                 [-1, 0, 6],
                 [-1, 0, 3]])
                 
   x_B = np.array([[-2],
                   [6],
                   [1]])
                   
   print('This will find x in Bx = x_B, where B and x_B are known\n')
   print('B =\n', B, '\nx_B =\n', x_B, '\n')
   
   x = solveVector(B, x_B)
   print('After performing the necessary calculations...\n x =\n', x)

if __name__ == "__main__":
   main()
