import numpy as np

def orientation(u,up,p):
    mat = np.array([u,up,p])
    if np.linalg.det(mat) < 0:
        return -1
    return 1
    

def norm(p):
    s = np.sqrt(sum([x*x for x in p]))
    p = [x/s for x in p]
    return p

def isNorm(p):
    s = np.sqrt(sum(x*x for x in p))
    return s == 1

def length(p):
    return np.sqrt(sum(x*x for x in p))

def getOrto(p):
    x = np.array([p[1],-p[0],0])
    if np.allclose(x,np.array([0,0,0])):
        return np.array([-p[2],0,p[0]])
    return x

def matricaKretanja(A,eps):
    X = np.dot(A,A.T)
    X = np.where(np.isclose(X,0),0,X)
    det = np.linalg.det(A)
    return np.allclose(X,np.eye(3,3)) and abs(1 - det) < eps
    
def A2AxisAngle(A):
    if not matricaKretanja(A,1e6):
        return 'Nije matrica kretanja!'
    
    if np.allclose(A,np.eye(3,3)):
        return (np.array([1,0,0]),0)
    
    Ae = A - np.eye(3,3)
    p = np.cross(Ae[0],Ae[1])
    
    if not isNorm(p):
        p = norm(p)
        
    u = getOrto(p)
    u = norm(u)
    up = np.dot(A,u)
    up = norm(up)
    
    p = [orientation(u,up,p) * x for x in p]
    
    angle = np.arccos(np.dot(u,up)) / (length(u) * length(up))
    
    p.append(angle)
    p = np.where(np.isclose(p,0),0,p)
    return p

np.set_printoptions(precision=5,suppress=True)
	
	
A = np.array([[1,0,0], [0,1,0], [0,0,1]])
print(A2AxisAngle(A))