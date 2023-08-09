import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

import numpy as np
import cv2
import colorsys

# init mediapipe task
BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
PoseLandmarkerResult = mp.tasks.vision.PoseLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

model_path = 'C:/Users/033/sk_opencv/Week7/0809/data/pose_landmarker_full.task'
options = PoseLandmarkerOptions(
		base_options=BaseOptions(model_asset_path=model_path),
		running_mode=VisionRunningMode.IMAGE, num_poses=1)

detector = vision.PoseLandmarker.create_from_options(options)

# for drawing limbs
pairs = list(mp.solutions.pose.POSE_CONNECTIONS)
colors = [tuple(int(255 * i) for i in colorsys.hsv_to_rgb(x / len(pairs), 1.0, 1.0)) for x in range(len(pairs))]

# initializing the webcam
cap = cv2.VideoCapture(0)

def draw_landmark(image, landmarks, pairs):
	# draw circles
	for idx, landmark in enumerate(landmarks):
		landmark_x = int(landmark.x * image_width)
		landmark_y = int(landmark.y * image_height)
		visibility = landmark.visibility
		image = cv2.circle(image, (landmark_x, landmark_y), 5, (255, 255, 255), -1)

	# draw limbs
	for pair_id, pair in enumerate(pairs):
		idx1 = pair[0]
		idx2 = pair[1]

		landmark_x_1 = int(landmarks[idx1].x * image_width)
		landmark_y_1 = int(landmarks[idx1].y * image_height)
		visibility_1 = landmarks[idx1].visibility

		landmark_x_2 = int(landmarks[idx2].x * image_width)
		landmark_y_2 = int(landmarks[idx2].y * image_height)
		visibility_2 = landmarks[idx1].visibility

		image = cv2.line(image, (landmark_x_1, landmark_y_1), (landmark_x_2, landmark_y_2), colors[pair_id], 2)

def pose_classification(landmarks):
	r_shoulder = landmarks[12]
	l_shoulder = landmarks[11]
	r_wrist = landmarks[16]
	l_wrist = landmarks[15]
	r_elbow = landmarks[14]
	l_elbow = landmarks[13]

	if r_shoulder.x < r_wrist.x and l_wrist.x < l_shoulder.x and r_shoulder.y < r_wrist.y and l_shoulder.y < l_wrist.y:
		pose_class = "ROCK"

	elif r_shoulder.x < r_wrist.x and l_wrist.y < l_shoulder.y:
		pose_class = "SCISSORS"

	elif r_wrist.x < r_shoulder.x and l_shoulder.x < l_wrist.x and r_wrist.y < r_elbow.y and l_wrist.y < l_elbow.y :
		pose_class = "PAPER"

	else:
		pose_class = ""

	return pose_class
 
while True:
	ret, image = cap.read()
	if not ret:
		break
	image_height, image_width, _ = image.shape
	
	# Convert the frame received from OpenCV to a MediaPipe’s Image object.
	mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
	detection_result = detector.detect(mp_image)

	# draw pose
	pose_landmarks_list = detection_result.pose_landmarks
	if not pose_landmarks_list:
		continue
	landmarks = pose_landmarks_list[0]
	
	# Draw pose landmarks on the input image.
	annotated_image = np.copy(image)
	draw_landmark(annotated_image, landmarks, pairs)
	pose_class = pose_classification(landmarks)
	annotated_image = cv2.putText(annotated_image, pose_class , (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
	
	cv2.imshow('frame', annotated_image)
	# quit
	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
