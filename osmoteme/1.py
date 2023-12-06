import cv2
path = './slika.jpeg'
image = cv2.imread(path)
windowName = 'box'
cv2.imshow(windowName, image)

corners = []

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
    print()
    print('P8: (',int(presek3[0]),', ',int(presek3[1]),')',sep='')
    return presek3


def onClick(event,x,y,flags,data):
    if event == cv2.EVENT_FLAG_LBUTTON and len(corners) < 7:
        print('P', len(corners)+1, ': (', x, ', ', y, ')', sep='')
        cv2.putText(image,'X',(x-15,y+12),cv2.FONT_HERSHEY_PLAIN,3,(0,255,100),3,cv2.LINE_AA)
        cv2.imshow('image',image)
        corners.append([x,y])
        if len(corners) == 7:
            teme = osmoteme(corners)
            x = int(teme[0])
            y = int(teme[1])
            cv2.putText(image,'X',(x-15,y+12),cv2.FONT_HERSHEY_PLAIN,3,(0,0,225),3,cv2.LINE_AA)
            cv2.imshow('image',image)

cv2.setMouseCallback(windowName, onClick)
cv2.waitKey(0)
cv2.destroyAllWindows()