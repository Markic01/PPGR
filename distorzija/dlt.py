import cv2
import numpy as np

points = []

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
        
    return V[-1].reshape(3,3)

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

def onClick(event, x, y, flags, param):
    if event  == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 4:
            points.append([x, y, 1])
            
            cv2.putText(image, 'X', (x-16,y+14), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 100), 3, cv2.LINE_AA)
            cv2.imshow('distorted image', image)
            
        if len(points) == 4:
            destPoints = getDest(points)
            matrix = DLTAlgorithm(points, destPoints)
            out = cv2.warpPerspective(image, matrix, (500,900))
            
            cv2.imshow('result', out)
            cv2.waitKey(0)

path = './3.jpeg'
image = cv2.imread(path, cv2.IMREAD_COLOR)
image = cv2.resize(image, (500, 900), interpolation = 2)
cv2.namedWindow('distorted image')
cv2.moveWindow('distorted image', 2440, 250)
cv2.imshow('distorted image', image)
cv2.setMouseCallback('distorted image', onClick)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)