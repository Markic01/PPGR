import numpy as np
from numpy import linalg as LA
np.set_printoptions(suppress=True)


dst =  np.array([1,-1,-1])*(np.array([2048,0,0]) -  np.array([[544,666, 1], [862,847, 1], [576,1082,1],[245,862,1],[296,1134,1],[566,1346,1], [814,1127,1],[567,919,1]] ))
src = np.array([[0,0,3,1],[0,3,3,1],[3,3,3,1],[3,0,3,1],[3,0,0,1],[3,3,0,1],[0,3,0,1],[2,2,3,1]])

def cameraMatrix(src, dst):
    A = np.empty((12))

    for i in range(len(src)):
        x = src[i][0]
        y = src[i][1]
        z = src[i][2]
        t = src[i][3]

        xp = dst[i][0]
        yp = dst[i][1]
        zp = dst[i][2]

        row1 = np.array([0, 0, 0, 0, -zp*x, -zp*y, -zp*z, -zp*t, yp*x, yp*y, yp*z, yp*t])
        row2 = np.array([zp*x, zp*y, zp*z, zp*t, 0, 0, 0, 0, -xp*x, -xp*y, -xp*z, -xp*t])

        A = np.vstack((A, row1))
        A = np.vstack((A, row2))

    _,_,V = LA.svd(A)

    T = V[-1].reshape(3,4)
    
    return T

def decomposition(T):
    T0=T[:, :-1]
    if LA.det(T0)<0:
        T=-T

    c1=LA.det(T[:, 1:])
    c2=-LA.det(np.array([T[:, 0], T[:, 2], T[:, 3]]).T)
    c3=LA.det(np.array([T[:, 0], T[:, 1], T[:, 3]]).T) 
    c4=-LA.det(T[:, :-1])

    c1=c1/c4
    c2=c2/c4
    c3=c3/c4

    C=np.array([c1, c2, c3])
    Q, R = LA.qr(LA.inv(T0))

    if R[0][0] < 0:
        R[0] = -R[0]
        Q[:,0] = -Q[:,0]
    if R[1][1] < 0:
        R[1] = -R[1]
        Q[:,1] = -Q[:,1]
    if R[2][2] < 0:
        R[2] = -R[2]
        Q[:,2] = -Q[:,2]

    A = Q.T
    K = T0.dot(Q) 
    K = K / K[2][2]

    return K, A, C  

T = cameraMatrix(src,dst)
T = T/ T[0][0]
print('camera matrix:\n',T,end='\n\n')

K,A,C = decomposition(T)

print('camera calibration matrix:\n ',K,end='\n\n')
print('camera center position:\n ',C,end='\n\n')
print('external camera parameters matrix:\n ',A,end='\n\n')



# print(dst[0])
# X = T.dot(src[0])
# print(X / X[2])

