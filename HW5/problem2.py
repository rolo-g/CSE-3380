# Rolando Rosales 1001850424 - problem2.py

import numpy as np
import random as rn
import matplotlib.pyplot as plt

def cosSimilarity(A):
   
   cos = np.empty([np.shape(A)[1], np.shape(A)[1]])
   
   for r in range(0, np.shape(A)[1]):
      for c in range(0, np.shape(A)[1]):
         cos[r][c] = np.dot(A[:, r], A[:, c]) / np.dot(np.linalg.norm(A[:, r]), np.linalg.norm(A[:, c])) 
   
   return cos
   
def main():
   
   A = np.random.randint(-9, 10, (rn.randint(2, 10), rn.randint(2, 10)))
   print('The original matrix, A = \n', A, '\n')

   cos = cosSimilarity(A)
   print('The Cosine Similarity matrix (rounded), Cos(θ) = \n', np.round(cos, 3), '\n')
   
   figure = plt.matshow(cos, cmap = "bwr")
   plt.show()
   
if __name__ == "__main__":
    main()
