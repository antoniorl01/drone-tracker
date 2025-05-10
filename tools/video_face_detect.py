import cv2 as cv


face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray_img, 1.8, 5)

    print(len(faces))

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        eye_gray = gray_img[y: y+h, x: x+w]
        eye_color = frame[y: y+h, x: x+w]
        eyes = eye_cascade.detectMultiScale(eye_gray, 1.01, 5)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(eye_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv.imshow('img', frame)  
    if cv.waitKey(1) & 0xFF == ord('q'):
        break  

cv.destroyAllWindows() 