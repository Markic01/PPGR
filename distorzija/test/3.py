import cv2
import numpy as np
import math


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
    
    T = np.dot(S,G)
    T = T / T[2][2]
    return T

def normMatrix(points):
    for i in range(len(points)):
        points[i] = [points[i][0]/points[i][2],points[i][1]/points[i][2],1]
    return normalize(points)

np.set_printoptions(precision=5, suppress=True)
trapez = [[- 3, - 1, 1], [3, - 1, 1], [1, 1, 1], [- 1, 1, 1], [1,2,3], [-8,-2,1]]
print(normMatrix(trapez))