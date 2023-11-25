import numpy as np

def norm(p):
    s = np.sqrt(sum([x*x for x in p]))
    p = [x/s for x in p]
    return p

def isNorm(p):
    s = np.sqrt(sum(x*x for x in p))
    return s == 1

def AxisAngle2A(pphi):
    # pphi = [px,py,pz,angle]
    pt = np.array([pphi[i] for i in range(3)])[np.newaxis]
    p = pt[0]
    phi = pphi[3]
    if not isNorm(p):
        p = norm(p)
        print('norm pe',p)
        pt = np.array([p[i] for i in range(3)])[np.newaxis]
    ppt = np.dot(pt.T,pt)  # dobar
    
    eppt = np.cos(phi) * (np.eye(3,3) - ppt) # dobar
    
    px = np.sin(phi) * np.array([[0,-p[2],p[1]],[p[2],0,-p[0]],[-p[1],p[0],0]])
    
    A= ppt + eppt + px
    A = np.where(np.isclose(A,0),0,A)
    return A
    
np.set_printoptions(precision=5,suppress=True)
pphi = np.array([1/3,-2/3,2/3,np.pi/2])
print(AxisAngle2A(pphi))

# pphi = np.array([1,2,3,np.pi/2])
# print(AxisAngle2A(pphi))
