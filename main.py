import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

tip_ids = [4, 8, 12, 16, 20]

previous_finger_count = 0  # Variable to track the previous finger count
current_action = ""  # New variable to store current action

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    fingers = []

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((id, cx, cy))

            if lm_list:
                # Thumb
                if lm_list[tip_ids[0]][1] > lm_list[tip_ids[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                # Fingers (index, middle, ring, pinky)
                for id in range(1, 5):
                    if lm_list[tip_ids[id]][2] < lm_list[tip_ids[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

    if fingers:
        total_fingers = fingers.count(1)
        cv2.putText(img, f'Fingers: {total_fingers}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 3)

        if total_fingers == 1 and previous_finger_count != 1:
            pyautogui.hotkey('space')  # Play
            current_action = "Play"

        elif total_fingers == 2 and previous_finger_count != 2:
            pyautogui.hotkey('space')  # Pause
            current_action = "Pause"

        elif total_fingers == 3:
            pyautogui.hotkey('volumeup')  # Volume Up
            current_action = "Volume Up"

        elif total_fingers == 4:
            pyautogui.hotkey('volumedown')  # Volume Down
            current_action = "Volume Down"

        elif total_fingers == 5:
            pyautogui.hotkey('nexttrack')  # Next Video
            current_action = "Next Video"

        previous_finger_count = total_fingers

    # Ye putText har frame mein chalega, action show karne ke liye
    if current_action:
        cv2.putText(img, f'Action: {current_action}', (10, 150), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
