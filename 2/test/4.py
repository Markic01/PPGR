import numpy as np
from numpy import linalg  #zbog SVD algoritma
np.set_printoptions(precision=5, suppress=True)


def normalize(points):
    x = sum([point[0] for point in points]) / len(points)
    y = sum([point[1] for point in points]) / len(points)
    
    translated = [[point[0] - x, point[1] - y, point[2]] for point in points]
    G = np.array([
        [1, 0, -x],
        [0, 1, -y],
        [0, 0, 1]
    ])
    
    avgDist = sum([np.sqrt(point[0]**2+point[1]**2) for point in translated]) / len(translated)
    scale = np.sqrt(2) / avgDist
    S = np.array([
        [scale, 0 , 0],
        [0, scale, 0],
        [0, 0, 1]
    ])
    
    T = np.dot(S,G)
    T = T / T[2][2]
    return T

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

def DLTwithNormalization(origs, imgs):
    for i in range(len(origs)):
        origs[i] = [origs[i][0]/origs[i][2],origs[i][1]/origs[i][2],1.]
    T1 = normalize(origs)    
    
    for i in range(len(imgs)):
        imgs[i] = [imgs[i][0]/imgs[i][2],imgs[i][1]/imgs[i][2],1.]
    T2 = normalize(imgs)
    
    origs = [np.dot(T1,point) for point in origs]
    imgs = [np.dot(T2,point) for point in imgs]
        
    P = DLTAlgorithm(origs,imgs)
    T = linalg.inv(T2).dot(P).dot(T1)
    T = T / T[2][2]
    return T

trapez = [[- 3, - 1, 1], [3, - 1, 1], [1, 1, 1], [- 1, 1, 1], [1,2,3], [-8,-2,1]] 
pravougaonik1 = [[- 2, - 1, 1], [2, - 1, 1], [2, 1, 1], [- 2, 1, 1], [2,1,5], [-16,-5,5]]
print(DLTwithNormalization(trapez, pravougaonik1))