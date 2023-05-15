import base64
import numpy as np

import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands


def track_fingers(image):
    with mp_hands.Hands(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        image_data = base64.b64decode(image.split(',')[1])
        nparr = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        results = hands.process(image)

        # Initially set finger count to 0 for each cap
        finger_count = 0

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:
                # Get hand index to check label (left or right)
                handIndex = results.multi_hand_landmarks.index(hand_landmarks)
                handLabel = results.multi_handedness[handIndex].classification[0].label

                # Set variable to keep landmarks positions (x and y)
                handLandmarks = []

                # Fill list with x and y positions of each landmark
                for landmarks in hand_landmarks.landmark:
                    handLandmarks.append([landmarks.x, landmarks.y])

                # Test conditions for each finger: Count is increased if finger is
                #   considered raised.
                # Thumb: TIP x position must be greater or lower than IP x position,
                #   deppeding on hand label.
                if handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
                    finger_count = finger_count + 1
                elif handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
                    finger_count = finger_count + 1

                # Other fingers: TIP y position must be lower than PIP y position,
                #   as image origin is in the upper left corner.
                if handLandmarks[8][1] < handLandmarks[6][1]:  # Index finger
                    finger_count = finger_count + 1
                if handLandmarks[12][1] < handLandmarks[10][1]:  # Middle finger
                    finger_count = finger_count + 1
                if handLandmarks[16][1] < handLandmarks[14][1]:  # Ring finger
                    finger_count = finger_count + 1
                if handLandmarks[20][1] < handLandmarks[18][1]:  # Pinky
                    finger_count = finger_count + 1

        # Display finger count
        return finger_count, image
