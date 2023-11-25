import numpy as np
from numpy import linalg  #zbog SVD algoritma
np.set_printoptions(precision=5, suppress=True)
 
 # ovde pišete pomocne funkcije
def DLTAlgorithm(points, destPoints):
    A = []
    
    for i in range(len(points)):
        row1 = [
            0, 0, 0,
            -destPoints[i][2]*points[i][0], -destPoints[i][2]*points[i][1], -destPoints[i][2]*points[i][2],
            destPoints[i][1]*points[i][0], destPoints[i][1]*points[i][1], destPoints[i][1]*points[i][2]
        ]
        A.append(row1)
        
        row2 = [
            destPoints[i][2]*points[i][0], destPoints[i][2]*points[i][1], destPoints[i][2]*points[i][2],
            0, 0, 0,
            -destPoints[i][0]*points[i][0], -destPoints[i][0]*points[i][1], -destPoints[i][0]*points[i][2]
        ]
        A.append(row2)
        
    _, _, V = np.linalg.svd(A, full_matrices= True)
        
    T = V[-1].reshape(3,3)
    T = T / T[2][2]
    return T
 
def DLT(origs, imgs):
 
 # vaš kod
 
    return DLTAlgorithm(origs,imgs)
 
 