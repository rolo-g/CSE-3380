import numpy as np
import scipy.linalg as sp

def main():
    A = ([[1, 0, 4],
         [-2, 3, -2],
         [-2, 0, 6]])

    Q, r = sp.qr(A)
    
    print("Q = ", Q)

if __name__ == "__main__":
    main()
