import cv2
from threading import Thread
from djitellopy import Tello
import numpy as np
from PIL import Image

tello = Tello()
tello.connect()

# Define target color
target_color = [6, 105, 255] 

def video_streamer():
    """Continuously captures frames from the drone and sends them for processing."""
    tello.streamon()
    while True:
        frame_read = tello.get_frame_read()
        yield frame_read.frame  # Yield frame for processing in main loop

def color_detector(frame):
    """Detects the target color in a given frame."""
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_limit, upper_limit = get_limits(target_color)
    mask = cv2.inRange(hsv_image, lower_limit, upper_limit)
    return mask  # Return mask for further processing (optional)

def get_limits(color):
    """Converts target color to HSV limits for color detection."""
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lower_limit = hsvC[0][0][0] - 10, 100, 100
    upper_limit = hsvC[0][0][0] + 10, 255, 255

    lower_limit = np.array(lower_limit, dtype=np.uint8) 

    upper_limit = np.array(upper_limit, dtype=np.uint8)

    return lower_limit, upper_limit 

def draw_rectangle(frame, mask):
    """If object is detected using the mask, there a rectangle is drawn on the object."""
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    return frame


video_stream = video_streamer()
tello.takeoff()

try:
    # Main loop: Continuously receive frames, process for color, and potentially control the drone
    while True:
        frame = next(video_stream)
        # Process frame for color detection (using color_detector function if needed)
        # Based on detection results, you can control the drone here (e.g., move towards target)
        cv2.imshow('Drone Stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if tello.get_battery() < 5:
            tello.land()
            break

except KeyboardInterrupt:
    print("Exiting...")

tello.land()
cv2.destroyAllWindows()
