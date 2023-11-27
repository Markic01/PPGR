import numpy as np

def normalize(p):
    s = np.sqrt(sum([x*x for x in p]))
    p = np.array([x/s for x in p])
    return p

def Q2AxisAngle(q):
    q = normalize(q)

    if q[3] < 0:
        q = -q
        
    phi = 2 * np.arccos(q[3])
    
    if phi == 0:
        return np.array([1,0,0,0])
    
    if abs(q[3]) == 1:
        p = [1,0,0]
    else:
        p = normalize(np.array([q[0],q[1],q[2]]))
      
    p = np.append(p,phi)
    p = np.array(p)
    p = np.where(np.isclose(p, 0) , 0 , p)
    return p

np.set_printoptions(precision=5,suppress=True)
q = np.array([1,5,1,3])
print(Q2AxisAngle(q))