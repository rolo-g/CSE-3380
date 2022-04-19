# Rolando Rosales 1001850424 - problem4.py
import numpy as np
import random as rn
import matplotlib.pyplot as plt

def main():
    data = np.loadtxt("dataset1.txt")
    A = np.vstack([data[:, 0], np.ones(len(data[:, 0]))]).T
    x, residuals, rank, s = np.linalg.lstsq(A, data[:, 1], rcond=None)
    print("Least squares solution = ", x)

    figure = plt.plot(data[:, 0], data[:, 1], 'o', color = 'red',  label='Original data', markersize=5)
    figure = plt.plot(data[:, 0], x[0]*data[:, 0] + x[1], color = 'blue', label='Fitted line', linewidth=3)
    figure = plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
