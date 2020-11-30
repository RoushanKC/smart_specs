import cv2

video = cv2.VideoCapture("road_view.mp4")
ret = True
i = 0
j = 3772
while ret:
    ret, frame = video.read()
    #frame = cv2.resize(frame, (640, 480))
    cv2.imshow('s', frame)
    if i % 5 == 0:
        cv2.imwrite('C:/Users/ROUSHAN K/Desktop/MDD_PROJECT/SMART_SPECS/CENTRE/'+str(j)+'.jpg', frame)
        j = j+1
    i = i+1
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cv2.destroyAllWindows()
