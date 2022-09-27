import cv2
filepath=r"C:\Users\Asus\Videos\Doraemon S01EP01.mp4"
video = cv2.VideoCapture(filepath) 

while True:
    check, frame= video.read()
    if not check:
        break
    cv2.imshow("webcam 0", frame) #display a window with the web cam
    key = cv2.waitKey(1)  #if the key is 
    if key == ord('q'):
        break
video.release()                #release the webcam
cv2.destroyAllWindows()   