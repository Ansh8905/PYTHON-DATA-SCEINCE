import cv2

video = cv2.VideoCapture(0) 

while True:
    status , frame= video.read()
    
    cv2.rectangle(frame , (0,0),(frame.shape[1], 50), (255, 255, 255), -1)

    cv2.putText(frame,'live',(10,30),
        cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), 2)

    cv2.putText(frame,'webcam 0',(frame.shape[1]//2-100,30),
        cv2.FONT_HERSHEY_PLAIN, 2 , (120,0,230), 2)




    cv2.imshow("webcam 0", frame) #display a window with the web cam
    if  cv2.waitKey == ord('q'):
        break
video.release()                #release the webcam
cv2.destroyAllWindows() 
