import cv2
import numpy as np

points = []

def normalize(points):
    x = sum([point[0] for point in points]) / len(points)
    y = sum([point[1] for point in points]) / len(points)
    
    translated = [[point[0] - x, point[1] - y, point[2]] for point in points]
    G = np.array([
        [1, 0, -x],
        [0, 1, -y],
        [0, 0, 1]
    ])
    
    avgDist = sum([np.sqrt(point[0]**2+point[1]**2) for point in translated]) / len(points)
    scale = np.sqrt(2) / avgDist
    S = np.array([
        [scale, 0 , 0],
        [0, scale, 0],
        [0, 0, 1]
    ])
    
    return np.dot(S,G)

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

def calcDist(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def getDest(points):
    #        A   B                              A        B
    # 
    #                        >>>>>>>>>>        
    # 
    #    D             C                        D        C
    # 
    
    destPoints = [points[0]]
    
    AB = calcDist(points[0], points[1])
    CD = calcDist(points[2], points[3])
    width = (AB + CD) / 2
    
    AD = calcDist(points[0], points[3])
    BC = calcDist(points[1], points[2])
    height = (AD + BC) / 2
    
    
    destPoints.append([points[0][0] + width, points[0][1], points[0][2]])
    destPoints.append([points[0][0] + width, points[0][1] + height, points[0][2]])
    destPoints.append([points[0][0], points[0][1] + height, points[0][2]])
    
    return destPoints

# def onClick(event, x, y, flags, param):
#     if event  == cv2.EVENT_LBUTTONDOWN:
#         if len(points) < 4:
#             points.append([x, y, 1])
            
#             cv2.putText(image, 'X', (x-16,y+14), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 100), 3, cv2.LINE_AA)
#             cv2.imshow('distorted image', image)
            
#         if len(points) == 4:
#             destPoints = getDest(points)
#             matrix = DLTAlgorithm(points, destPoints)
#             out = cv2.warpPerspective(image, matrix, (500,900))
            
#             cv2.imshow('result', out)
#             cv2.waitKey(0)

# path = './3.jpeg'
# image = cv2.imread(path, cv2.IMREAD_COLOR)
# image = cv2.resize(image, (500, 900), interpolation = 2)
# cv2.namedWindow('distorted image')
# cv2.moveWindow('distorted image', 2440, 250)
# cv2.imshow('distorted image', image)
# cv2.setMouseCallback('distorted image', onClick)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)


def normalizedDLTAlgorithm(points, destPoints):
    T = normalize(points)
    Tp = normalize(destPoints)

    M = np.dot(T,np.transpose(points)).transpose()
    Mp = np.dot(Tp, np.transpose(destPoints)).transpose()
    
    Pp = DLTAlgorithm(M, Mp)
    
    return np.linalg.inv(Tp).dot(Pp).dot(T)

def DLT(origs, imgs):
    np.set_printoptions(precision=5, suppress=True)
    return DLTAlgorithm(origs,imgs)

trapez = [[- 3, - 1, 1], [3, - 1, 1], [1, 1, 1], [- 1, 1, 1], [1,2,3], [-8,-2,1]] 
pravougaonik1 = [[- 2, - 1, 1], [2, - 1, 1], [2, 1, 1], [- 2, 1, 1], [2,1,5], [-16,-5,5]]
print(DLT(trapez, pravougaonik1))
# ako gledate uradjeni primer, primetite [2,1,4]->[2,1,5], [-16,-5,4]->[-16,-5,5]
# zato matrica nije ista kao u primeru