import numpy as np
import copy

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

normalize([[1,2,3],[3,2,1],[0,1,1],[7,11,10],[9,5,5],[2,2,2],[1,5,3],[12,1,11]])