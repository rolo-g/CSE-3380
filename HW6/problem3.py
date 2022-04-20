import numpy as np
import scipy.linalg as sp

def main():
    A = np.array([[1, 0, 4],
                 [-2, 3, -2],
                 [-2, 0, 6]])

    QR = sp.qr(A)

    print("Q = \n", QR[0], "\nR = \n", QR[1])
    
if __name__ == "__main__":
    main()
