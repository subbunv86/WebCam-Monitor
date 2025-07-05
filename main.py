import cv2
import time
video = cv2.VideoCapture(0)
time.sleep(2)  # Allow camera to warm up
first_frame = None
while True:
    time.sleep(1)
    check, frame = video.read()
    gray_frame= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau =cv2.GaussianBlur(gray_frame, (5, 5), 0)

    if first_frame is None:
        first_frame = gray_frame_gau


    delta = cv2.absdiff(first_frame, gray_frame_gau)
    

    tresh =cv2.threshold(delta, 60, 255, cv2.THRESH_BINARY, dst=delta)[1]

    dilate = cv2.dilate(tresh, None, iterations=2)
    contours, _check = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 13)

    cv2.imshow("Capturing", frame)
    

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
