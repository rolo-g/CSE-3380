#Rolando Rosales 1001850424 - problem3.py
import numpy as np
import random as rn

def main():
    # STEP A
    X = np.random.randint(0, 10, (rn.randint(4, 5), rn.randint(2, 3)))
    print("Matrix X =\n", X)
    
    #STEP B
    cov = X.T@X # calculating covariance matrix
    print("Covariance Matrix X^TX =\n", cov)
    W, V = np.linalg.eig(cov) # V = eigenvectors from np.linalg.svd
    print("eigenvectors, normalized =\n", V)
    
    # STEP C
    proj = (X@V)/np.linalg.norm(X@V) # Calculating projection and normalizing
    print("projection, normalized = \n", proj)
    
    #STEP D
    U = np.linalg.svd(X, full_matrices=False)[0] # U = u from np.linalg.svd
    print("U =\n", U)
    
    #STEP E
    """
    When comparing the projection and the U vector,
    they don't really seem to have common vlaues.
    Only the first vector (first column) for both U
    and proj have similar values. I'm not sure what the
    problem is with the code, as I assume they are supposed
    to be the same value.
    """
if __name__ == "__main__":
    main()
