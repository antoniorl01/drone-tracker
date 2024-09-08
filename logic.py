import cv2
from threading import Thread
from djitellopy import Tello
import numpy as np
from PIL import Image


def color_detector(frame, color):
    """Detects the target color in a given frame."""
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_limit, upper_limit = get_limits(color)
    mask = cv2.inRange(hsv_image, lower_limit, upper_limit)
    return mask  # Return mask for further processing (optional)

def get_limits(color):
    """Converts target color to HSV limits for color detection."""
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lower_limit = hsvC[0][0][0] #- 10, 100, 100
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
        x, y = get_center_of_rectangle(x1, y1, x2, y2)
        frame = cv2.circle(frame, (x,y), radius=3, color=(255, 0, 0), thickness=-1)
        
    return frame

def get_center_of_rectangle(x1, y1, x2, y2):
    center_x = int((x1 + x2) / 2)
    center_y = int((y1 + y2) / 2)
    return (center_x, center_y)

def find_biggest_color_apperance(frame, color):
    pass
