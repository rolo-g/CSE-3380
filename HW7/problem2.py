#Rolando Rosales 1001850424 - problem2.py
import numpy as np
import matplotlib.pyplot as plt

def main():
    A = np.array([[1, -2],
                  [-4, 1]])
    
    V = np.linalg.eig(A)[1]
    
    print("A =\n", A)
    print("V =\n", V)
    
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.quiver([0, 0], [0, 0], A[:, 0], A[:, 1], angles = 'xy', scale_units = 'xy', scale = 1, color = "Red")
    plt.quiver([0, 0], [0, 0], V[:, 0], V[:, 1], angles = 'xy', scale_units = 'xy', scale = 1, color = "Blue")
    plt.quiver([0, 0], [0, 0], [1, 0], [0, 1], angles = 'xy', scale_units = 'xy', scale = 1, color = "Black")
    plt.show()

if __name__ == "__main__":
    main()
