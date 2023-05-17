import cv2
import sys
import time

device = 0
period = 1000
number = 10

for index, argument in enumerate(sys.argv):
    if argument in ("-d", "--device"):
        device = int(sys.argv[index + 1])
    elif argument in ("-p", "--period"):
        period = int(sys.argv[index + 1])
    elif argument in ("-n", "--number"):
        number = int(sys.argv[index + 1])

camera = cv2.VideoCapture(device)

# Check if the webcam is opened correctly
if not camera.isOpened():
    raise IOError("Cannot open webcam")

filename = "files/IMG_"
filecount = 0
fileextension = ".jpg"
period /= 1000

while filecount < number:
    ret, frame = camera.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    temporal_filename = filename + str(filecount) + fileextension
    cv2.imwrite(temporal_filename, frame)

    time.sleep(period)
    filecount += 1
    cv2.waitKey(1)

camera.release()
cv2.destroyAllWindows()
