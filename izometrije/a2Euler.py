import numpy as np

def matricaKretanja(A,eps):
    X = np.dot(A,A.T)
    X = np.where(np.isclose(X,0),0,X)
    det = np.linalg.det(A)
    return np.allclose(X,np.eye(3,3)) and abs(1 - det) < eps

def A2Euler(A):
    if not matricaKretanja(A,1e-6):
        return 'Nije matrica kretanja!'
    
    if A[2][0] == -1:
        teta = np.pi/2
        phi = 0
        psi = np.arctan2(-A[0][1],A[1][1])
    elif A[2][0] == 1:
        teta = -np.pi/2
        phi = 0
        psi = np.arctan2(-A[0][1],A[1][1])
    else:
        teta = np.arcsin(-A[2][0])
        phi = np.arctan2(A[2][1],A[2][2])
        psi = np.arctan2(A[1][0],A[0][0])
        
    uglovi = np.array([psi,teta,phi])
    uglovi = np.where(np.isclose(uglovi,0),0,uglovi)
    return uglovi


np.set_printoptions(precision=5,suppress=True)
A = (1/9)*np.array([[1,-8,-4], [4,4,-7], [8,-1,4]])
print(A2Euler(A))