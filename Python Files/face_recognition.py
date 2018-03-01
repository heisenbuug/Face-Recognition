#imported Libraries
import cv2

#defined the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
#detecting eye and face

def detect(gray, frame): #gray is black and white image frame is original image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)# will give top left corner coordinate and height and width
    #gray is image, 1.3 times reduced 5 is number of neiboursi.e. in order for that pixel to be acepted 5 neibhour 
    #pixels should also be accepted
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        #image, upper left coordinate, lower right coordinate, colour, thickness
        roi_gray = gray[y:y+h, x:x+w] #defining region for eye in black and white image
        roi_colour = frame[y:y+h, x:x+w] #defining region for eye in colour image
        
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22) #same as above faces
        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_colour, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            
        smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 29)
        for(sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_colour, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
    
    return frame #we printed frame with rectangle around face and eyes

#face recog by webcam

#we need to get last frame of webcam ass on this last frame we will apply detect so to get last frame
video_capture = cv2.VideoCapture(0)#0 or 1: 0 if internal webcam 1 if external webcam
#above is the last frame coming from webcam

#to apply detect functoin on all the iamges coming from webcam
while True:
    
    ret, frame = video_capture.read() #read gives 2 return values by applying _ we will get only one returning value
    #we got last frame of webcam
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #image converts to gray
        canvas = detect(gray, frame)
        cv2.imshow('Video', canvas) #to display
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
    
        
        
    