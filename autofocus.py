from imutils.video import VideoStream
from pyimagesearch.blur_detector import detect_blur_fft
import argparse
import imutils
import time
import cv2
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--thresh", type=int, default=9,
    help="threshold for our blur detector to fire")
args = vars(ap.parse_args())

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
#vs = VideoStream(src=6).start()
vs = VideoStream(src="rtsp://127.0.0.1:8554/mystream").start()
time.sleep(2.0)

# loop over the frames from the video stream
while True:
    # grab the frame from the threaded video stream and resize it
    # to have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=500)

    # convert the frame to grayscale and detect blur in it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (mean, blurry) = detect_blur_fft(gray, size=60,
        thresh=args["thresh"], vis=False)
    if blurry:
        if mean < -1:
            print("reset triggered")
            GPIO.output(26, False)
            time.sleep(2.0)
        GPIO.output(26, True)
        time.sleep(2.0)
        print("b")
    else:
        GPIO.output(26, False)
        print("f")
    print(mean)

# do a bit of cleanup
GPIO.output(26, False)
cv2.destroyAllWindows()
vs.stop()
