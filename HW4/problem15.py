# Rolando Rosales 1001850424 - problem15.py

import numpy as np
import sympy as sp
import scipy.linalg as linalg

"""
The basis of the matrix was calculated by performing row reduction and getting the pivots of the matrix.
Then, the vectors in those pivots were used to make the basis for col(A)
The dimension is simply the number of pivots, or the number of vectors in the basis
"""

def main():
   print('This program only works with matricies with a max row size of 4 (0-3), but works for any column size')
   A = np.array([[0, 2, 3],
                 [1, 1, -2],
                 [4, 1, 0],
                 [3, -1, -1]])
                 
   print("A = \n", A, "\n")

   # ROW-REDUCING MATRIX A

   A_pivots = sp.Matrix(A).rref()[1]   
   B = np.empty([4, 1])

   # STORING BASIS OF COL(A) FROM THE PIVOTS

   for c in A_pivots:
      B = np.append(B, [[A[0][c]], [A[1][c]], [A[2][c]], [A[3][c]]], axis = 1)
   
   B = np.delete(B, 0, 1)
   
   print('The basis for col(A) is...\nB =\n', B, "\n")
   
   # OBTAINING DIMENSION
   
   A_dimension = A_pivots[2] + 1
   
   print('Additionally, the dimension for the vector space of A is', A_dimension)
   
if __name__ == "__main__":
   main()
