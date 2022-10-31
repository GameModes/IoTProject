import numpy as np
import cv2


cap = cv2.VideoCapture(0)
while True:
    #screen =  np.array(ImageGrab.grab())
    ret, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #Help
    lower = np.array([30, 50, 180])
    upper = np.array([80, 90, 255])

    mask = cv2.inRange(hsv, lower, upper)
    
    kernel = np.ones((7,7),np.uint8)

    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    segmented_img = cv2.bitwise_and(img, img, mask=mask)
    
    #cv2.imshow('screen', mask)
    cv2.imshow('original', img)
    
    # Find contours from the mask
    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
    # Showing the output
    cv2.imshow("Output", output)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    
