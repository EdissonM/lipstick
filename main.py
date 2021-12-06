import cv2
import dlib
import numpy as np

import faceBlendCommon as fbc

# Landmark model location
PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"

# Get the face detector
faceDetector = dlib.get_frontal_face_detector()
# The landmark detector is implemented in the shape_predictor class
landmarkDetector = dlib.shape_predictor(PREDICTOR_PATH)

im = cv2.imread("girl-no-makeup.jpg")

RGB_image = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

points = fbc.getLandmarks(faceDetector, landmarkDetector, RGB_image)

# Use mouth points according predictor_68_face_landmarks.
mouth_points = points[48:60]
# Get mask same size original image.
mask = 255 * np.ones((im.shape[0], im.shape[1], 3), dtype=np.uint8)
# Fill mask according using mouth points and convex polygon.
cv2.fillConvexPoly(mask, np.int32(mouth_points), (0, 0, 0))
# Apply a gaussian smoothing in the border lips.
mask = cv2.GaussianBlur(mask, (13, 13), cv2.BORDER_DEFAULT)
# Using mask get image without mouth.
not_mouth = cv2.multiply(mask.astype(float) / 255, im.astype(float) / 255)

# Get negative mask
not_mask = cv2.bitwise_not(mask)
# Using negative mask extract only mouth.
mouth = cv2.multiply(not_mask.astype(float) / 255, im.astype(float) / 255)
# Convert mouth image to HSV
imgHSV = cv2.cvtColor(((mouth * 255).astype(np.uint8)), cv2.COLOR_BGR2HSV)
# Move hue for take new lips color.
# https://en.wikipedia.org/wiki/HSL_and_HSV
imgHSV[:, :, 0] = imgHSV[:, :, 0] - 100
# Convert HSV to BRG
mouth = cv2.cvtColor(imgHSV, cv2.COLOR_HSV2BGR).astype(float) / 255

# Image result is image without mouth and mouth image.
lipstick = mouth + not_mouth

# Save and show results.
cv2.imshow("Lipstick", lipstick)
cv2.imwrite("Lipstick.jpg", (lipstick * 255).astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
