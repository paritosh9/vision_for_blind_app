import cv2
import time

# Create an object. Zero for external camera
# To capture a video, you need to create a VideoCapture object.
# Its argument can be either the device index or the name of a video file.
# Device index is just the number to specify which camera.
# Normally one camera will be connected (as in my case). So I simply pass 0 (or -1).
# You can select the second camera by passing 1 and so on.
# After that, you can capture frame-by-frame.
# But at the end, don’t forget to release the capture.
video = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not video.isOpened():
    raise IOError("Cannot open webcam")

# a variable
number_of_frames_captured = 0

#while True:
number_of_frames_captured = number_of_frames_captured + 1

# Create a frame object
# video.read() returns a bool (True/False).
# If frame is read correctly, it will be True.
# So you can check end of the video by checking this return value.
check, frame = video.read()

# print return value (check) and frame.shape (matrix dimensions)
print('video.read() Return value - ', check)
print('frame matrix dimensions - ', frame.shape)
h, w, c = frame.shape
#print(frame)  #Representing Image

# Converting to grayscale
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
print('frame matrix dimensions after grayscaling - ', gray_frame.shape)

# Show the frame
# cv2.imshow() method is used to display an image in a window.
# The window automatically fits to the image size
cv2.imshow("Capturing", gray_frame)

# For press any key to out (milliseconds)
#cv2.waitKey(1)

# For Playing
# The function waitKey waits for a key event infinitely (when delay < 0 ) or for delay milliseconds, when it is positive.
# Since the OS has a minimum time between switching threads, the function will not wait exactly delay ms,
# it will wait at least delay ms, depending on what else is running on your computer at that time.
# It returns the code of the pressed key or -1 if no key was pressed before the specified time had elapsed.
key = cv2.waitKey(0)  # 0 for image

#if key == ord('q'):
#    break

print('number of frame - ', number_of_frames_captured)

# write frame to image file
filename = "tiger.jpg"
# Saves an image to a specified file.
cv2.imwrite(filename, gray_frame)

# Shutdown the camera
# Closes video file or capturing device
video.release()

# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()
