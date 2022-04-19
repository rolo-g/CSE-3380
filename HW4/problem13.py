# Rolando Rosales 1001850424 - problem13.py

import numpy as np
import sympy as sp

def main():

   A = np.array([[3, 8, -5],
                [3, -6, -7],
                [3, 4, 2]])
                  
   b = np.array([[-1],
                 [-1],
                 [3]])

   print('A =\n', A, '\nb =\n', b, '\n')

   # PART A

   A_reduced = np.array(sp.Matrix(A).rref()[0])
   print('Echelon form of A =\n', A_reduced, "\n")

   # PART B

   A_columnspace = np.array(sp.Matrix(A).columnspace())
   print('Column space of A =\n', A_columnspace, "\n")

   # PART C

   x1, x2, x3 = sp.symbols("x1, x2, x3")
   x = np.array(sp.linsolve((sp.Matrix(A), sp.Matrix(b)), (x1, x2, x3)))

   print('Solving Ax = b for x...\n x =\n', x, "\n")

   # PART D

   A_nullspace = np.array(sp.linsolve((sp.Matrix(A), sp.Matrix([[0],[0],[0]])), (x1, x2, x3)))
   print('nul(A) = \n', A_nullspace, "\n")
   
if __name__ == "__main__":
    main()
