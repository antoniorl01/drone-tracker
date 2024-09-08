import cv2
import logic

def laptop_video_streamer():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame = cap.read()
    
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        frame = test_draw_rectangle(frame)
        yield frame
    
    cap.release()
    cv2.destroyAllWindows()


def test_color_detector(frame):
    color = [18, 105, 255] 
    mask = logic.color_detector(frame=frame, color=color)
    return mask
    

def test_draw_rectangle(frame):
    color = [18, 105, 255] 
    mask = logic.color_detector(frame=frame, color=color)
    frame = logic.draw_rectangle(frame=frame, mask=mask)
    return frame



"""DETECTS THE COLOR ORANGE"""
# frame = test_color_detector()

"""DRAWS A RECTANGLE AROUND THE MASK """
#frame = test_draw_rectangle("ria.png")

"""TESTING REAL TIME"""
#while True:
#    frame = laptop_video_streamer()
#    cv2.imshow("WebCam", frame)


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
 
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame = test_draw_rectangle(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()