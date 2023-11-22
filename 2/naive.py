import numpy as np


def getMatrix(A, B, C, D):
    A = np.array(A)
    B = np.array(B)
    C = np.array(C)
    D = np.array(D)
    
    a = np.array([[A[0], B[0], C[0]], [A[1], B[1], C[1]], [A[2], B[2], C[2]]])
    b = np.array([D[0], D[1], D[2]])
    
    x = np.linalg.solve(a,b)
    P = np.array([x[0]*A,x[1]*B,x[2]*C]).T
    return P
    
def naiveAlg(A, B, C, D, Ap, Bp, Cp, Dp):
    P1 = getMatrix(A,B,C,D)
    P2 = getMatrix(Ap,Bp,Cp,Dp)
    
    T = P2.dot(np.linalg.inv(P1))
    T = T / T[2][2]
    return T

def opsti(points):
    for i in range(4):
        if np.linalg.det([points[j] for j in range(4) if i!=j]) == 0:
            return False
        
    return True
    
def naivni(origs, imgs):

    if not opsti(origs):
        return 'Losi originali!'
    
    if not opsti(imgs):
        return 'Lose slike!'
    
    return naiveAlg(origs[0], origs[1], origs[2], origs[3],
                    imgs[0], imgs[1], imgs[2], imgs[3])

trapez = [[- 3, - 1, 1], [3, - 1, 1], [1, 1, 1], [- 1, 1, 1]] 
pravougaonik = [[- 2, - 1, 1], [2, - 1, 1], [2, 1, 1], [- 2, 1, 1]]
print(naivni(trapez, pravougaonik))