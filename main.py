import cv2
from threading import Thread
from djitellopy import Tello
import numpy as np
from PIL import Image
import logic

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


video_stream = video_streamer()
tello.takeoff()

try:
    # Main loop: Continuously receive frames, process for color, and potentially control the drone
    while True:
        frame = next(video_stream)
        frame = logic.draw_rectangle(frame)

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
