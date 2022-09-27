import cv2

video = cv2.VideoCapture(0) 

while True:
    check, frame= video.read()
    if not check:
        break
    cv2.imshow("webcam 0", frame) #display a window with the web cam
    key = cv2.waitKey(1)  #if the key is 
    if key == ord('q'):
        break
video.release()                #release the webcam
cv2.destroyAllWindows()    #close all window