import numpy as np

def normalize(p):
    s = np.sqrt(sum([x*x for x in p]))
    p = [x/s for x in p]
    return p

def AxisAngle2Q(p):
    phi = p[3]
    if phi == 0:
        return np.array([0,0,0,1])
    p = p[:-1]
    w = np.cos(phi/2)
    
    p = normalize(p)
    p = [np.sin(phi/2) * x for x in p]
    p.append(w)
    p = np.array(p)
    p = np.where(np.isclose(p, 0) , 0 , p)
    return p
    

np.set_printoptions(precision=5,suppress=True)
pphi = np.array([1, 1,1, 0])
print(AxisAngle2Q(pphi))