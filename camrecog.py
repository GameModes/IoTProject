
import cv2
import numpy as np
import time
import paho.mqtt.publish as publish


MQTT_SERVER = "192.168.3.196"
MQTT_PATH = "domoticz/in"
licensedevice_id = 15
colordevice_id = 16

license_cascade = cv2.CascadeClassifier('/home/ruben/IoTProject/haarcascade_russian_plate_number.xml')
timer1 = 99999999999
timer2 = 99999999999
# capture frames from a camera
cap = cv2.VideoCapture(0)
sensor_recog_array = [0,0]

# loop runs if capturing has been initialized.
while True: 
  
    # reads frames from a camera
    ret, img = cap.read()
        
    def licenseplate(img, license_cascade, sensor_recog_array, timer2):
        # convert to gray scale of each frames
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      
        # Detects faces of different sizes in the input image
        licenseplate = license_cascade.detectMultiScale(gray, 1.3, 5)
        licensearea = 0
        for (x,y,w,h) in licenseplate:
            # To draw a rectangle
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            licensearea = ((x*y) - (w*h))
            sensor_recog_array[1] = 1
            print(sensor_recog_array)
        #print("area" + str(licensearea))
        if licensearea != 0:
            timer2 = time.time()
        if time.time() > timer2 + 5:
            sensor_recog_array[1] = 0
            
            timer2 = 99999999999
        return img, timer2
  
    def colordetection(img, sensor_recog_array, timer1):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower = np.array([30, 40, 210])
        upper = np.array([80, 255, 255])

        mask = cv2.inRange(hsv, lower, upper)
        
        kernel = np.ones((7,7),np.uint8)

        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        segmented_img = cv2.bitwise_and(img, img, mask=mask)
        
        #cv2.imshow('screen', mask)
        
        
        # Find contours from the mask
        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
        #contour = np.array([[[0,0]], [[10,0]], [[10,10]], [[5,4]]])
        if contours is not ():
            area = cv2.contourArea(np.array(contours[0]))
            if area > 10000:
                sensor_recog_array[0] = 1
                timer1 = time.time()
                
        if time.time() > timer1 + 2:
            sensor_recog_array[0] = 0
            timer1 = 99999999999
        
        return output, timer1
    print(sensor_recog_array)
    #cv2.imshow('original', img)
    
    # Showing the output
    img, timer2 = licenseplate(img, license_cascade, sensor_recog_array, timer2)
    cv2.imshow("licenseplate", img) 
          
    # Display an image in a window
    output, timer1 = colordetection(img, sensor_recog_array, timer1)
    cv2.imshow('color', output)
    
    
    publish.single(MQTT_PATH, '{ "idx" : ' + str(licensedevice_id) + ', "nvalue" : ' + str(sensor_recog_array[1]) + ', "svalue" : "Detected"}' , hostname=MQTT_SERVER)  # send data continuously every 3 seconds
    publish.single(MQTT_PATH, '{ "idx" : ' + str(colordevice_id) + ', "nvalue" : ' + str(sensor_recog_array[0]) + ', "svalue" : "Detected"}' , hostname=MQTT_SERVER)  # send data continuously every 3 seconds
    print("printed to mqqt:" + str(sensor_recog_array))
  
    # Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
  
# Close the window
cap.release()
  
# De-allocate any associated memory usage
cv2.destroyAllWindows() 
