import numpy as np

def okoX(phi):
    A = np.array([[1,0,0],[0,np.cos(phi),-np.sin(phi)],[0,np.sin(phi),np.cos(phi)]])
    A = np.where(np.isclose(A,0),0,A)
    return A

def okoY(phi):
    A = np.array([[np.cos(phi),0,np.sin(phi)],[0,1,0],[-np.sin(phi),0,np.cos(phi)]])
    A = np.where(np.isclose(A,0),0,A)
    return A

def okoZ(phi):
    A = np.array([[np.cos(phi),-np.sin(phi),0],[np.sin(phi),np.cos(phi),0],[0,0,1]])
    A = np.where(np.isclose(A,0),0,A)
    return A
    
def Euler2A(uglovi):
    A = okoZ(uglovi[0]).dot(okoY(uglovi[1]).dot(okoX(uglovi[2])))
    A = np.where(np.isclose(A,0),0,A)
    return A

np.set_printoptions(precision=5,suppress=True)
uglovi = np.array([np.pi/2,-np.pi/4,(7/8)*np.pi])
print(Euler2A(uglovi))