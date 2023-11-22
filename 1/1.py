def cross(a,b):
    x = a[1]*b[2]-a[2]*b[1]
    y = a[2]*b[0]-a[0]*b[2]
    z = a[0]*b[1]-a[1]*b[0]
    return [x,y,z]    

def osmoteme(a):
    prava1 = cross([a[0][0],a[0][1],1],[a[4][0],a[4][1],1])
    prava2 = cross([a[1][0],a[1][1],1],[a[5][0],a[5][1],1])
    presek1 = cross(prava1,prava2)
    
    prava3 = cross([a[0][0],a[0][1],1],[a[3][0],a[3][1],1])
    prava4 = cross([a[1][0],a[1][1],1],[a[2][0],a[2][1],1])
    presek2 = cross(prava3,prava4)
    
    prava5 = cross(presek1,[a[3][0],a[3][1],1])
    prava6 = cross(presek2,[a[4][0],a[4][1],1])
    
    presek3 = cross(prava5,prava6)
    presek3 = list(map(lambda x: x/presek3[2],presek3))
    return [int(presek3[0]),int(presek3[1])]



print(osmoteme([[32, 70], [195, 144], [195, 538], [30, 307], [251, 40], [454, 78], [455, 337]]))