import cv2
import numpy as np
import pyautogui
import time
time.sleep(5)  

# Step 1: Take a screenshot
screenshot = pyautogui.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Step 2: Load face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Step 3: Convert to grayscale (face detection works better)
gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

# Step 4: Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Step 5: Draw rectangles and report
for (x, y, w, h) in faces:
    cv2.rectangle(screenshot, (x, y), (x+w, y+h), (0, 255, 0), 2)

if len(faces) > 0:
    print(f"Detected {len(faces)} face(s).")
else:
    print("No faces detected.")

# Optional: Show the screenshot with detections
cv2.imshow('Screenshot with Face Detection', screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()
