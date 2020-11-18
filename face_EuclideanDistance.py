import numpy as np
import cv2

#欧式距离匹配，强噪声
def get_EuclideanDistance(x,y):
    myx= np.array(x)
    myy = np.array(y)
    return np.sqrt(np.sum((myy-myx)*(myy-myx)))

def findpic(img, findimg, h, fh,w, fw):
    minds = 1e8
    mincb_h = 0
    mincb_w = 0
    for now_h in range(0, h-fh):
        for now_w in range(0, w-fw):
            my_img = img[now_h:now_h+fh, now_w:now_w+fw, : ]
            my_findimg = findimg
            dis = get_EuclideanDistance(my_img, my_findimg)
            if dis < minds:
                mincb_h = now_h
                mincb_w = now_w
            minds = dis
    findpt = mincb_w, mincb_h
    cv2.rectangle(img, findpt, (findpt[0]+fw, findpt[1]+fh), (255, 0, 0))
    return img

def showpiclocation(img, findimg):
    w = img.shape[1]
    h = img.shape[0]
    fw = findimg.shape[1]
    fh = findimg.shape[0]
    return findpic(img, findimg, h, fh, w, fw)

if __name__ == '__main__':
    fn1 = ".\img.jpg" # ".\img.jpg"
    fn2 = ".\imgfind.jpg"
    
    myimg =cv2.imread(fn1)
    myfindimg = cv2.imread(fn2)
    cv2.imshow("img", myimg)
    print(myimg)
    
    myimg = showpiclocation(myimg, myfindimg)
    cv2.imshow("find img3", myimg)
    cv2.imwrite("./myimg.jpg", myimg)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
    
